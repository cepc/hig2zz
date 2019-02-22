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

    evah = signal_sample.Get('hevtflw_pre')
    eva = evah.GetBinContent(1)
    scs = 5050 * 6.77 * 0.0266 / (eva * (6.77 / (7.04 + 6.77 + 6.75)))

    tep = signal_sample.Get('hevtflw_sel')
    for i in range(9):
        exec ("s%s = tep.GetBinContent(%s) * scs"%(i+1,i+3))

    for i in range(9):
        exec ("z%s = 0"%(i+1))
        exec ("f%s = 0"%(i+1))
        exec ("ff%s = 0"%(i+1))

    for t in tabs: 

        tab = open(t , 'r' )
        
        for s_line in tab :
            if not s_line.startswith('#'):
                l = [x.strip() for x in s_line.split(',')]
                dname = l[0]
                event_exp = float(l[3])
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
                    # if scb < 2:
                        for i in range(9):
                            exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+3))

                            if tabs.index(t) == 0:
                                exec ("z%s += cut%s"%(i+1,i+1))

                            if tabs.index(t) == 1:
                                exec ("f%s += cut%s"%(i+1,i+1))

                            if tabs.index(t) == 2:
                                exec ("ff%s += cut%s"%(i+1,i+1))

    if opt == 0 :
        print("%-25s%-25s%-25s"%('name','scale','final'))

    if opt == 1 :
        print("%-25s%-25s%-25s%-25s%-25s"%('cut','signal','zh','2f','4f'))
        print("%-25s%-25s%-25s%-25s%-25s"%('start cut',s1,z1,f1,ff1))
        print("%-25s%-25s%-25s%-25s%-25s"%('M(dimuon) ',s2,z2,f2,ff2))
        print("%-25s%-25s%-25s%-25s%-25s"%('RecM(dimuon) ',s3,z3,f3,ff3))
        print("%-25s%-25s%-25s%-25s%-25s"%('N(pfo) ',s4,z4,f4,ff4))
        print("%-25s%-25s%-25s%-25s%-25s"%('Pt(total visible) ',s5,z5,f5,ff5))
        print("%-25s%-25s%-25s%-25s%-25s"%('Min angle ',s6,z6,f6,ff6))
        print("%-25s%-25s%-25s%-25s%-25s"%('Missing Mass & M(dijets)',s7,z7,f7,ff7))
        print("%-25s%-25s%-25s%-25s%-25s"%('Pt(jets)',s8,z8,f8,ff8))
        print("%-25s%-25s%-25s%-25s%-25s"%('N(lepton)',s9,z9,f9,ff9))

if __name__ == '__main__':
    main()
