#!/usr/bin/env python
"""
Plot information 
"""

__author__ = "Kong Lingteng <konglingteng15@mails.ucas.ac.cn>"
__copyright__ = "Copyright (c) Kong Lingteng"
__created__ = "[2019-01-11 Fri 01:39]" 

import sys,os,copy
import ROOT 
from tools import check_outfile_path

ZZ_Selection = int(sys.argv[1])

def main():

    combine_opt = int(sys.argv[2])
    tabs = sys.argv[3:]

    if (combine_opt==1):
        signal_sample =  ROOT.TFile('./run/channel_ll_%s/llh2zz/hist/ana_File_merged_1.root'%ZZ_Selection)
    if (combine_opt==2):
        signal_sample =  ROOT.TFile('./run/channel_nn/nnh2zz/hist/ana_File_merged_1.root')
    if (combine_opt==3):
        signal_sample =  ROOT.TFile('./run/channel_qq_%s/qqh2zz/hist/ana_File_merged_1.root'%ZZ_Selection)

    sh = signal_sample.Get('hevtflw_pre')
    eva = sh.GetBinContent(1)  #number of e2e2h
    if (combine_opt==1):
        scs = 5600 * 6.77 * 0.0264 / eva
    if (combine_opt==2):
        scs = 5600 * 46.3 * 0.0264 / eva
    if (combine_opt==3):
        scs = 5600 * 137 *0.0264 /eva

    print('scale for signal is %s'%scs)

    s_raw = sh.GetBinContent(1) * scs

    tep = signal_sample.Get('hevtflw_sel')

    if (combine_opt==1):
        for i in range(12):
            exec ("s%s = tep.GetBinContent(%s) * scs"%(i+1,i+1))

        for i in range(12):
            exec ("z%s = 0"%(i+1))
            exec ("f%s = 0"%(i+1))
            exec ("ff%s = 0"%(i+1))
    
    if (combine_opt==2):
        for i in range(16):
            exec ("s%s = tep.GetBinContent(%s) * scs"%(i+1,i+1))

        for i in range(16):
            exec ("z%s = 0"%(i+1))
            exec ("f%s = 0"%(i+1))
            exec ("ff%s = 0"%(i+1))

    if (combine_opt==3):
        for i in range(18):
            exec ("s%s = tep.GetBinContent(%s) * scs"%(i+1,i+1))

        for i in range(18):
            exec ("z%s = 0"%(i+1))
            exec ("f%s = 0"%(i+1))
            exec ("ff%s = 0"%(i+1))

    z_raw = 0
    f_raw = 0
    ff_raw = 0

    print("%-25s%-25s%-25s"%('name','scale','final'))

    if (combine_opt==1):
        outname = './table/channel_ll_%s/cut_info.txt'%ZZ_Selection
    if (combine_opt==2):
        outname = './table/channel_nn/cut_info.txt'
    if (combine_opt==3):
        outname = './table/channel_qq_%s/cut_info.txt'%ZZ_Selection

    fout_script = open(outname,'w')

    fout_script.write("%-25s&%-25s&%-25s%-25s\n"%('name','scale','final',r'\\ \hline'))
        

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
                    sample = ROOT.TFile('./run/channel_ll_%s/'%ZZ_Selection + path + '/hist/' + dname + '/ana_File_merged_1.root')
                if (combine_opt==2):
                    sample = ROOT.TFile('./run/channel_nn/' + path + '/hist/' + dname + '/ana_File_merged_1.root')
                if (combine_opt==3):
                    sample = ROOT.TFile('./run/channel_qq_%s/'%ZZ_Selection + path + '/hist/' + dname + '/ana_File_merged_1.root')

                h=sample.Get('hevtflw_pre')
                event_ana = h.GetBinContent(1)

                if event_ana != 0:
                    scb = (event_exp / event_ana)

                    tep = sample.Get('hevtflw_sel')

                    if (combine_opt==1):
                        evt = tep.GetBinContent(12) * scb
                    if (combine_opt==2):
                        evt = tep.GetBinContent(16) * scb
                    if (combine_opt==3):
                        evt = tep.GetBinContent(18) * scb

                    if evt > 0:
                        print("%-25s%-25s%-25s"%(dname,scb,evt))
                        tname = dname.replace('_',r'\_')
                        fout_script.write("%-25s&%-25s&%-25s%-25s\n"%(tname,scb,int(evt),r'\\'))

                    if tabs.index(t) == 0:
                        z_raw += event_exp

                    if tabs.index(t) == 1:
                        f_raw += event_exp

                    if tabs.index(t) == 2:
                        ff_raw += event_exp

                    if (combine_opt==1):
                        for i in range(12):
                            exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+1))
                            if tabs.index(t) == 0:
                                exec ("z%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 1:
                                exec ("f%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 2:
                                exec ("ff%s += cut%s"%(i+1,i+1))

                    if (combine_opt==2):
                        for i in range(16):
                            exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+1))
                            if tabs.index(t) == 0:
                                exec ("z%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 1:
                                exec ("f%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 2:
                                exec ("ff%s += cut%s"%(i+1,i+1))

                    if (combine_opt==3):
                        for i in range(18):
                            exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+1))
                            if tabs.index(t) == 0:
                                exec ("z%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 1:
                                exec ("f%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 2:
                                exec ("ff%s += cut%s"%(i+1,i+1))

    print('\n')
    if (combine_opt==1):
        print("%-25s%-15s%-15s%-15s%-15s"%('cut','llhzz','zh','2f','4f'))
    if (combine_opt==2):
        print("%-25s%-15s%-15s%-15s%-15s"%('cut','nnhzz','zh','2f','4f'))
    if (combine_opt==3):
        print("%-25s%-15s%-15s%-15s%-15s"%('cut','qqhzz','zh','2f','4f'))

    print("%-25s%-15s%-15s%-15s%-15s"%('Raw events',int(s_raw),int(z_raw),int(f_raw),int(ff_raw)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Pre-selection',int(s1),int(z1),int(f1),int(ff1)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Signal or not',int(s2),int(z2),int(f2),int(ff2)))

    if (combine_opt==1):
        if (ZZ_Selection==1):
            print("%-25s%-15s%-15s%-15s%-15s"%('missingM > M(dijet)',int(s3),int(z3),int(f3),int(ff3)))
        if (ZZ_Selection==2):
            print("%-25s%-15s%-15s%-15s%-15s"%('M(dijet) > missingM',int(s3),int(z3),int(f3),int(ff3)))
        print("%-25s%-15s%-15s%-15s%-15s"%('M(dimuon) ',int(s4),int(z4),int(f4),int(ff4)))
        print("%-25s%-15s%-15s%-15s%-15s"%('RecM(dimuon) ',int(s5),int(z5),int(f5),int(ff5)))
        print("%-25s%-15s%-15s%-15s%-15s"%('N(pfo) ',int(s6),int(z6),int(f6),int(ff6)))
        print("%-25s%-15s%-15s%-15s%-15s"%('Pt(total visible) ',int(s7),int(z7),int(f7),int(ff7)))
        print("%-25s%-15s%-15s%-15s%-15s"%('Min angle ',int(s8),int(z8),int(f8),int(ff8)))
        print("%-25s%-15s%-15s%-15s%-15s"%('Missing Mass & M(dijets)',int(s9),int(z9),int(f9),int(ff9)))
        print("%-25s%-15s%-15s%-15s%-15s"%('Single jet',int(s10),int(z10),int(f10),int(ff10)))
        print("%-25s%-15s%-15s%-15s%-15s"%('RecM(dijet) not qqhzz',int(s11),int(z11),int(f11),int(ff11)))
        print("%-25s%-15s%-15s%-15s%-15s"%('VisM not vvhzz',int(s12),int(z12),int(f12),int(ff12)))

    if (combine_opt==2):
        print("%-25s%-15s%-15s%-15s%-15s"%('Npfo',int(s3),int(z3),int(f3),int(ff3)))
        print("%-25s%-15s%-15s%-15s%-15s"%('Vis_mass',int(s4),int(z4),int(f4),int(ff4)))
        print("%-25s%-15s%-15s%-15s%-15s"%('cos_theta ',int(s5),int(z5),int(f5),int(ff5)))
        print("%-25s%-15s%-15s%-15s%-15s"%('RecM(dimuon) ',int(s6),int(z6),int(f6),int(ff6)))
        print("%-25s%-15s%-15s%-15s%-15s"%('vis_all_p ',int(s7),int(z7),int(f7),int(ff7)))
        print("%-25s%-15s%-15s%-15s%-15s"%('M(dijet) ',int(s8),int(z8),int(f8),int(ff8)))
        print("%-25s%-15s%-15s%-15s%-15s"%('jet_lead_e ',int(s9),int(z9),int(f9),int(ff9)))
        print("%-25s%-15s%-15s%-15s%-15s"%('jet_sub_e',int(s10),int(z10),int(f10),int(ff10)))
        print("%-25s%-15s%-15s%-15s%-15s"%('angle_mj',int(s11),int(z11),int(f11),int(ff11)))
        print("%-25s%-15s%-15s%-15s%-15s"%('M(dimuon)',int(s12),int(z12),int(f12),int(ff12)))
        print("%-25s%-15s%-15s%-15s%-15s"%('vis_all_cos',int(s13),int(z13),int(f13),int(ff13)))
        print("%-25s%-15s%-15s%-15s%-15s"%('RecM(vis_all)',int(s14),int(z14),int(f14),int(ff14)))
        print("%-25s%-15s%-15s%-15s%-15s"%('RecM(dimuon) not mmHzz',int(s15),int(z15),int(f15),int(ff15)))
        print("%-25s%-15s%-15s%-15s%-15s"%('RecM(dijet) not qqHzz',int(s16),int(z16),int(f16),int(ff16)))

    if (combine_opt==3):
        if (ZZ_Selection==1):
            print("%-25s%-15s%-15s%-15s%-15s"%('M(missing)>M(dimuon)',int(s3),int(z3),int(f3),int(ff3)))
        if (ZZ_Selection==2):
            print("%-25s%-15s%-15s%-15s%-15s"%('M(dimuon)>M(missing)',int(s3),int(z3),int(f3),int(ff3)))
        print("%-25s%-15s%-15s%-15s%-15s"%('Npfo',int(s4),int(z4),int(f4),int(ff4)))
        print("%-25s%-15s%-15s%-15s%-15s"%('Vis_mass',int(s5),int(z5),int(f5),int(ff5)))
        print("%-25s%-15s%-15s%-15s%-15s"%('cos_theta ',int(s6),int(z6),int(f6),int(ff6)))
        print("%-25s%-15s%-15s%-15s%-15s"%('RecM(dimuon) ',int(s7),int(z7),int(f7),int(ff7)))
        print("%-25s%-15s%-15s%-15s%-15s"%('vis_all_p ',int(s8),int(z8),int(f8),int(ff8)))
        print("%-25s%-15s%-15s%-15s%-15s"%('M(dijet) ',int(s9),int(z9),int(f9),int(ff9)))
        print("%-25s%-15s%-15s%-15s%-15s"%('jet_lead_e ',int(s10),int(z10),int(f10),int(ff10)))
        print("%-25s%-15s%-15s%-15s%-15s"%('jet_sub_e',int(s11),int(z11),int(f11),int(ff11)))
        print("%-25s%-15s%-15s%-15s%-15s"%('angle_mj',int(s12),int(z12),int(f12),int(ff12)))
        print("%-25s%-15s%-15s%-15s%-15s"%('M(dimuon)',int(s13),int(z13),int(f13),int(ff13)))
        print("%-25s%-15s%-15s%-15s%-15s"%('vis_all_cos',int(s14),int(z14),int(f14),int(ff14)))
        print("%-25s%-15s%-15s%-15s%-15s"%('RecM(vis_all)',int(s15),int(z15),int(f15),int(ff15)))
        print("%-25s%-15s%-15s%-15s%-15s"%('vis_all_pt',int(s16),int(z16),int(f16),int(ff16)))
        print("%-25s%-15s%-15s%-15s%-15s"%('not mmhzz',int(s17),int(z17),int(f17),int(ff17)))
        print("%-25s%-15s%-15s%-15s%-15s"%('not nnhzz',int(s18),int(z18),int(f18),int(ff18)))
 

    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('cut','signal','zh background','2f background','4f background',r'\\ \hline'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Expected$',int(s_raw),int(z_raw),int(f_raw),int(ff_raw),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Pre-selection$',int(s1),int(z1),int(f1),int(ff1),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Signal \ or \ not$',int(s2),int(z2),int(f2),int(ff2),r'\\'))

    if (combine_opt==1):
        if (ZZ_Selection==1):
            fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{missing}>M_{dijet}$',int(s3),int(z3),int(f3),int(ff3),r'\\'))
        if (ZZ_Selection==2):
            fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{dijet}<M_{missing}$',int(s3),int(z3),int(f3),int(ff3),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{\mu^{+}\mu^{-}}$',int(s4),int(z4),int(f4),int(ff4),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{dimuon}^{rec}$',int(s5),int(z5),int(f5),int(ff5),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$N(pfo)$',int(s6),int(z6),int(f6),int(ff6),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Pt_{visible}$',int(s7),int(z7),int(f7),int(ff7),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Angle_{min}$ ',int(s8),int(z8),int(f8),int(ff8),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{missing}, \ M_{dijet}$',int(s9),int(z9),int(f9),int(ff9),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Pt_{jet1,2}, \ E_{jet1,2}$',int(s10),int(z10),int(f10),int(ff10),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$not \ qqHZZ$',int(s11),int(z11),int(f11),int(ff11),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$not \ \\nu \\nu HZZ$',int(s12),int(z12),int(f12),int(ff12),r'\\'))

    if (combine_opt==2):
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$N(pfo)$',int(s3),int(z3),int(f3),int(ff3),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{visible}$',int(s4),int(z4),int(f4),int(ff4),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$cos\ \\theta$',int(s5),int(z5),int(f5),int(ff5),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{dimuon}$',int(s6),int(z6),int(f6),int(ff6),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$P_{visible}$',int(s7),int(z7),int(f7),int(ff7),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{dijet}$',int(s8),int(z8),int(f8),int(ff8),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$E_{leading \ jet}$ ',int(s9),int(z9),int(f9),int(ff9),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$E_{subleading \ jet}$ ',int(s10),int(z10),int(f10),int(ff10),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Angle_{\mu j}$',int(s11),int(z11),int(f11),int(ff11),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{\mu^{+}\mu^{-}}$',int(s12),int(z12),int(f12),int(ff12),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$cos \ \\theta_{visible}$ ',int(s13),int(z13),int(f13),int(ff13),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{visible}^{rec}$ ',int(s14),int(z14),int(f14),int(ff14),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$not \ \mu^{+}\mu^{-}HZZ$ ',int(s15),int(z15),int(f15),int(ff15),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$not \ qqHZZ$ ',int(s16),int(z16),int(f16),int(ff16),r'\\'))

    if (combine_opt==3):
        if (ZZ_Selection==1):
            fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{missing}>M_{dimuon}$',int(s3),int(z3),int(f3),int(ff3),r'\\'))
        if (ZZ_Selection==2):
            fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{dimuon}>M_{missing}$',int(s3),int(z3),int(f3),int(ff3),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$N(pfo)$',int(s4),int(z4),int(f4),int(ff4),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{visible}$',int(s5),int(z5),int(f5),int(ff5),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$cos \ \\theta$',int(s6),int(z6),int(f6),int(ff6),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{dimuon}^{rec}$',int(s7),int(z7),int(f7),int(ff7),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$P_{visible}$',int(s8),int(z8),int(f8),int(ff8),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{dijet}$',int(s9),int(z9),int(f9),int(ff9),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$E_{leading \ jet}$ ',int(s10),int(z10),int(f10),int(ff10),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$E_{subleading \ jet}$ ',int(s11),int(z11),int(f11),int(ff11),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Angle_{\mu j}$',int(s12),int(z12),int(f12),int(ff12),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{dimuon}$',int(s13),int(z13),int(f13),int(ff13),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$cos \\theta_{visible} $ ',int(s14),int(z14),int(f14),int(ff14),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$M_{visible}^{rec}$ ',int(s15),int(z15),int(f15),int(ff15),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Pt_{visible}$ ',int(s16),int(z16),int(f16),int(ff16),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$not \mu^{+}\mu^{-}HZZ$ ',int(s17),int(z17),int(f17),int(ff17),r'\\'))
        fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$not \\nu\\nu HZZ$ ',int(s18),int(z18),int(f18),int(ff18),r'\\'))

    fout_script.close()
    
if __name__ == '__main__':
    main()
