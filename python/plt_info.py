#!/usr/bin/env python
"""
Plot information 
"""

__author__ = "Kong Lingteng <konglingteng15@mails.ucas.ac.cn>"
__copyright__ = "Copyright (c) Kong Lingteng"
__created__ = "[2019-01-11 Fri 01:39]" 

import sys,os,copy
import ROOT 


def main():
 
    draw_info(0) #plt scale and cut detail
    draw_info(1) #plt cut flow table

def draw_info(opt):

    tabs = sys.argv[1:]

    signal_sample =  ROOT.TFile('./run/llh2zz/hist/ana_File_merged_1.root')

    evah = signal_sample.Get('hevtflw_sel')
    eva = evah.GetBinContent(3)  #number of e2e2hvvjj
    scs = 5600 * 6.77 * 0.0264 * 0.2 * 0.69 / eva

    sh = signal_sample.Get('hevtflw_pre')
    s_raw = sh.GetBinContent(1) * scs

    tep = signal_sample.Get('hevtflw_sel')
    for i in range(11):
        exec ("s%s = tep.GetBinContent(%s) * scs"%(i+1,i+1))

    for i in range(11):
        exec ("z%s = 0"%(i+1))
        exec ("f%s = 0"%(i+1))
        exec ("ff%s = 0"%(i+1))
    
    z_raw = 0
    f_raw = 0
    ff_raw = 0

    if opt == 0 :
        print("%-25s%-25s%-25s"%('name','scale','final'))

    for t in tabs: 

        tab = open(t , 'r' )
        
        for s_line in tab :
            if not s_line.startswith('#'):
                l = [x.strip() for x in s_line.split(',')]
                dname = l[0]
                event_exp = 1.11 * float(l[3])
                sample = ROOT.TFile('./run/bg/hist/' + dname + '/ana_File_merged_1.root')
                h=sample.Get('hevtflw_pre')
                event_ana = h.GetBinContent(1)

                if event_ana != 0:
                    scb = (event_exp / event_ana)

                tep = sample.Get('hevtflw_sel')

                if opt == 0:   #cut i = bincontent (i + 2)
                    # scb = 1
                    evt = tep.GetBinContent(11) * scb
                    if evt != 0:
                        print("%-25s%-25s%-25s"%(dname,scb,evt))

                if opt == 1:
                        for i in range(11):
                            exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+1))

                            if tabs.index(t) == 0:
                                exec ("z%s += cut%s"%(i+1,i+1))
                                z_raw += event_exp

                            if tabs.index(t) == 1:
                                exec ("f%s += cut%s"%(i+1,i+1))
                                f_raw += event_exp

                            if tabs.index(t) == 2:
                                exec ("ff%s += cut%s"%(i+1,i+1))
                                ff_raw += event_exp

    if opt == 1 :
        print('\n')
        print("%-25s%-25s%-25s%-25s%-25s"%('cut','llhzz','zh','2f','4f'))
        print("%-25s%-25s%-25s%-25s%-25s"%('Raw events',s_raw,z_raw,f_raw,ff_raw))
        print("%-25s%-25s%-25s%-25s%-25s"%('Pre-selection',s1,z1,f1,ff1))
        print("%-25s%-25s%-25s%-25s%-25s"%('Signal or not',s2,z2,f2,ff2))
        print("%-25s%-25s%-25s%-25s%-25s"%('missing mass > dijet',s3,z3,f3,ff3))
        print("%-25s%-25s%-25s%-25s%-25s"%('M(dimuon) ',s4,z4,f4,ff4))
        print("%-25s%-25s%-25s%-25s%-25s"%('RecM(dimuon) ',s5,z5,f5,ff5))
        print("%-25s%-25s%-25s%-25s%-25s"%('N(pfo) ',s6,z6,f6,ff6))
        print("%-25s%-25s%-25s%-25s%-25s"%('Pt(total visible) ',s7,z7,f7,ff7))
        print("%-25s%-25s%-25s%-25s%-25s"%('Min angle ',s8,z8,f8,ff8))
        print("%-25s%-25s%-25s%-25s%-25s"%('Missing Mass & M(dijets)',s9,z9,f9,ff9))
        print("%-25s%-25s%-25s%-25s%-25s"%('Pt(jets)',s10,z10,f10,ff10))
        print("%-25s%-25s%-25s%-25s%-25s"%('N(lepton)',s11,z11,f11,ff11))

if __name__ == '__main__':
    main()
