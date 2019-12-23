#!/usr/bin/env python
"""
Event Selection

## Inspired from an event selection script for J/psi->invisible
"""

__author__ = "R. Kiuchi <kiuchi@ihep.ac.cn>"
__copyright__ = "Copyright (c) Ryuta Kiuchi"
__created__ = "[2018-06-06 ]" 

import sys
import os
import math
import ROOT
from progressbar import Bar, Percentage, ProgressBar
from array import array
from time import time
from tools import duration, check_outfile_path

#TEST=True 
TEST=False

# Flag
ZZ_Selection = int(sys.argv[1])     # 1: Z->nunu, Z*->jj/mm,  2: Z->jj/mm, Z*->nunu , 3: Both 

# Global constants 
Z_MASS = 91.2

# Global histograms

## Event Flow
h_evtflw = ROOT.TH1D('hevtflw_sel','eventflow',20,0,20)
h_evtflw_pre = ROOT.TH1D('hevtflw_pre','eventflow',20,0,20)

## After Pre-Selection 
h_m_dimuon_raw = ROOT.TH1D('h_m_dimuon_raw', 'm_dimuon_raw', 260, 0, 260)
h_mrec_dimuon_raw = ROOT.TH1D('h_mrec_dimuon_raw', 'mrec_dimuon_raw', 260, 0, 260)
h_m_dijet_raw =  ROOT.TH1D('h_m_dijet_raw', 'm_dijet_raw', 260, 0, 260)
h_mrec_dijet_raw =  ROOT.TH1D('h_mrec_dijet_raw', 'mrec_dijet_raw', 260, 0, 260)
h_m_visible_raw =  ROOT.TH1D('h_m_visible_raw', 'm_visible_raw', 260, 0, 260)
h_m_missing_raw =  ROOT.TH1D('h_m_missing_raw', 'm_missing_raw', 260, 0, 260)
h_vis_all_pt_raw =  ROOT.TH1D('h_vis_all_pt_raw', 'vis_all_pt_raw', 100, 0, 100)
h_vis_all_m_raw =  ROOT.TH1D('h_vis_all_m_raw', 'vis_all_m_raw', 240, 0, 240)
h_vis_all_p_raw =  ROOT.TH1D('h_vis_all_p_raw', 'vis_all_p_raw', 80, 0, 80)
h_vis_all_rec_m_raw =  ROOT.TH1D('h_vis_all_rec_m_raw', 'vis_all_rec_m_raw', 300,-50, 250)
h_vis_all_cos_raw =  ROOT.TH1D('h_vis_all_cos_raw', 'vis_all_cos_raw', 100, -1, 1)
h_cos_raw =  ROOT.TH1D('h_cos_raw', 'cos_raw', 100, -1, 1)
h_npfo_raw = ROOT.TH1D('h_npfo_raw','h_npfo_raw',200,0,200)
h_jet_lead_e_raw = ROOT.TH1D('h_jet_lead_e_raw','h_jet_lead_e_raw',200,0,200);
h_jet_sub_e_raw = ROOT.TH1D('h_jet_sub_e_raw','h_jet_sub_e_raw',200,0,200);
h_angle_mj_raw = ROOT.TH1D('h_angle_mj_raw','h_angle_mj_raw',180,0,180);

h_2D_visible_missing_raw =  ROOT.TH2D('h_2D_visible_missing_raw', '2D_visible_missing_raw', 240, -20, 220, 240, -40, 200)
h_2D_dijet_missing_raw =  ROOT.TH2D('h_2D_dijet_missing_raw', '2D_dijet_missing_raw', 240, -20, 220, 240, -40, 200)

## After All of Cuts
h_m_dimuon_final = ROOT.TH1D('h_m_dimuon_final', 'm_dimuon_final', 260, 0, 260)
h_mrec_dimuon_final = ROOT.TH1D('h_mrec_dimuon_final', 'mrec_dimuon_final', 260, 0, 260)
h_m_dijet_final =  ROOT.TH1D('h_m_dijet_final', 'm_dijet_final', 260, 0, 260)
h_mrec_dijet_final =  ROOT.TH1D('h_mrec_dijet_final', 'mrec_dijet_final', 260, 0, 260)
h_m_visible_final =  ROOT.TH1D('h_m_visible_final', 'm_visible_final', 260, 0, 260)
h_m_missing_final =  ROOT.TH1D('h_m_missing_final', 'm_missing_final', 260, 0, 260)
h_vis_all_pt_final =  ROOT.TH1D('h_vis_all_pt_final', 'vis_all_pt_final', 100, 0, 100)
h_vis_all_m_final =  ROOT.TH1D('h_vis_all_m_final', 'vis_all_m_final', 50, 100, 150)
h_vis_all_p_final =  ROOT.TH1D('h_vis_all_p_final', 'vis_all_p_final', 80, 0, 80)
h_vis_all_rec_m_final =  ROOT.TH1D('h_vis_all_rec_m_final', 'vis_all_rec_m_final', 300, -50, 250)
h_vis_all_cos_final =  ROOT.TH1D('h_vis_all_cos_final', 'vis_all_cos_final', 100, -1, 1)
h_cos_final =  ROOT.TH1D('h_cos_final', 'cos_final', 100, -1, 1)
h_npfo_final = ROOT.TH1D('h_npfo_final','h_npfo_final',200,0,200)
h_jet_lead_e_final = ROOT.TH1D('h_jet_lead_e_final','h_jet_lead_e_final',200,0,200)
h_jet_sub_e_final = ROOT.TH1D('h_jet_sub_e_final','h_jet_sub_e_final',200,0,200)
h_angle_mj_final = ROOT.TH1D('h_angle_mj_final','h_angle_mj_final',180,0,180)
h_m_lljj = ROOT.TH1D('h_m_lljj', 'm_lljj', 260, 0, 260)
h_2D_visible_missing_final =  ROOT.TH2D('h_2D_visible_missing_final', '2D_visible_missing_final', 240, -20, 220, 240, -40, 200)
h_2D_dijet_missing_final =  ROOT.TH2D('h_2D_dijet_missing_final', '2D_dijet_missing_final', 240, -20, 220, 240, -40, 200)

h_y12 = ROOT.TH1D('h_y12', 'y12', 4000, -2, 2)
h_y23 = ROOT.TH1D('h_y23', 'y23', 4000, -2, 2)
h_y34 = ROOT.TH1D('h_y34', 'y34', 4000, -2, 2)

h_mc_init_plist = ROOT.TH1D('h_mc_init_plist', 'mc_init_plist', 80, -40, 40)
h_mc_higgs_dlist = ROOT.TH1D('h_mc_higgs_dlist', 'mc_higgs_dlist', 80, -40, 40)
h_m_mc_zz_flag = ROOT.TH1D('h_m_mc_zz_flag', 'mc_zz_flag', 80, -40, 40)

def usage():
    sys.stdout.write('''
NAME
    sel_events.py 

SYNOPSIS

    ./sel_events.py infile outfile flag ( 0: all, 1: select signal, 2: not signal )

AUTHOR 
    Ryuta Kiuchi  <kiuchi@ihep.ac.cn> 

DATE
    June 2018 
\n''')


def main():

    args = sys.argv[2:]
    if len(args)<2:
        return usage()

    infile  = args[0]
    outfile = args[1]

    if len(args)==3: # default: all pass
        flag = 0
    else:            # or , set flag 
        flag = int(args[2]) 

    combine_opt = int(sys.argv[5]);

    fin = ROOT.TFile(infile)
    t_in = fin.Get('tree')
    entries = t_in.GetEntriesFast()

    if entries > 0 :
        pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=entries).start()

    time_start = time()

    # output file & TTree definition
    fout = ROOT.TFile(outfile, "RECREATE")
    t = ROOT.TTree( 'Higgs Tree', 'Higgs Tree' )

    dimuon_m = array( 'd', [0] )
    dimuon_rec_m = array( 'd', [0] )
    dijet_m = array( 'd', [0] )
    dijet_rec_m = array( 'd', [0] )
    vis_ex_dimuon_m = array( 'd', [0] )
    vis_all_rec_m = array( 'd', [0] )
    vis_all_pt = array( 'd', [0] )
    vis_all_m = array( 'd', [0] )
    vis_all_p = array( 'd', [0] )
    vis_all_rec_m = array( 'd', [0] )
    vis_all_cos = array( 'd', [0] )
    npfo = array( 'd', [0] )
    cos = array( 'd', [0] )
    jet_lead_e = array( 'd', [0] )
    jet_sub_e = array( 'd', [0] )
    angle_mj = array( 'd', [0] )

    t.Branch( 'dimuon_m', dimuon_m, 'dimuon_m/D')
    t.Branch( 'dimuon_rec_m', dimuon_rec_m, 'dimuon_rec_m/D')
    t.Branch( 'dijet_m', dijet_m, 'dijet_m/D')
    t.Branch( 'dijet_rec_m', dijet_rec_m, 'dijet_rec_m/D')
    t.Branch( 'vis_ex_dimuon_m', vis_ex_dimuon_m, 'vis_ex_dimuon_m/D')
    t.Branch( 'vis_all_rec_m', vis_all_rec_m, 'vis_all_rec_m/D')
    t.Branch( 'vis_all_pt', vis_all_pt, 'vis_all_pt/D')
    t.Branch( 'vis_all_m', vis_all_m, 'vis_all_m/D')
    t.Branch( 'vis_all_p', vis_all_p, 'vis_all_p/D')
    t.Branch( 'vis_all_rec_m', vis_all_rec_m, 'vis_all_rec_m/D')
    t.Branch( 'npfo', npfo, 'npfo/D')
    t.Branch( 'jet_lead_e', jet_lead_e, 'jet_lead_e/D')
    t.Branch( 'jet_sub_e', jet_sub_e, 'jet_sub_e/D')
    t.Branch( 'angle_mj', angle_mj, 'angle_mj/D')

    t.Branch( 'vis_all_cos', vis_all_cos, 'vis_all_cos/D')
    t.Branch( 'cos', cos, 'cos/D')

    if combine_opt==1 :
        if ZZ_Selection==1 :
            h_evtflw.GetXaxis().SetBinLabel(1,'pre-selection')
            h_evtflw.GetXaxis().SetBinLabel(2,'is signal')
            h_evtflw.GetXaxis().SetBinLabel(3,'M(miss)>M(dijet)')
            h_evtflw.GetXaxis().SetBinLabel(4,'80GeV<M(dimuon)<100GeV')
            h_evtflw.GetXaxis().SetBinLabel(5,'120GeV<RecM(dimuon)<150GeV')
            h_evtflw.GetXaxis().SetBinLabel(6,'15<Npfo<70')
            h_evtflw.GetXaxis().SetBinLabel(7,'visible PT>10GeV')
            h_evtflw.GetXaxis().SetBinLabel(8,'Mininum angle>17.2')
            h_evtflw.GetXaxis().SetBinLabel(9,'M(miss)>80GeV, M(dijet)<35GeV')
            h_evtflw.GetXaxis().SetBinLabel(10,'JetE>5GeV,JetPt>3GeV')
            h_evtflw.GetXaxis().SetBinLabel(11,'RecM(dijet)<122GeV + 128GeV<RecM(dijet)')
            h_evtflw.GetXaxis().SetBinLabel(12,'vis_all_m<122GeV + 128GeV<vis_all_m')

        if ZZ_Selection==2 :
            h_evtflw.GetXaxis().SetBinLabel(1,'pre-selection')
            h_evtflw.GetXaxis().SetBinLabel(2,'is signal')
            h_evtflw.GetXaxis().SetBinLabel(3,'M(miss)<M(dijet)')
            h_evtflw.GetXaxis().SetBinLabel(4,'80GeV<M(dimuon)<100GeV')
            h_evtflw.GetXaxis().SetBinLabel(5,'120GeV<RecM(dimuon)<150GeV')
            h_evtflw.GetXaxis().SetBinLabel(6,'30<Npfo<100')
            h_evtflw.GetXaxis().SetBinLabel(7,'10GeV<visible PT<50GeV')
            h_evtflw.GetXaxis().SetBinLabel(8,'17.2<Mininum angle<90')
            h_evtflw.GetXaxis().SetBinLabel(9,'M(miss),M(dijet)')
            h_evtflw.GetXaxis().SetBinLabel(10,'JetE,JetPt,JetAngle')
            h_evtflw.GetXaxis().SetBinLabel(11,'RecM(dijet)<122GeV + 128GeV<RecM(dijet)')
            h_evtflw.GetXaxis().SetBinLabel(12,'vis_all_m<122GeV + 128GeV<vis_all_m')

    if combine_opt==2 :
        h_evtflw.GetXaxis().SetBinLabel(1,'pre-selection')
        h_evtflw.GetXaxis().SetBinLabel(2,'is signal')
        h_evtflw.GetXaxis().SetBinLabel(3,'Npfo > 9')
        h_evtflw.GetXaxis().SetBinLabel(4,'115Gev<Vis_Mass<135GeV')
        h_evtflw.GetXaxis().SetBinLabel(5,'|cos_theta|<0.9')
        h_evtflw.GetXaxis().SetBinLabel(6,'130GeV<RecM(dimuon)<220GeV')
        h_evtflw.GetXaxis().SetBinLabel(7,'43GeV<vis_all_p<60GeV')
        h_evtflw.GetXaxis().SetBinLabel(8,'10GeV<M(dijet)<100GeV')
        h_evtflw.GetXaxis().SetBinLabel(9,'10GeV<jet_lead_e<95GeV')
        h_evtflw.GetXaxis().SetBinLabel(10,'jet_sub_e')
        h_evtflw.GetXaxis().SetBinLabel(11,'angle_mj')
        h_evtflw.GetXaxis().SetBinLabel(12,'13GeV<M(dimuon)<100GeV')
        h_evtflw.GetXaxis().SetBinLabel(13,'vis_all_cos')
        h_evtflw.GetXaxis().SetBinLabel(14,'80GeV<RecM(vis_all)<107GeV')
        h_evtflw.GetXaxis().SetBinLabel(15,'RecM(dimuon)<122GeV + 128GeV<RecM(dimuon)')
        h_evtflw.GetXaxis().SetBinLabel(16,'RecM(dijet)<122GeV + 128GeV<RecM(dijet)')

    if combine_opt==3 :
        if ZZ_Selection==1:
            h_evtflw.GetXaxis().SetBinLabel(1,'pre-selection')
            h_evtflw.GetXaxis().SetBinLabel(2,'is signal')
            h_evtflw.GetXaxis().SetBinLabel(3,'M(missing)>M(dimuon)')
            h_evtflw.GetXaxis().SetBinLabel(4,'35<Npfo<107')
            h_evtflw.GetXaxis().SetBinLabel(5,'103Gev<Vis_Mass<179GeV')
            h_evtflw.GetXaxis().SetBinLabel(6,'-0.94<cos_theta<0.95')
            h_evtflw.GetXaxis().SetBinLabel(7,'155GeV<RecM(dimuon)<217GeV')
            h_evtflw.GetXaxis().SetBinLabel(8,'7GeV<vis_all_p<76GeV')
            h_evtflw.GetXaxis().SetBinLabel(9,'60GeV<M(dijet)<111GeV')
            h_evtflw.GetXaxis().SetBinLabel(10,'34GeV<jet_lead_e<88GeV')
            h_evtflw.GetXaxis().SetBinLabel(11,'13GeV<jet_sub_e<57GeV')
            h_evtflw.GetXaxis().SetBinLabel(12,'20<angle_mj<175')
            h_evtflw.GetXaxis().SetBinLabel(13,'8GeV<M(dimuon)<59GeV')
            h_evtflw.GetXaxis().SetBinLabel(14,'-0.84<vis_all_cos<0.86')
            h_evtflw.GetXaxis().SetBinLabel(15,'43GeV<RecM(vis_all)<125GeV')
            h_evtflw.GetXaxis().SetBinLabel(16,'10GeV<vis_all_pt<74GeV')
            h_evtflw.GetXaxis().SetBinLabel(17,'RecM(dimuon)<122GeV + 128GeV<RecM(dimuon)')
            h_evtflw.GetXaxis().SetBinLabel(18,'vis_all_m<122GeV + 128GeV<vis_all_m')

        if ZZ_Selection==2:
            h_evtflw.GetXaxis().SetBinLabel(1,'pre-selection')
            h_evtflw.GetXaxis().SetBinLabel(2,'is signal')
            h_evtflw.GetXaxis().SetBinLabel(3,'M(missing)<M(dimuon)')
            h_evtflw.GetXaxis().SetBinLabel(4,'29<Npfo<105')
            h_evtflw.GetXaxis().SetBinLabel(5,'164Gev<Vis_Mass<222GeV')
            h_evtflw.GetXaxis().SetBinLabel(6,'-0.94<cos_theta<0.95')
            h_evtflw.GetXaxis().SetBinLabel(7,'114GeV<RecM(dimuon)<161GeV')
            h_evtflw.GetXaxis().SetBinLabel(8,'4GeV<vis_all_p<62GeV')
            h_evtflw.GetXaxis().SetBinLabel(9,'69GeV<M(dijet)<110GeV')
            h_evtflw.GetXaxis().SetBinLabel(10,'44GeV<jet_lead_e<83GeV')
            h_evtflw.GetXaxis().SetBinLabel(11,'22GeV<jet_sub_e<58GeV')
            h_evtflw.GetXaxis().SetBinLabel(12,'95<angle_mj<171')
            h_evtflw.GetXaxis().SetBinLabel(13,'57GeV<M(dimuon)<95GeV')
            h_evtflw.GetXaxis().SetBinLabel(14,'-0.84<vis_all_cos<0.86')
            h_evtflw.GetXaxis().SetBinLabel(15,'15GeV<RecM(vis_all)<61GeV')
            h_evtflw.GetXaxis().SetBinLabel(16,'8GeV<vis_all_pt<48GeV')
            h_evtflw.GetXaxis().SetBinLabel(17,'RecM(dimuon)<122GeV + 128GeV<RecM(dimuon)')
            h_evtflw.GetXaxis().SetBinLabel(18,'vis_all_m<122GeV + 128GeV<vis_all_m')

    for jentry in xrange(entries):
        pbar.update(jentry+1)
        # get the next tree in the chain and verify
        ientry = t_in.LoadTree(jentry)
        if ientry < 0:
            break
        # copy next entry into memory and verify
		
        if TEST and ientry > 10000:
            break
		
        nb = t_in.GetEntry(jentry)
        if nb<=0:
            continue
		
        # raw event number
        h_evtflw.Fill(0)

        if is_sel(t_in,flag,combine_opt):
            
            fill_histograms(t_in,flag,combine_opt)

            if select_higgs_to_zz(t_in,combine_opt):
                index=0
                h_m_dimuon_final.Fill( t_in.dimuon_m[index] )
                h_mrec_dimuon_final.Fill( t_in.dimuon_rec_m[index] )
                h_m_dijet_final.Fill( t_in.dijet_m[0] )
                h_mrec_dijet_final.Fill( t_in.dijet_rec_m[0] )
                h_m_visible_final.Fill( t_in.vis_ex_dimuon_m )
                h_m_missing_final.Fill( t_in.vis_all_rec_m )
                h_vis_all_pt_final.Fill( t_in.vis_all_pt )
                h_vis_all_m_final.Fill( t_in.vis_all_m )
                h_vis_all_p_final.Fill( t_in.vis_all_p )
                h_vis_all_rec_m_final.Fill( t_in.vis_all_rec_m )
                h_vis_all_cos_final.Fill( t_in.vis_all_cos )
                h_cos_final.Fill( t_in.cos )
                h_npfo_final.Fill( t_in.n_col_reco )
                h_jet_lead_e_final.Fill( t_in.jet_lead_e[0] )
                h_jet_sub_e_final.Fill( t_in.jet_sub_e[0] )
                h_angle_mj_final.Fill( t_in.lj_angle )
                h_2D_visible_missing_final.Fill( t_in.vis_ex_dimuon_m, t_in.vis_all_rec_m )
                h_2D_dijet_missing_final.Fill( t_in.dijet_m[0], t_in.vis_all_rec_m )

                # h_m_lljj.Fill( t_in.lljj_m )

                h_y12.Fill( t_in.y12 )
                h_y23.Fill( t_in.y23 )
                h_y34.Fill( t_in.y34 )

                h_m_mc_zz_flag.Fill( t_in.mc_zz_flag )

                save_pid( t_in )

                dimuon_m[0] = t_in.dimuon_m[index]
                dimuon_rec_m[0] = t_in.dimuon_rec_m[index]
                dijet_m[0] = t_in.dijet_m[0]
                dijet_rec_m[0] = t_in.dijet_rec_m[0]
                vis_ex_dimuon_m[0] = t_in.vis_ex_dimuon_m
                vis_all_rec_m[0] = t_in.vis_all_rec_m
                vis_all_pt[0] = t_in.vis_all_pt
                vis_all_m[0] = t_in.vis_all_m
                vis_all_p[0] = t_in.vis_all_p
                vis_all_rec_m[0] = t_in.vis_all_rec_m
                vis_all_cos[0] = t_in.vis_all_cos
                cos[0] = t_in.cos
                npfo[0] = t_in.n_col_reco
                jet_lead_e[0] = t_in.jet_lead_e[0]
                jet_sub_e[0] = t_in.jet_sub_e[0]
                angle_mj[0] = t_in.lj_angle
                t.Fill()

    fout.Write()
            
    # Get event flow histogram @ Higgs2zz.cc
    copy_histo(fin, 'hevtflw', h_evtflw_pre) 
 
    # Writ histograms & Close file
    write_histograms()

    fout.Close()

    if entries > 0 :
        pbar.finish()
	
    dur = duration(time()-time_start)
    sys.stdout.write(' \nDone in %s. \n' % dur)


def is_signal(t,combine_opt):

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
        flag = MuonMinus * MuonPlus * hig
    if ( combine_opt==2 ):
        flag = NeutrinoMinus * NeutrinoPlus * hig
    if ( combine_opt==3 ):
        flag = QuarkMinus * QuarkPlus * hig

    return flag
    
def is_sel(t,num,combine_opt):

    sel = 0

    # Signal
    if( num==1 and is_signal(t,combine_opt) ):
        sel = 1
    # not Signal 
    if( num==2 and not( is_signal(t,combine_opt) ) ):
        sel = 1
    #all
    if( num==0 ):
        sel = 1

    return sel

def copy_histo(f, hname, h_copy):
    
    h_in = f.Get(hname)
    for i in range(1, 10):
        c1 = h_in.GetBinContent(i)
        t1 = h_in.GetXaxis().GetBinLabel(i)
        h_copy.SetBinContent(i, c1)
        h_copy.GetXaxis().SetBinLabel(i,t1)


def save_pid(t):

    # Initial Parton PID
    n_initial_parton = t.mc_init_pdgid.size()
    for i in xrange(n_initial_parton):
        h_mc_init_plist.Fill( t.mc_init_pdgid[i] )

    # Higgs Daughter PID
    n_higgs_daughter = t.mc_higgs_daughter_pdgid.size()
    for i in xrange(n_higgs_daughter):
        h_mc_higgs_dlist.Fill( t.mc_higgs_daughter_pdgid[i] )    


def fill_histograms(t,num,combine_opt):

    index = 0
    if (is_sel(t,num,combine_opt) ):
        # Distribution after pre-selectioon ( muon_p>=1, muon_m>=1, njet=2 ) 
        h_m_dimuon_raw.Fill( t.dimuon_m[index] )
        h_mrec_dimuon_raw.Fill( t.dimuon_rec_m[index] )
        h_m_dijet_raw.Fill( t.dijet_m[0] )
        h_mrec_dijet_raw.Fill( t.dijet_rec_m[0] )
        h_m_visible_raw.Fill( t.vis_ex_dimuon_m )
        h_m_missing_raw.Fill( t.vis_all_rec_m )
        h_vis_all_pt_raw.Fill( t.vis_all_pt )
        h_vis_all_m_raw.Fill( t.vis_all_m )
        h_vis_all_p_raw.Fill( t.vis_all_p)
        h_vis_all_rec_m_raw.Fill( t.vis_all_rec_m )
        h_vis_all_cos_raw.Fill( t.vis_all_cos )
        h_cos_raw.Fill( t.cos )
        h_npfo_raw.Fill( t.n_col_reco )
        h_jet_lead_e_raw.Fill( t.jet_lead_e[0] )
        h_jet_sub_e_raw.Fill( t.jet_sub_e[0] )
        h_angle_mj_raw.Fill( t.lj_angle )
        h_2D_visible_missing_raw.Fill( t.vis_ex_dimuon_m, t.vis_all_rec_m )
        h_2D_dijet_missing_raw.Fill( t.dijet_m[0], t.vis_all_rec_m )

def write_histograms():
	
## Event Flow
    h_evtflw.Write()
    h_evtflw_pre.Write()

## After Pre-Selection 
    h_m_dimuon_raw.Write()
    h_mrec_dimuon_raw.Write()
    h_m_dijet_raw.Write()
    h_mrec_dijet_raw.Write()
    h_m_visible_raw.Write()
    h_m_missing_raw.Write()
    h_vis_all_pt_raw.Write()
    h_vis_all_m_raw.Write()
    h_vis_all_p_raw.Write()
    h_vis_all_rec_m_raw.Write()
    h_vis_all_cos_raw.Write()
    h_cos_raw.Write()
    h_npfo_raw.Write()
    h_jet_lead_e_raw.Write()
    h_jet_sub_e_raw.Write()
    h_angle_mj_raw.Write()
    h_2D_visible_missing_raw.Write()
    h_2D_dijet_missing_raw.Write()

# After All of Cuts
    h_m_dimuon_final.Write()
    h_mrec_dimuon_final.Write()
    h_m_dijet_final.Write()
    h_mrec_dijet_final.Write()
    h_m_visible_final.Write()
    h_m_missing_final.Write()
    h_vis_all_pt_final.Write()
    h_vis_all_m_final.Write()
    h_vis_all_p_final.Write()
    h_vis_all_rec_m_final.Write()
    h_vis_all_cos_final.Write()
    h_cos_final.Write()
    h_npfo_final.Write()
    h_jet_lead_e_final.Write()
    h_jet_sub_e_final.Write()
    h_angle_mj_final.Write()
    h_2D_visible_missing_final.Write()
    h_2D_dijet_missing_final.Write()

    h_m_lljj.Write()

    h_y12.Write()
    h_y23.Write()
    h_y34.Write()

    h_mc_init_plist.Write()
    h_mc_higgs_dlist.Write()

    h_m_mc_zz_flag.Write()

def select_higgs_to_zz(t,combine_opt):
    
    h_evtflw.Fill(1)

    if ( combine_opt == 1 ):
        index = select_zpole_muon(t)

        # Select ZZ*->nunu,jj ( Z->nunu, Z*->jj ) events : Mass(missing) > Mass(dijet)
        if ( ZZ_Selection == 1 ):
            if not ( t.vis_all_rec_m > t.dijet_m[0] ):
                return False
        if ( ZZ_Selection == 2 ):
            if not ( t.vis_all_rec_m < t.dijet_m[0] ):
                return False
        h_evtflw.Fill(2)
    
        if not ( t.dimuon_m[index] > 80.0 and t.dimuon_m[index] < 100.0 ):
            return False
        h_evtflw.Fill(3)

        if not ( t.dimuon_rec_m[index] > 120.0 and t.dimuon_rec_m[index] < 142.0 ):
            return False
        h_evtflw.Fill(4)
    
        if ( ZZ_Selection == 1 ):
            if not ( t.n_col_reco > 20 and t.n_col_reco < 67 ):
                return False
        if ( ZZ_Selection == 2 ):
            if not ( t.n_col_reco > 30 and t.n_col_reco < 100 ):
                return False
        h_evtflw.Fill(5)
    
        if ( ZZ_Selection == 1 ):
            if not ( t.vis_all_pt > 10 ):
                return False
        if ( ZZ_Selection == 2 ):
            if not ( t.vis_all_pt > 12 and t.vis_all_pt < 50 ):
                return False
        h_evtflw.Fill(6)
    
        if ( ZZ_Selection == 1 ):
            if not ( t.lj_minangle > 17.2  ):
                return False
        if ( ZZ_Selection == 2 ):
            if not ( t.lj_minangle > 17.2 and t.lj_minangle < 90 ):
                return False
        h_evtflw.Fill(7)
    
        if ( ZZ_Selection == 1 ):
            if not ( t.vis_all_rec_m > 80 and t.vis_all_rec_m < 105 and t.dijet_m[0] > 10 and t.dijet_m[0] < 43 ):
                return False
        if ( ZZ_Selection == 2 ):
            if not ( 4 < t.vis_all_rec_m and t.vis_all_rec_m < 59 and 58 < t.dijet_m[0] and t.dijet_m[0] < 100 and 12 * t.dijet_m[0] + 7 * t.vis_all_rec_m > 1160 ): 
                return False
        h_evtflw.Fill(8)
        
        if ( ZZ_Selection == 1 ):
            if not ( t.jet_pt[0] > 3.0 and t.jet_pt[1] > 3.0 and t.jet_e[0] > 5.0  and t.jet_e[1] > 5.0 ):
                return False
        if ( ZZ_Selection == 2 ):
            if not ( t.jet_pt[0] > 10 and t.jet_pt[0] < 65 and t.jet_pt[1] > 10 and t.jet_pt[1] < 65 and t.jet_e[0] > 20 and t.jet_e[0] <80 and t.jet_e[1] > 20 and t.jet_e[1] < 80 and t.jet_theta[0] > 10 and  t.jet_theta[0] < 170 and t.jet_theta[1] >10 and  t.jet_theta[1] < 170 ):
                return False
        h_evtflw.Fill(9)

        if ( 122 < t.dijet_rec_m[index] and t.dijet_rec_m[index] < 128 ):
            return False
        h_evtflw.Fill(10)

        if ( 122 < t.vis_all_m and t.vis_all_m < 128 ):
            return False
        h_evtflw.Fill(11)

    if ( combine_opt == 2 ):
        index=0
        if not ( 20 < t.n_col_reco and t.n_col_reco < 73 ):
            return False
        h_evtflw.Fill(2)

        if not ( 115 < t.vis_all_m and t.vis_all_m < 135 ):
            return False
        h_evtflw.Fill(3)

        if not ( -0.9 < t.cos and t.cos < 0.9 ):
            return False
        h_evtflw.Fill(4)

        if not ( (104 < t.dimuon_rec_m[index] and t.dimuon_rec_m[index] < 162) or (190 < t.dimuon_rec_m[index] and t.dimuon_rec_m[index] < 214) ):
            return False
        h_evtflw.Fill(5)

        if not ( 43 < t.vis_all_p and t.vis_all_p < 60 ):
            return False
        h_evtflw.Fill(6)

        if not ( (14 < t.dijet_m[0] and t.dijet_m[0] < 55) or (81 < t.dijet_m[0] and t.dijet_m[0] < 99) ):
            return False
        h_evtflw.Fill(7)

        if not ( 14 < t.jet_lead_e[0] and t.jet_lead_e[0] < 69 ):
            return False
        h_evtflw.Fill(8)

        if not (3 < t.jet_sub_e[0] and t.jet_sub_e[0] < 49 ):
            return False
        h_evtflw.Fill(9)

        if not (t.lj_angle < 142):
            return False
        h_evtflw.Fill(10)

        if not ( 14 < t.dimuon_m[index] and t.dimuon_m[index] < 94 ):
            return False
        h_evtflw.Fill(11)

        if not ( -0.9 < t.vis_all_cos and t.vis_all_cos < 0.9 ):
            return False
        h_evtflw.Fill(12)

        if not ( 78 < t.vis_all_rec_m and t.vis_all_rec_m < 100 ):
            return False
        h_evtflw.Fill(13)

        if ( 122 < t.dimuon_rec_m[index] and t.dimuon_rec_m[index] < 128 ):
            return False
        h_evtflw.Fill(14)

        if ( 122 < t.dijet_rec_m[index] and t.dijet_rec_m[index] < 128 ):
            return False
        h_evtflw.Fill(15)

    if ( combine_opt == 3 ):
        if (ZZ_Selection==1):
            index=0

            if not ( t.dimuon_m[index] < t.vis_all_rec_m):
                return False
            h_evtflw.Fill(2)

            if not ( 35 < t.n_col_reco and t.n_col_reco < 107 ):
                return False
            h_evtflw.Fill(3)
 
            if not ( 114 < t.vis_all_m and t.vis_all_m < 154 ):
                return False
            h_evtflw.Fill(4)

            if not ( -0.94 < t.cos and t.cos < 0.95 ):
                return False
            h_evtflw.Fill(5)

            if not ( 193 < t.dimuon_rec_m[index] and t.dimuon_rec_m[index] < 212):
                return False
            h_evtflw.Fill(6)

            if not ( 16 < t.vis_all_p and t.vis_all_p < 72 ):
                return False
            h_evtflw.Fill(7)

            if not ( 76 < t.dijet_m[0] and t.dijet_m[0] < 104 ):
                return False
            h_evtflw.Fill(8)

            if not ( 47 < t.jet_lead_e[0] and t.jet_lead_e[0] < 83 ):
                return False
            h_evtflw.Fill(9)

            if not ( 23 < t.jet_sub_e[0] and t.jet_sub_e[0] < 55 ):
                return False
            h_evtflw.Fill(10)

            if not ( 20 < t.lj_angle and t.lj_angle < 175):
                return False
            h_evtflw.Fill(11)
 
            if not ( 12 < t.dimuon_m[index] and t.dimuon_m[index] < 43 ):
                return False
            h_evtflw.Fill(12)

            if not ( -0.84 < t.vis_all_cos and t.vis_all_cos < 0.86 ):
                return False
            h_evtflw.Fill(13)

            if not ( 69 < t.vis_all_rec_m and t.vis_all_rec_m < 111 ):
                return False
            h_evtflw.Fill(14)

            if not ( 10 < t.vis_all_pt and t.vis_all_pt < 71):
                return False
            h_evtflw.Fill(15)
 
            if ( 122 < t.dimuon_rec_m[index] and t.dimuon_rec_m[index] < 128 ):
                return False
            h_evtflw.Fill(16)

            if ( 122 < t.vis_all_m and t.vis_all_m < 128 ):
                return False
            h_evtflw.Fill(17)

        if (ZZ_Selection==2):
            index=0

            if not ( t.dimuon_m[index] > t.vis_all_rec_m):
                return False
            h_evtflw.Fill(2)

            if not ( 35 < t.n_col_reco and t.n_col_reco < 105 ):
                return False
            h_evtflw.Fill(3)

            if not ( 179 < t.vis_all_m and t.vis_all_m < 214 ):
                return False
            h_evtflw.Fill(4)

            if not ( -0.94 < t.cos and t.cos < 0.95 ):
                return False
            h_evtflw.Fill(5)

            if not ( 130 < t.dimuon_rec_m[index] and t.dimuon_rec_m[index] < 157):
                return False
            h_evtflw.Fill(6)

            if not ( 8 < t.vis_all_p and t.vis_all_p < 45 ):
                return False
            h_evtflw.Fill(7)

            if not ( 76 < t.dijet_m[0] and t.dijet_m[0] < 104 ):
                return False
            h_evtflw.Fill(8)

            if not ( 49 < t.jet_lead_e[0] and t.jet_lead_e[0] < 82 ):
                return False
            h_evtflw.Fill(9)

            if not ( 22 < t.jet_sub_e[0] and t.jet_sub_e[0] < 56 ):
                return False
            h_evtflw.Fill(10)

            if not ( 118 < t.lj_angle and t.lj_angle < 177):
                return False
            h_evtflw.Fill(11)

            if not ( 77 < t.dimuon_m[index] and t.dimuon_m[index] < 95 ):
                return False
            h_evtflw.Fill(12)

            if not ( -0.84 < t.vis_all_cos and t.vis_all_cos < 0.86 ):
                return False
            h_evtflw.Fill(13)

            if not ( 7 < t.vis_all_rec_m and t.vis_all_rec_m < 56 ):
                return False
            h_evtflw.Fill(14)

            if not ( 8 < t.vis_all_pt and t.vis_all_pt < 45):
                return False
            h_evtflw.Fill(15)

            if ( 122 < t.dimuon_rec_m[index] and t.dimuon_rec_m[index] < 128 ):
                return False
            h_evtflw.Fill(16)

            if ( 122 < t.vis_all_m and t.vis_all_m < 128 ):
                return False
            h_evtflw.Fill(17)

    return True

def select_zpole_muon(t):

    nentry = t.n_muon_plus * t.n_muon_minus
    min_diff = 1000.0
    for i in range(nentry):
       if ( abs( t.dimuon_m[i] - Z_MASS ) < min_diff ):
           min_diff = abs( t.dimuon_m[i] - Z_MASS )
           index = i

    return index

if __name__ == '__main__':
	main()
