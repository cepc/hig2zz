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


def main():

    tabs = sys.argv[1:]

    signal_sample =  ROOT.TFile('./run/llh2zz/hist/ana_File_merged_1.root')

    evah = signal_sample.Get('hevtflw_pre')
    eva = evah.GetBinContent(1)  # # Total number of e2e2HZZ events analyzed
    scs = 5600 * 6.77 * 0.0264 / eva
    print('scale for signal is %s'%scs)

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

    print("%-25s%-25s%-25s"%('name','scale','final'))

    outname = './table/cut_info.txt'
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
                event_exp = 1.11 * float(l[3]) # 5050 fb-1 to 5600 fb-1

                sample = ROOT.TFile('./run/' + path + '/hist/' + dname + '/ana_File_merged_1.root')
                h=sample.Get('hevtflw_pre')
                event_ana = h.GetBinContent(1)

                if event_ana != 0:
                    scb = (event_exp / event_ana)

                    tep = sample.Get('hevtflw_sel')

                    evt = tep.GetBinContent(11) * scb

                    if int(evt) > 10:
                        print("%-25s%-25s%-25s"%(dname,scb,int(evt)))
                        tname = dname.replace('_',r'\_')
                        fout_script.write("%-25s&%-25s&%-25s%-25s\n"%(tname,scb,int(evt),r'\\'))

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

    print('\n')
    print("%-25s%-15s%-15s%-15s%-15s"%('cut','llhzz','zh','2f','4f'))
    print("%-25s%-15s%-15s%-15s%-15s"%('Raw events',int(s_raw),int(z_raw),int(f_raw),int(ff_raw)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Pre-selection',int(s1),int(z1),int(f1),int(ff1)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Signal or not',int(s2),int(z2),int(f2),int(ff2)))
    print("%-25s%-15s%-15s%-15s%-15s"%('missing mass > dijet',int(s3),int(z3),int(f3),int(ff3)))
    print("%-25s%-15s%-15s%-15s%-15s"%('M(dimuon) ',int(s4),int(z4),int(f4),int(ff4)))
    print("%-25s%-15s%-15s%-15s%-15s"%('RecM(dimuon) ',int(s5),int(z5),int(f5),int(ff5)))
    print("%-25s%-15s%-15s%-15s%-15s"%('N(pfo) ',int(s6),int(z6),int(f6),int(ff6)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Pt(total visible) ',int(s7),int(z7),int(f7),int(ff7)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Min angle ',int(s8),int(z8),int(f8),int(ff8)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Missing Mass & M(dijets)',int(s9),int(z9),int(f9),int(ff9)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Single jet',int(s10),int(z10),int(f10),int(ff10)))
    print("%-25s%-15s%-15s%-15s%-15s"%('N(lepton)',int(s11),int(z11),int(f11),int(ff11)))


    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('cut','signal','zh background','2f background','4f background',r'\\ \hline'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('Raw events',int(s_raw),int(z_raw),int(f_raw),int(ff_raw),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Pre-selection$',int(s1),int(z1),int(f1),int(ff1),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Signal or not$',int(s2),int(z2),int(f2),int(ff2),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Missing Mass>M_{dijets}$',int(s3),int(z3),int(f3),int(ff3),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$80GeV<M_{\mu^{+}\mu^{-}}<100GeV$',int(s4),int(z4),int(f4),int(ff4),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$120GeV<M_{Recoil}<150GeV$',int(s5),int(z5),int(f5),int(ff5),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$15GeV<N_{pfo}$',int(s6),int(z6),int(f6),int(ff6),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$10GeV<Pt_{total visible}$',int(s7),int(z7),int(f7),int(ff7),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Min angle>0.3$\degree ',int(s8),int(z8),int(f8),int(ff8),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Missing Mass>80,M_{dijets}<35$\degree ',int(s9),int(z9),int(f9),int(ff9),r'\\'))
    fout_script.write('%-40s&%-25s&%-25s&%-25s&%-25s%-25s\n'%('$Pt_{jet1,2}>3,E_{jet1,2}>3$',int(s10),int(z10),int(f10),int(ff10),r'\\'))

    fout_script.close()
    
if __name__ == '__main__':
    main()
