#!/usr/bin/env python
"""
Save results as root files
"""

__author__ = "Kong Lingteng <konglingteng15@mails.ucas.ac.cn>"
__copyright__ = "Copyright (c) Kong Lingteng"
__created__ = "[2019-02-26 Feb 10:49]" 

import sys
import os
import math
import ROOT
from array import array
from tools import check_outfile_path

def main():

    #signal
    s_in = './run/llh2zz/hist/ana_File_merged_1.root'
    s_out = './root/sig_e2e2hvvjj.root'

    signal_sample =  ROOT.TFile(s_in)
    evah = signal_sample.Get('hevtflw_sel')
    eva = evah.GetBinContent(3)  #number of e2e2hvvjj
    s = 5600 * 6.77 * 0.0264 * 0.2 * 0.69 / eva

    save_root(s_in, s_out, s)

    #background
    tabs = sys.argv[1:]

    for t in tabs: 

        tab = open(t , 'r' )

        for s_line in tab :
            
            if not s_line.startswith('#'):
                l = [x.strip() for x in s_line.split(',')]
                dname = l[0]
                event_exp = 1.11 * float(l[3])
                b_in = './run/bg/hist/' + dname + '/ana_File_merged_1.root'
                sample = ROOT.TFile(b_in)
                h=sample.Get('hevtflw_pre')
                event_ana = h.GetBinContent(1)

                if event_ana != 0:
                    s = (event_exp / event_ana)

                    tep=sample.Get('hevtflw_sel')
                    if tep.GetBinContent(11) != 0:

                        b_out = './root/bkg_%s.root'%dname
                        save_root(b_in, b_out, s)

def save_root(f_in, f_out, s):

    check_outfile_path(f_out)
    
    fin = ROOT.TFile(f_in)
    fout = ROOT.TFile(f_out, "RECREATE")

    t_in = fin.Get('Higgs Tree')
    entries = t_in.GetEntriesFast()

    dimuon_m = array( 'd', [0] )
    dimuon_rec_m = array( 'd', [0] )
    dijet_m = array( 'd', [0] )
    dijet_rec_m = array( 'd', [0] )
    vis_ex_dimuon_m = array( 'd', [0] )
    vis_all_rec_m = array( 'd', [0] )
    vis_all_pt = array( 'd', [0] )
    scale = array( 'd', [0] )

    t = ROOT.TTree( 'Higgs Tree', 'Higgs Tree' )

    t.Branch( 'dimuon_m', dimuon_m, 'dimuon_m/D')
    t.Branch( 'dimuon_rec_m', dimuon_rec_m, 'dimuon_rec_m/D')
    t.Branch( 'dijet_m', dijet_m, 'dijet_m/D')
    t.Branch( 'dijet_rec_m', dijet_rec_m, 'dijet_rec_m/D')
    t.Branch( 'vis_ex_dimuon_m', vis_ex_dimuon_m, 'vis_ex_dimuon_m/D')
    t.Branch( 'vis_all_rec_m', vis_all_rec_m, 'vis_all_rec_m/D')
    t.Branch( 'vis_all_pt', vis_all_pt, 'vis_all_pt/D')
    t.Branch( 'scale', scale, 'scale/D')

    for jentry in xrange(entries):

        ientry = t_in.LoadTree(jentry)
        if ientry < 0:
            break

        nb = t_in.GetEntry(jentry)
        if nb<=0:
            continue

        dimuon_m[0] = t_in.dimuon_m
        dimuon_rec_m[0] = t_in.dimuon_rec_m
        dijet_m[0] = t_in.dijet_m
        dijet_rec_m[0] = t_in.dijet_rec_m
        vis_ex_dimuon_m[0] = t_in.vis_ex_dimuon_m
        vis_all_rec_m[0] = t_in.vis_all_rec_m
        vis_all_pt[0] = t_in.vis_all_pt
        scale[0] = s

        t.Fill()

    fout.Write()
    fout.Close()


if __name__ == '__main__':
    main()