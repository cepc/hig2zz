#!/usr/bin/env python
"""
Event Selection

## Inspired from an event selection script for J/psi->invisible
"""

__author__ = "Min Zhong <zmind@mail.ustc.edu.cn>"
__copyright__ = "Copyright (c) Min Zhong"
__created__ = "[2019-08-01 ]" 

import sys
import os
import math
import ROOT
from progressbar import Bar, Percentage, ProgressBar
from array import array
from time import time
from tools import duration, check_outfile_path

## Before BDT 
h_dimuon_rec_m_raw = ROOT.TH1D('h_dimuon_rec_m_raw', 'dimuon_rec_m_raw', 250, 0, 250)
h_dijet_rec_m_raw = ROOT.TH1D('h_dijet_rec_m_raw', 'dijet_rec_m_raw', 250, 0, 250)
h_vis_all_rec_m_raw = ROOT.TH1D('h_vis_all_rec_m_raw', 'vis_all_rec_m_raw', 250, -50, 200)
h_vis_all_p_raw = ROOT.TH1D('h_vis_all_p_raw', 'vis_all_p_raw', 250, 0, 250)
h_vis_all_pt_raw = ROOT.TH1D('h_vis_all_pt_raw', 'vis_all_pt_raw', 250, 0, 250)
h_vis_all_m_raw = ROOT.TH1D('h_vis_all_m_raw', 'vis_all_m_raw', 250, 0, 250)
h_dimuon_m_raw = ROOT.TH1D('h_dimuon_m_raw', 'dimuon_m_raw', 250, 0, 250)
h_dijet_m_raw =  ROOT.TH1D('h_dijet_m_raw', 'dijet_m_raw', 250, 0, 250)
h_jet_lead_e_raw = ROOT.TH1D('h_jet_lead_e_raw', 'jet_lead_e_raw', 250, 0, 250)
h_jet_lead_pt_raw = ROOT.TH1D('h_jet_lead_pt_raw', 'jet_lead_pt_raw', 250, 0, 250)
h_jet_sub_e_raw = ROOT.TH1D('h_jet_sub_e_raw', 'jet_sub_e_raw', 250, 0, 250)
h_jet_sub_pt_raw = ROOT.TH1D('h_jet_sub_pt_raw', 'jet_sub_pt_raw', 250, 0, 250)
h_dimuon_dijet_angle_raw = ROOT.TH1D('h_dimuon_dijet_angle_raw', 'dimuon_dijet_angle_raw', 200, 0, 200)
h_n_col_reco_raw = ROOT.TH1D('h_n_col_reco_raw', 'n_col_reco_raw', 160, 0, 160)
h_cos_raw = ROOT.TH1D('h_cos_raw', 'cos_raw', 100, -1, 1)
h_vis_all_cos_raw = ROOT.TH1D('h_vis_all_cos_raw', 'cos_raw', 100, -1, 1)
h_BDT_score_raw = ROOT.TH1D('h_BDT_score_raw', 'BDT_score_raw', 400, -2, 2)

## After BDT
h_dimuon_rec_m_final = ROOT.TH1D('h_dimuon_rec_m_final', 'dimuon_rec_m_final', 250, 0, 250)
h_dijet_rec_m_final = ROOT.TH1D('h_dijet_rec_m_final', 'dijet_rec_m_final', 250, 0, 250)
h_vis_all_rec_m_final = ROOT.TH1D('h_vis_all_rec_m_final', 'vis_all_rec_m_final', 250, -50, 200)
h_vis_all_p_final = ROOT.TH1D('h_vis_all_p_final', 'vis_all_p_final', 250, 0, 250)
h_vis_all_pt_final = ROOT.TH1D('h_vis_all_pt_final', 'vis_all_pt_final', 250, 0, 250)
h_vis_all_m_final = ROOT.TH1D('h_vis_all_m_final', 'vis_all_m_final', 250, 0, 250)
h_dimuon_m_final = ROOT.TH1D('h_dimuon_m_final', 'dimuon_m_final', 250, 0, 250)
h_dijet_m_final =  ROOT.TH1D('h_dijet_m_final', 'dijet_m_final', 250, 0, 250)
h_jet_lead_e_final = ROOT.TH1D('h_jet_lead_e_final', 'jet_lead_e_final', 250, 0, 250)
h_jet_lead_pt_final = ROOT.TH1D('h_jet_lead_pt_final', 'jet_lead_pt_final', 250, 0, 250)
h_jet_sub_e_final = ROOT.TH1D('h_jet_sub_e_final', 'jet_sub_e_final', 250, 0, 250)
h_jet_sub_pt_final = ROOT.TH1D('h_jet_sub_pt_final', 'jet_sub_pt_final', 250, 0, 250)
h_dimuon_dijet_angle_final = ROOT.TH1D('h_dimuon_dijet_angle_final', 'dimuon_dijet_angle_final', 200, 0, 200)
h_n_col_reco_final = ROOT.TH1D('h_n_col_reco_final', 'n_col_reco_final', 160, 0, 160)
h_cos_final = ROOT.TH1D('h_cos_final', 'cos_final', 100, -1, 1)
h_vis_all_cos_final = ROOT.TH1D('h_vis_all_cos_final', 'cos_final', 100, -1, 1)
h_BDT_score_final = ROOT.TH1D('h_BDT_score_final', 'BDT_score_final', 400, -2, 2)

def usage():
    sys.stdout.write('''
NAME
    sel_events.py 

SYNOPSIS

    ./sel_events.py infile evtflw_infile outfile combine_opt (1: llhzz, 2: nnhzz, 3: qqhzz) flag_zz (1: vv jj/ll, 2: jj/ll vv)

AUTHOR 
    Min Zhong <zmind@mail.ustc.edu.cn>

DATE
    August 2019
\n''')


def main():

    args = sys.argv[1:]
    if len(args)<5:
        return usage()

    infile  = args[0]
    evtflow_file = args[1]
    outfile = args[2]
    combine_opt = int(args[3])
    flag_zz = int(args[4])

    ## Event Flow
    h_evtflw = ROOT.TH1D('hevtflw_sel','eventflow',10,0,10)
    if (combine_opt==1):
	last_bin=9
    if (combine_opt==2):
	last_bin=9
    if (combine_opt==3):
	last_bin=9

    h_evtflw.GetXaxis().SetBinLabel(last_bin,'BDT score')

    fin = ROOT.TFile(infile)
    t_in = fin.Get('tree')
    entries = t_in.GetEntriesFast()

    if entries > 0 :
       pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=entries).start()

    time_start = time()

    # Get event flow histogram @BDT_pre.python
    evtflow_fin = ROOT.TFile(evtflow_file)
    copy_histo(evtflow_fin, 'h_evtflw_beforeBDT', h_evtflw, combine_opt)          

    # output file
    fout = ROOT.TFile(outfile, "RECREATE")
    t = ROOT.TTree( 'Higgs Tree', 'Higgs Tree' )

    dimuon_m =  array( 'd', [0] )
    dijet_m =  array( 'd', [0] )
    vis_all_rec_m =  array( 'd', [0] )
    n_col_reco =  array( 'i', [0] )
    cos =  array( 'd', [0] )
    vis_all_cos =  array( 'd', [0] )
    dimuon_dijet_angle =  array( 'd', [0] )
    dimuon_rec_m =  array( 'd', [0] )
    dijet_rec_m = array( 'd', [0] )
    vis_all_m =  array( 'd', [0] )
    vis_all_p =  array( 'd', [0] )
    vis_all_pt = array( 'd', [0] )
    jet_lead_e =  array( 'd', [0] )
    jet_lead_pt =  array( 'd', [0] )
    jet_sub_e =  array( 'd', [0] )
    jet_sub_pt =  array( 'd', [0] )
    BDT_score = array( 'd', [0] )

    t.Branch( 'dimuon_m', dimuon_m, 'dimuon_m/D')
    t.Branch( 'dijet_m', dijet_m, 'dijet_m/D')
    t.Branch( 'vis_all_rec_m', vis_all_rec_m, 'vis_all_rec_m/D')
    t.Branch( 'n_col_reco', n_col_reco, 'n_col_reco/I')
    t.Branch( 'cos', cos, 'cos/D')
    t.Branch( 'vis_all_cos', vis_all_cos, 'vis_all_cos/D')
    t.Branch( 'dimuon_dijet_angle', dimuon_dijet_angle, 'dimuon_dijet_angle/D')
    t.Branch( 'dimuon_rec_m', dimuon_rec_m, 'dimuon_rec_m/D')
    t.Branch( 'dijet_rec_m', dijet_rec_m, 'dijet_rec_m/D')
    t.Branch( 'vis_all_m', vis_all_m, 'vis_all_m/D')
    t.Branch( 'vis_all_p', vis_all_p, 'vis_all_p/D')
    t.Branch( 'vis_all_pt', vis_all_pt, 'vis_all_pt/D')
    t.Branch( 'jet_lead_e', jet_lead_e, 'jet_lead_e/D')
    t.Branch( 'jet_lead_pt', jet_lead_pt, 'jet_lead_pt/D')
    t.Branch( 'jet_sub_e', jet_sub_e, 'jet_sub_e/D')
    t.Branch( 'jet_sub_pt', jet_sub_pt, 'jet_sub_pt/D')
    t.Branch( 'BDT_score', BDT_score, 'BDT_score/D')

    # read trees
    for jentry in xrange(entries):
        pbar.update(jentry+1)
        # get the next tree in the chain and verify
        ientry = t_in.LoadTree(jentry)
        if ientry < 0:
            break
        # copy next entry into memory and verify
		
        nb = t_in.GetEntry(jentry)
        if nb<=0:
            continue

        h_dimuon_rec_m_raw.Fill(t_in.dimuon_rec_m)
	h_dijet_rec_m_raw.Fill(t_in.dijet_rec_m)
        h_vis_all_p_raw.Fill(t_in.vis_all_p)
        h_vis_all_pt_raw.Fill(t_in.vis_all_pt)
        h_vis_all_m_raw.Fill(t_in.vis_all_m)
        h_dimuon_m_raw.Fill(t_in.dimuon_m)
        h_dijet_m_raw.Fill(t_in.dijet_m)
        h_vis_all_rec_m_raw.Fill(t_in.vis_all_rec_m)
        h_jet_lead_e_raw.Fill(t_in.jet_lead_e)
        h_jet_lead_pt_raw.Fill(t_in.jet_lead_pt)
        h_jet_sub_e_raw.Fill(t_in.jet_sub_e)
        h_jet_sub_pt_raw.Fill(t_in.jet_sub_pt)
        h_dimuon_dijet_angle_raw.Fill(t_in.dimuon_dijet_angle)
        h_n_col_reco_raw.Fill(t_in.n_col_reco)
        h_cos_raw.Fill(t_in.cos)
	h_vis_all_cos_raw.Fill(t_in.vis_all_cos)
        h_BDT_score_raw.Fill(t_in.BDT_score)

	if (combine_opt==1):
	    if (flag_zz==1):
		Cut_BDT_score = (t_in.BDT_score > 0.15)
	    if (flag_zz==2):
		Cut_BDT_score = (t_in.BDT_score > 0.03)
	if (combine_opt==2):
            if (flag_zz==1):
                Cut_BDT_score = (t_in.BDT_score > -0.01)
            if (flag_zz==2):
                Cut_BDT_score = (t_in.BDT_score > 0.00)
	if (combine_opt==3):
	    if (flag_zz==1):
                Cut_BDT_score = (t_in.BDT_score > -0.05)
            if (flag_zz==2):
                Cut_BDT_score = (t_in.BDT_score > -0.02)

	if (Cut_BDT_score):
            h_dimuon_rec_m_final.Fill(t_in.dimuon_rec_m)
            h_dijet_rec_m_final.Fill(t_in.dijet_rec_m)
            h_vis_all_p_final.Fill(t_in.vis_all_p)
            h_vis_all_pt_final.Fill(t_in.vis_all_pt)
            h_vis_all_m_final.Fill(t_in.vis_all_m)
            h_dimuon_m_final.Fill(t_in.dimuon_m)
            h_dijet_m_final.Fill(t_in.dijet_m)
            h_vis_all_rec_m_final.Fill(t_in.vis_all_rec_m)
            h_jet_lead_e_final.Fill(t_in.jet_lead_e)
            h_jet_lead_pt_final.Fill(t_in.jet_lead_pt)
            h_jet_sub_e_final.Fill(t_in.jet_sub_e)
            h_jet_sub_pt_final.Fill(t_in.jet_sub_pt)
            h_dimuon_dijet_angle_final.Fill(t_in.dimuon_dijet_angle)
            h_n_col_reco_final.Fill(t_in.n_col_reco)
            h_cos_final.Fill(t_in.cos)
            h_vis_all_cos_final.Fill(t_in.vis_all_cos)
            h_BDT_score_final.Fill(t_in.BDT_score)

            dimuon_m[0] =  t_in.dimuon_m
            dijet_m[0] = t_in.dijet_m
            vis_all_rec_m[0] = t_in.vis_all_rec_m
            n_col_reco[0] = t_in.n_col_reco
            cos[0] = t_in.cos
            vis_all_cos[0] = t_in.vis_all_cos
            dimuon_dijet_angle[0] = t_in.dimuon_dijet_angle
            dimuon_rec_m[0] =  t_in.dimuon_rec_m
            dijet_rec_m[0] = t_in.dijet_rec_m
            vis_all_m[0] = t_in.vis_all_m
            vis_all_p[0] = t_in.vis_all_p
            vis_all_pt[0] = t_in.vis_all_pt
            jet_lead_e[0] = t_in.jet_lead_e
            jet_lead_pt[0] = t_in.jet_lead_pt
            jet_sub_e[0] =  t_in.jet_sub_e
            jet_sub_pt[0] = t_in.jet_sub_pt
	    BDT_score[0] = t_in.BDT_score

	    t.Fill()

            # Fill event flow
	    if (combine_opt==1):
	        h_evtflw.Fill(8)
	    if (combine_opt==2):
		h_evtflw.Fill(8)
	    if (combine_opt==3):
		h_evtflw.Fill(8)

    fout.Write()
    h_evtflw.Write()

    h_dimuon_rec_m_raw.Write()
    h_dijet_rec_m_raw.Write()
    h_vis_all_p_raw.Write()
    h_vis_all_pt_raw.Write()
    h_vis_all_m_raw.Write()
    h_dimuon_m_raw.Write()
    h_dijet_m_raw.Write()
    h_vis_all_rec_m_raw.Write()
    h_jet_lead_e_raw.Write()
    h_jet_lead_pt_raw.Write()
    h_jet_sub_e_raw.Write()
    h_jet_sub_pt_raw.Write()
    h_dimuon_dijet_angle_raw.Write()
    h_n_col_reco_raw.Write()
    h_cos_raw.Write()
    h_vis_all_cos_raw.Write()
    h_BDT_score_raw.Write()
    
    h_dimuon_rec_m_final.Write()
    h_dijet_rec_m_final.Write()
    h_vis_all_p_final.Write()
    h_vis_all_pt_final.Write()
    h_vis_all_m_final.Write()
    h_dimuon_m_final.Write()
    h_dijet_m_final.Write()
    h_vis_all_rec_m_final.Write()
    h_jet_lead_e_final.Write()
    h_jet_lead_pt_final.Write()
    h_jet_sub_e_final.Write()
    h_jet_sub_pt_final.Write()
    h_dimuon_dijet_angle_final.Write()
    h_n_col_reco_final.Write()
    h_cos_final.Write()
    h_vis_all_cos_final.Write()
    h_BDT_score_final.Write()

    # Writ histograms & Close file
    fout.Close()

    if entries > 0 :
        pbar.finish()
	
    dur = duration(time()-time_start)
    sys.stdout.write(' \nDone in %s. \n' % dur)
#    sys.stdout.write(' \nDone \n' )


def copy_histo(f, hname, h_copy, combine_opt):
    
    h_in = f.Get(hname)
    if (combine_opt==1):
        bin_max=9
    if (combine_opt==2):
	bin_max=9
    if (combine_opt==3):
	bin_max=9

    for i in range(1, bin_max):
        c1 = h_in.GetBinContent(i)
        t1 = h_in.GetXaxis().GetBinLabel(i)
        h_copy.SetBinContent(i, c1)
        h_copy.GetXaxis().SetBinLabel(i,t1)


if __name__ == '__main__':
	main()
