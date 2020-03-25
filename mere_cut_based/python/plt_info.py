#!/usr/bin/env python
"""
Plot information 
"""

__author__ = "Kong Lingteng <konglingteng15@mails.ucas.ac.cn>"
__copyright__ = "Copyright (c) Kong Lingteng"
__created__ = "[2019-01-11 Fri 01:39]" 

import sys,os,copy
import math
import ROOT 
from tools import check_outfile_path

ZZ_Selection = int(sys.argv[1])

def main():

    combine_opt = int(sys.argv[2])
    tabs = sys.argv[3:]

    if (combine_opt==1):
        signal_sample =  ROOT.TFile('./run/channel_ll_%s/llh2zz/hist/ana_File_merged_1.root'%ZZ_Selection)
    if (combine_opt==2):
        signal_sample =  ROOT.TFile('./run/channel_nn_%s/nnh2zz/hist/ana_File_merged_1.root'%ZZ_Selection)
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
        for i in range(21):
            exec ("s%s = tep.GetBinContent(%s) * scs"%(i+1,i+1))

        for i in range(21):
            exec ("z%s = 0"%(i+1))
            exec ("f%s = 0"%(i+1))
            exec ("ff%s = 0"%(i+1))
    
    if (combine_opt==2):
        for i in range(21):
            exec ("s%s = tep.GetBinContent(%s) * scs"%(i+1,i+1))

        for i in range(21):
            exec ("z%s = 0"%(i+1))
            exec ("f%s = 0"%(i+1))
            exec ("ff%s = 0"%(i+1))

    if (combine_opt==3):
        for i in range(21):
            exec ("s%s = tep.GetBinContent(%s) * scs"%(i+1,i+1))

        for i in range(21):
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
        outname = './table/channel_nn_%s/cut_info.txt'%ZZ_Selection
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
                    sample = ROOT.TFile('./run/channel_nn_%s/'%ZZ_Selection + path + '/hist/' + dname + '/ana_File_merged_1.root')
                if (combine_opt==3):
                    sample = ROOT.TFile('./run/channel_qq_%s/'%ZZ_Selection + path + '/hist/' + dname + '/ana_File_merged_1.root')

                h=sample.Get('hevtflw_pre')
                event_ana = h.GetBinContent(1)

                if event_ana != 0:
                    scb = (event_exp / event_ana)

                    tep = sample.Get('hevtflw_sel')

                    if (combine_opt==1):
                        evt = tep.GetBinContent(21) * scb
                    if (combine_opt==2):
                        evt = tep.GetBinContent(21) * scb
                    if (combine_opt==3):
                        evt = tep.GetBinContent(21) * scb

                    if evt > 1:
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
                        for i in range(21):
                            exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+1))
                            if tabs.index(t) == 0:
                                exec ("z%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 1:
                                exec ("f%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 2:
                                exec ("ff%s += cut%s"%(i+1,i+1))

                    if (combine_opt==2):
                        for i in range(21):
                            exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+1))
                            if tabs.index(t) == 0:
                                exec ("z%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 1:
                                exec ("f%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 2:
                                exec ("ff%s += cut%s"%(i+1,i+1))

                    if (combine_opt==3):
                        for i in range(21):
                            exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+1))
                            if tabs.index(t) == 0:
                                exec ("z%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 1:
                                exec ("f%s += cut%s"%(i+1,i+1))
                            if tabs.index(t) == 2:
                                exec ("ff%s += cut%s"%(i+1,i+1))

    print('\n')
    if (combine_opt==1):
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cut','llhzz','ZH','2f','4f','S/sqrt(S+B)'))
    if (combine_opt==2):
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cut','nnhzz','ZH','2f','4f','S/sqrt(S+B)'))
    if (combine_opt==3):
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cut','qqHZZ','ZH','2f','4f','S/sqrt(S+B)'))

    print("%-25s%-15s%-15s%-15s%-15s"%('Expected',int(s_raw),int(z_raw),int(f_raw),int(ff_raw)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Pre-selection',int(s1),int(z1),int(f1),int(ff1)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Signal or not',int(s2),int(z2),int(f2),int(ff2)))

    if (combine_opt==1):
        if (ZZ_Selection==1):
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(missing)>M(dijet)',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Npfo',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dimuon)',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dijet)',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(missing)',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Cos',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cos(visible)',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Angle(ll-jj) ',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Mrec(dimuon)',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Mrec(dijet)',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*M(visible)',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*P(visible)',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(visible)',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(leading jet)',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(leading jet)',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(sub-leading jet)',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(sub-leading jet)',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not qqhzz',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not nnhzz',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4)))
        if (ZZ_Selection==2):
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(missing)<M(dijet)',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Npfo',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dimuon)',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dijet)',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(missing)',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Cos',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cos(visible)',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Angle(ll-jj) ',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Mrec(dimuon)',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Mrec(dijet)',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(visible)',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*P(visible)',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(visible)',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(leading jet)',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(leading jet)',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(sub-leading jet)',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(sub-leading jet)',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not qqhzz',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not nnhzz',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4)))

    if (combine_opt==2):
        if (ZZ_Selection==1):
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dimuon)>M(dijet)',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Npfo',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(missing)',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dimuon)',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dijet)',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Cos',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cos(visible)',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Angle(ll-jj) ',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Mrec(dimuon)',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Mrec(dijet)',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(visible)',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*P(visible)',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(visible)',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(leading jet)',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(leading jet)',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(sub-leading jet)',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(sub-leading jet)',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not mmhzz',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not qqhzz',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4)))
        if (ZZ_Selection==2):
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dimuon)<M(dijet)',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Npfo',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(missing)',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dimuon)',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dijet)',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Cos',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cos(visible)',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Angle(ll-jj) ',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Mrec(dimuon)',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Mrec(dijet)',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(visible)',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*P(visible)',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(visible)',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(leading jet)',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(leading jet)',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(sub-leading jet)',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(sub-leading jet)',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not mmhzz',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not qqhzz',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4)))

    if (combine_opt==3):
        if (ZZ_Selection==1):
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(missing)>M(dimuon)',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Npfo',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dijet)',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dimuon)',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(missing)',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Cos',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cos(visible)',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Angle(ll-jj)',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Mrec(dimuon)',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Mrec(dijet)',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(visible)',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*P(visible)',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(visible)',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(leading jet)',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(leading jet)',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(sub-leading jet)',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(sub-leading jet)',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not mmhzz',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not nnhzz',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4)))
        if (ZZ_Selection==2):
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(missing)<M(dimuon)',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Npfo',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dijet)',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dimuon)',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(missing)',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Cos',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cos(visible)',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Angle(ll-jj)',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Mrec(dimuon)',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Mrec(dijet)',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(visible)',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*P(visible)',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(visible)',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(leading jet)',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(leading jet)',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*E(sub-leading jet)',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('*Pt(sub-leading jet)',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not mmhzz',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('not nnhzz',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4)))
 
    fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('Cut','Signal','ZH Background','2f Background','4f Background','$S\over\sqrt{S+B}$',r'\\ \hline'))
    fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$Expected$',int(s_raw),int(z_raw),int(f_raw),int(ff_raw),'        ',r'\\'))
    fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$Pre-selection$',int(s1),int(z1),int(f1),int(ff1),'        ',r'\\'))
    fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$Signal \ or \ not$',int(s2),int(z2),int(f2),int(ff2),'        ',r'\\'))

    if (combine_opt==1): # mmHZZ
        if (ZZ_Selection==1): # mmHvvjj
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}>M_{dijet}$',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$N(pfo)$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}$',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dijet}$',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}$',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*cos \ \\theta$',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$Angle_{\mu j}$',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}^{rec}$',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dijet}^{rec}$',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*M_{visible}$',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{visible}$',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ qqHZZ$ ',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ \\nu\\nu HZZ$ ',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4),r'\\'))

        if (ZZ_Selection==2): # mmHjjvv
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}<M_{dijet}$',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$N(pfo)$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}$',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dijet}$',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}$',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*cos \ \\theta$',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$Angle_{\mu j}$',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}^{rec}$',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*M_{dijet}^{rec}$',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{visible}$',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{visible}$',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ qqHZZ$ ',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ \\nu\\nu HZZ$ ',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4),r'\\'))

    if (combine_opt==2): # vvHZZ
        if (ZZ_Selection==1): # vvHmmjj
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}>M_{dijet}$',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$N(pfo)$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}$',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}$',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dijet}$',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*cos \ \\theta$',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$Angle_{\mu j}$',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*M_{dimuon}^{rec}$',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*M_{dijet}^{rec}$',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{visible}$',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{visible}$',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ \mu^{+}\mu^{-}HZZ$ ',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ qqHZZ$ ',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4),r'\\'))

        if (ZZ_Selection==2): # vvHjjmm
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}<M_{dijet}$',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$N(pfo)$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}$',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}$',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dijet}$',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*cos \ \\theta$',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$Angle_{\mu j}$',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}^{rec}$',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*M_{dijet}^{rec}$',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{visible}$',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{visible}$',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ \mu^{+}\mu^{-}HZZ$ ',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ qqHZZ$ ',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4),r'\\'))

    if (combine_opt==3): # qqHZZ
        if (ZZ_Selection==1): # qqHvvmm
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}>M_{dimuon}$',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$N(pfo)$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dijet}$',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}$',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}$',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*cos \ \\theta$',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*Angle_{\mu j}$',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}^{rec}$',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dijet}^{rec}$',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{visible}$',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{visible}$',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ \mu^{+}\mu^{-}HZZ$ ',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ \\nu\\nu HZZ$ ',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4),r'\\'))

        if (ZZ_Selection==2): # qqHmmvv
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}<M_{dimuon}$',int(s3),int(z3),int(f3),int(ff3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$N(pfo)$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dijet}$',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}$',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}$',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*cos \ \\theta$',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$Angle_{\mu j}$',int(s10),int(z10),int(f10),int(ff10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}^{rec}$',int(s11),int(z11),int(f11),int(ff11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dijet}^{rec}$',int(s12),int(z12),int(f12),int(ff12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{visible}$',int(s13),int(z13),int(f13),int(ff13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{visible}$',int(s14),int(z14),int(f14),int(ff14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',int(s15),int(z15),int(f15),int(ff15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',int(s16),int(z16),int(f16),int(ff16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',int(s17),int(z17),int(f17),int(ff17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',int(s18),int(z18),int(f18),int(ff18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',int(s19),int(z19),int(f19),int(ff19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ \mu^{+}\mu^{-}HZZ$ ',int(s20),int(z20),int(f20),int(ff20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$not \ \\nu\\nu HZZ$ ',int(s21),int(z21),int(f21),int(ff21),round(s21/math.sqrt(s21+z21+f21+ff21),4),r'\\'))

    fout_script.close()
    
if __name__ == '__main__':
    main()
