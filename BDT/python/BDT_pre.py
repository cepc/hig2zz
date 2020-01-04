#!/usr/bin/env python

import sys
import os
import math
import ROOT
from ROOT import TLorentzVector
from progressbar import Bar, Percentage, ProgressBar
from array import array
from time import time
from tools import duration, check_outfile_path

def usage():
    sys.stdout.write('''
NAME 
    BDT_pre.py

SYNOPSIS
  
    ./BDT_pre.py infile outfile combine_opt (1: llhzz, 2: nnhzz, 3: qqhzz) flag_zz (1: vv jj/ll, 2: jj/ll vv) flag (0: signal, 1: zh_background, 2: background)

AUTHOR 
    Min Zhong <zmind@mail.ustc.edu.cn>

DATE
    JULY 2019
\n''')


# Event Flow Plot
h_evtflw = ROOT.TH1D('h_evtflw_beforeBDT', 'eventflow', 10, 0, 10)

def main():

    args = sys.argv[1:]
    if len(args) < 5:
        return usage()

    infile = args[0]
    outfile = args[1]
    combine_opt = int(args[2])
    flag_zz = int(args[3])
    flag = int(args[4])

    fin = ROOT.TFile(infile)
    t_in = fin.Get('tree')
    entries = t_in.GetEntriesFast()

    if entries > 0:
        pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=entries).start()

    time_start = time()

    # event flow plot definition
    h_evtflw.GetXaxis().SetBinLabel(1,'Raw')
    h_evtflw.GetXaxis().SetBinLabel(2,'Pre-selection')
    h_evtflw.GetXaxis().SetBinLabel(3,'Is signal')

    if (combine_opt==1):
	if (flag_zz==1):
	    h_evtflw.GetXaxis().SetBinLabel(4,'M_miss > M_dijet')
	    h_evtflw.GetXaxis().SetBinLabel(5,'80<M_dimuon<100')
	    h_evtflw.GetXaxis().SetBinLabel(6,'120<M_dimuon_rec<150')
	    h_evtflw.GetXaxis().SetBinLabel(7,'15<npfo<70')
	    h_evtflw.GetXaxis().SetBinLabel(8,'Pt(visible)>10')

	if (flag_zz==2):
	    h_evtflw.GetXaxis().SetBinLabel(4,'M_miss > M_dijet')
	    h_evtflw.GetXaxis().SetBinLabel(5,'80<M_dimuon<100')
	    h_evtflw.GetXaxis().SetBinLabel(6,'120<M_dimuon_rec<150')
	    h_evtflw.GetXaxis().SetBinLabel(7,'30<npfo<100')
	    h_evtflw.GetXaxis().SetBinLabel(8,'10<Pt(visible)<50')

    if (combine_opt==2):
            h_evtflw.GetXaxis().SetBinLabel(4,'N(pfo) >= 10')
	    h_evtflw.GetXaxis().SetBinLabel(5,'115<Vis_Mass<130')
	    h_evtflw.GetXaxis().SetBinLabel(6,'|Cos_Theta|<0.9')

    if (combine_opt==3):
	if (flag_zz==1):
	    h_evtflw.GetXaxis().SetBinLabel(4,'Missing mass > dimuon mass')
	    h_evtflw.GetXaxis().SetBinLabel(5,'35<nPFO<107')
	    h_evtflw.GetXaxis().SetBinLabel(6,'70<Dijet_Mass<110')
	    h_evtflw.GetXaxis().SetBinLabel(7,'|Cos_Theta|<0.94')
	    h_evtflw.GetXaxis().SetBinLabel(8,'Visible Mass~[103, 179]')

	if (flag_zz==2):
	    h_evtflw.GetXaxis().SetBinLabel(4,'Missing mass < dimuon mass')
	    h_evtflw.GetXaxis().SetBinLabel(5,'29<nPFO<105')
	    h_evtflw.GetXaxis().SetBinLabel(6,'70<Dijet_Mass<110')
	    h_evtflw.GetXaxis().SetBinLabel(7,'|Cos_Theta|<0.94')
	    h_evtflw.GetXaxis().SetBinLabel(8,'Visible Mass~[164, 222]')

    # event flow copying
    h_evtflw_in = fin.Get("hevtflw")
    c1 = h_evtflw_in.GetBinContent(1)
    h_evtflw.SetBinContent(1, c1)

    # output file
    fout = ROOT.TFile(outfile, "RECREATE")
    t = ROOT.TTree('tree', 'tree')

    dimuon_rec_m =  array( 'd', [0] )
    dijet_rec_m = array( 'd', [0] )
    vis_all_p =  array( 'd', [0] )
    vis_all_pt = array( 'd', [0] )
    vis_all_m =  array( 'd', [0] )
    dijet_m =  array( 'd', [0] )
    jet_lead_e =  array( 'd', [0] )
    jet_sub_e =  array( 'd', [0] )
    dimuon_dijet_angle =  array( 'd', [0] )
    n_col_reco =  array( 'i', [0] )
    dimuon_m =  array( 'd', [0] )
    cos =  array( 'd', [0] )
    vis_all_rec_m =  array( 'd', [0] )
    dalitz_mzz = array( 'd', [0] )
    dalitz_mzz_star = array( 'd', [0] )

    t.Branch( 'dimuon_rec_m', dimuon_rec_m, 'dimuon_rec_m/D')
    t.Branch( 'dijet_rec_m', dijet_rec_m, 'dijet_rec_m/D')
    t.Branch( 'vis_all_p', vis_all_p, 'vis_all_p/D')
    t.Branch( 'vis_all_pt', vis_all_pt, 'vis_all_pt/D')
    t.Branch( 'vis_all_m', vis_all_m, 'vis_all_m/D')
    t.Branch( 'dijet_m', dijet_m, 'dijet_m/D')
    t.Branch( 'jet_lead_e', jet_lead_e, 'jet_lead_e/D')
    t.Branch( 'jet_sub_e', jet_sub_e, 'jet_sub_e/D')
    t.Branch( 'dimuon_dijet_angle', dimuon_dijet_angle, 'dimuon_dijet_angle/D')
    t.Branch( 'n_col_reco', n_col_reco, 'n_col_reco/I')
    t.Branch( 'dimuon_m', dimuon_m, 'dimuon_m/D')
    t.Branch( 'cos', cos, 'cos/D')
    t.Branch( 'vis_all_rec_m', vis_all_rec_m, 'vis_all_rec_m/D')

    # read trees
    for jentry in xrange(entries):
        pbar.update(jentry+1)
        #get the next tree in the chain and verify
        ientry = t_in.LoadTree(jentry)
        if ientry < 0:
            break
        # copy next entry into memory and verify

        nb = t_in.GetEntry(jentry)
        if nb<=0:
            continue

        # Raw event number (after pre-selection)
        h_evtflw.Fill(1)

        # use truth information of not
        sel = 0
        if( flag==0 and is_signal(t_in, combine_opt) ):
            sel = 1
        # not Signal 
        if( flag==1 and not(is_signal(t_in, combine_opt)) ):
            sel = 1
        if( flag==2 ):
            sel = 1

        # Cut begins
        if (sel):
            if (combine_opt==1):
		if (flag_zz==1):
	            Cut_Missing_dijet = ( t_in.vis_all_rec_m > t_in.dijet_m[0] )
	            Cut_Dimuon_Mass = ( 80 < t_in.dimuon_m[0] and t_in.dimuon_m[0] < 100 )
	            Cut_Dimuon_Rec_Mass = ( 120 < t_in.dimuon_rec_m[0] and t_in.dimuon_rec_m[0] < 150 )
		    Cut_Npfo = ( 15 < t_in.n_col_reco and t_in.n_col_reco < 70 )
		    Cut_Vis_Pt = ( t_in.vis_all_pt > 10 )
		if (flag_zz==2):
	            Cut_Missing_dijet = ( t_in.vis_all_rec_m < t_in.dijet_m[0] )
	            Cut_Dimuon_Mass = ( 80 < t_in.dimuon_m[0] and t_in.dimuon_m[0] < 100 )
	            Cut_Dimuon_Rec_Mass = ( 120 < t_in.dimuon_rec_m[0] and t_in.dimuon_rec_m[0] < 150 )
	            Cut_Npfo = ( 30 < t_in.n_col_reco and t_in.n_col_reco < 100 )
	            Cut_Vis_Pt = ( 10 < t_in.vis_all_pt and t_in.vis_all_pt < 50 )

                BDT_pre_cut = 0
                BDT_pre_cut = Cut_Missing_dijet * Cut_Dimuon_Mass * Cut_Dimuon_Rec_Mass * Cut_Npfo * Cut_Vis_Pt

	        # event flow and filling
	        h_evtflw.Fill(2)
	        if (Cut_Missing_dijet):
	            h_evtflw.Fill(3)
	        if (Cut_Missing_dijet and Cut_Dimuon_Mass):
	            h_evtflw.Fill(4)
	        if (Cut_Missing_dijet and Cut_Dimuon_Mass and Cut_Dimuon_Rec_Mass):
	            h_evtflw.Fill(5)
	        if (Cut_Missing_dijet and Cut_Dimuon_Mass and Cut_Dimuon_Rec_Mass and Cut_Npfo):
		    h_evtflw.Fill(6)
		if (Cut_Missing_dijet and Cut_Dimuon_Mass and Cut_Dimuon_Rec_Mass and Cut_Npfo and Cut_Vis_Pt):
	            h_evtflw.Fill(7)

	    if (combine_opt==2):
                Cut_Npfo = ( t_in.n_col_reco >= 10 )
                Cut_Visible_Mass = ( 115 < t_in.vis_all_m and t_in.vis_all_m < 135 )
                Cut_CosTheta = ( -0.9 < t_in.cos and t_in.cos < 0.9 )
 		
		BDT_pre_cut = 0
		BDT_pre_cut = Cut_Npfo * Cut_Visible_Mass * Cut_CosTheta

                # event flow and filling
                h_evtflw.Fill(2)
                if (Cut_Npfo):
                    h_evtflw.Fill(3)
                if (Cut_Npfo and Cut_Visible_Mass):
                    h_evtflw.Fill(4)
                if (Cut_Npfo and Cut_Visible_Mass and Cut_CosTheta):
                    h_evtflw.Fill(5)

	    if (combine_opt==3):
		if (flag_zz==1):
	    	    Cut_Missing_dimuon = ( t_in.vis_all_rec_m > t_in.dimuon_m[0] )
	            Cut_Npfo = ( 35 < t_in.n_col_reco and t_in.n_col_reco < 107 )
	            Cut_Dijet_Mass = ( 70 < t_in.dijet_m[0] and t_in.dijet_m[0] < 110 )
	            Cut_CosTheta = ( -0.94 < t_in.cos and t_in.cos < 0.94 )
	            Cut_Visible_Mass = ( 103 < t_in.vis_all_m and t_in.vis_all_m < 179 )
		if (flag_zz==2):
        	    Cut_Missing_dimuon = ( t_in.vis_all_rec_m < t_in.dimuon_m[0] )
	            Cut_Npfo = ( 29 < t_in.n_col_reco and t_in.n_col_reco < 105 )
	            Cut_Dijet_Mass = ( 70 < t_in.dijet_m[0] and t_in.dijet_m[0] < 110 )
	            Cut_CosTheta = ( -0.94 < t_in.cos and t_in.cos < 0.94 )
        	    Cut_Visible_Mass = ( 164 < t_in.vis_all_m and t_in.vis_all_m < 222 )

                BDT_pre_cut = 0
                BDT_pre_cut = Cut_Missing_dimuon * Cut_Npfo * Cut_Dijet_Mass * Cut_CosTheta * Cut_Visible_Mass

	        # event flow and filling
         	h_evtflw.Fill(2)
         	if (Cut_Missing_dimuon):
                    h_evtflw.Fill(3)
        	if (Cut_Missing_dimuon and Cut_Npfo):
                    h_evtflw.Fill(4)
	        if (Cut_Missing_dimuon and Cut_Npfo and Cut_Dijet_Mass):
	            h_evtflw.Fill(5)
	        if (Cut_Missing_dimuon and Cut_Npfo and Cut_Dijet_Mass and Cut_CosTheta):
	            h_evtflw.Fill(6)
	        if (Cut_Missing_dimuon and Cut_Npfo and Cut_Dijet_Mass and Cut_CosTheta and Cut_Visible_Mass):
	            h_evtflw.Fill(7)

	    # Several cuts before BDT
            if (BDT_pre_cut):
                dimuon_rec_m[0] =  t_in.dimuon_rec_m[0]
		dijet_rec_m[0] = t_in.dijet_rec_m[0]
                vis_all_p[0] = t_in.vis_all_p
		vis_all_pt[0] = t_in.vis_all_pt
                vis_all_m[0] = t_in.vis_all_m
                dijet_m[0] = t_in.dijet_m[0]
                jet_lead_e[0] = t_in.jet_lead_e[0]
                jet_sub_e[0] =  t_in.jet_sub_e[0]
                dimuon_dijet_angle[0] = t_in.lj_angle
                n_col_reco[0] = t_in.n_col_reco
                dimuon_m[0] =  t_in.dimuon_m[0]
                cos[0] = t_in.cos
                vis_all_rec_m[0] = t_in.vis_all_rec_m

                t.Fill()
         
    fout.Write()

    h_evtflw.Write()

    fout.Close()

    if entries > 0 :
        pbar.finish()

    dur = duration(time()-time_start)
    sys.stdout.write(' \nDone in %s. \n' % dur)

def is_signal(t, combine_opt):

    # mm/nn/qq + Higgs(->ZZ)
    MuonMinus = 0
    MuonPlus = 0
    NeutrinoMinus = 0
    NeutrinoPlus = 0
    QuarkPlus = 0
    QuarkMinus = 0
    hig = 0

    if ( t.mc_lepton_minus_id == 13 ):
        MuonMinus = 1
    if ( t.mc_lepton_plus_id == -13 ):
        MuonPlus = 1
    if ( t.mc_neutrino_minus_id == 12 or t.mc_neutrino_minus_id == 14 or t.mc_neutrino_minus_id == 16 ):
        NeutrinoMinus = 1
    if ( t.mc_neutrino_plus_id == -12 or t.mc_neutrino_plus_id == -14 or t.mc_neutrino_plus_id == -16 ):
        NeutrinoPlus = 1
    if ( t.mc_quark_minus_id == 1 or t.mc_quark_minus_id == 2 or t.mc_quark_minus_id == 3 or t.mc_quark_minus_id == 4 or t.mc_quark_minus_id == 5 or t.mc_quark_minus_id == 6 ):
        QuarkMinus = 1
    if ( t.mc_quark_plus_id == -1 or t.mc_quark_plus_id == -2 or t.mc_quark_plus_id == -3 or t.mc_quark_plus_id == -4 or t.mc_quark_plus_id == -5 or t.mc_quark_plus_id == -6):
        QuarkPlus = 1

    if ( combine_opt==1 and (t.mc_zz_flag == 12 or t.mc_zz_flag == 21)):
        hig = 1
    if ( combine_opt==2 and (t.mc_zz_flag == 13 or t.mc_zz_flag == 31)):
        hig = 1
    if ( combine_opt==3 and (t.mc_zz_flag == 23 or t.mc_zz_flag == 32)):
        hig = 1

    if ( combine_opt==1 ):
        signal_flag = MuonMinus * MuonPlus * hig
    if ( combine_opt==2 ):
        signal_flag = NeutrinoMinus * NeutrinoPlus * hig
    if ( combine_opt==3 ):
        signal_flag = QuarkMinus * QuarkPlus * hig

    return signal_flag
 
if __name__ == '__main__':
        main()                                                                                                                                             
