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

    combine_opt = int(sys.argv[1])
    flag_zz = sys.argv[2]

    #signal
    if (combine_opt==1):
        s_in = './run/channel_ll_' + flag_zz + '/llh2zz/hist/ana_File_merged_1.root'
        s_out = './root/channel_ll_' + flag_zz + '/sig.root'
    if (combine_opt==2):
        s_in = './run/channel_nn_' + flag_zz + '/nnh2zz/hist/ana_File_merged_1.root'
        s_out = './root/channel_nn_' + flag_zz + '/sig.root'
    if (combine_opt==3):
        s_in = './run/channel_qq_' + flag_zz + '/qqh2zz/hist/ana_File_merged_1.root'
        s_out = './root/channel_qq_' + flag_zz + '/sig.root'

    signal_sample =  ROOT.TFile(s_in)
    evah = signal_sample.Get('hevtflw_sel')
    eva = evah.GetBinContent(1)  #number of e2e2h
    if (combine_opt==1):
        s = 5600 * 6.77 * 0.0264 / eva
    if (combine_opt==2):
        s = 5600 * 46.3 * 0.0264 / eva
    if (combine_opt==3):
        s = 5600 * 137 * 0.0264 / eva

    save_root(s_in, s_out, s, combine_opt)

    #background
    tabs = sys.argv[3:]

    for t in tabs: 

        tab = open(t , 'r' )
        name = t.split('/')[-1]
        path = name.split('_')[0]

        for s_line in tab :
            
            if not s_line.startswith('#'):
                l = [x.strip() for x in s_line.split(',')]
                dname = l[0]
                event_exp = 5600.0/5050.0 * float(l[3])
                if (combine_opt==1):
                    b_in = './run/channel_ll_' + flag_zz + '/' + path + '/hist/' + dname + '/ana_File_merged_1.root'
                if (combine_opt==2):
                    b_in = './run/channel_nn_' + flag_zz + '/' + path + '/hist/' + dname + '/ana_File_merged_1.root'
                if (combine_opt==3):
                    b_in = './run/channel_qq_' + flag_zz + '/' + path + '/hist/' + dname + '/ana_File_merged_1.root'
                sample = ROOT.TFile(b_in)
                h=sample.Get('hevtflw_sel')
                event_ana = h.GetBinContent(1)

                if event_ana != 0:
                    s = (event_exp / event_ana)

                    tep=sample.Get('hevtflw_sel')

                    if (combine_opt==1):
                        if tep.GetBinContent(9) != 0:
                            b_out = './root/channel_ll_%s/bkg_%s.root'%(flag_zz, dname)
                            save_root(b_in, b_out, s, combine_opt)
                    if (combine_opt==2):
                        if tep.GetBinContent(7) != 0:
                            b_out = './root/channel_nn_%s/bkg_%s.root'%(flag_zz, dname)
                            save_root(b_in, b_out, s, combine_opt)
                    if (combine_opt==3):
                        if tep.GetBinContent(9) != 0:
                            b_out = './root/channel_qq_%s/bkg_%s.root'%(flag_zz, dname)
                            save_root(b_in, b_out, s, combine_opt)

def save_root(f_in, f_out, s, combine_opt):

    check_outfile_path(f_out)
    print f_in, f_out 
    fin = ROOT.TFile(f_in)
    fout = ROOT.TFile(f_out, "RECREATE")

    t_in = fin.Get('Higgs Tree')
    entries = t_in.GetEntriesFast()

    dimuon_m = array( 'f', [0] )
    dimuon_rec_m = array( 'f', [0] )
    dijet_m = array( 'f', [0] )
    dijet_rec_m = array( 'f', [0] )
    vis_all_rec_m = array( 'f', [0] )
    vis_all_pt = array( 'f', [0] )
    vis_all_m = array( 'f', [0] )
    scale = array( 'f', [0] )

    t = ROOT.TTree( 'HiggsTree', 'HiggsTree' )

    t.Branch( 'dimuon_m', dimuon_m, 'dimuon_m/F')
    t.Branch( 'dimuon_rec_m', dimuon_rec_m, 'dimuon_rec_m/F')
    t.Branch( 'dijet_m', dijet_m, 'dijet_m/F')
    t.Branch( 'dijet_rec_m', dijet_rec_m, 'dijet_rec_m/F')
    t.Branch( 'vis_all_m', vis_all_m, 'vis_all_m/F')
    t.Branch( 'vis_all_rec_m', vis_all_rec_m, 'vis_all_rec_m/F')
    t.Branch( 'vis_all_pt', vis_all_pt, 'vis_all_pt/F')

    if (combine_opt==1):
        t.Branch( 'Mass_H', dimuon_rec_m, 'Mass_H/F')
    if (combine_opt==2):
        t.Branch( 'Mass_H', vis_all_m, 'Mass_H/F')
    if (combine_opt==3):
        t.Branch( 'Mass_H', dijet_rec_m, 'Mass_H/F')
    t.Branch( 'weight', scale, 'weight/F')

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
        vis_all_rec_m[0] = t_in.vis_all_rec_m
        vis_all_pt[0] = t_in.vis_all_pt
        vis_all_m[0] = t_in.vis_all_m
        scale[0] = s

        t.Fill()

    fout.Write()
    fout.Close()

if __name__ == '__main__':
    main()
