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
        scs = 5600 * 137 * 0.0264 /eva

    print('scale for signal is %s'%scs)

    s_raw = sh.GetBinContent(1) * scs
#    s_raw_error = math.sqrt(sh.GetBinContent(1))*scs
    s_raw_error = math.sqrt(s_raw)
  
    tep = signal_sample.Get('hevtflw_sel')

    if (combine_opt==1):
        for i in range(21):
            exec ("s%s = tep.GetBinContent(%s) * scs"%(i+1,i+1))
#	    exec ("serror%s = tep.GetBinContent(%s)**0.5 * scs"%(i+1,i+1))
            exec ("serror%s = math.sqrt(s%s)"%(i+1,i+1))

        for i in range(21):
            exec ("z%s = 0"%(i+1))
            exec ("f%s = 0"%(i+1))
            exec ("ff%s = 0"%(i+1))
            exec ("zerror%s = 0"%(i+1))
            exec ("ferror%s = 0"%(i+1))
            exec ("fferror%s = 0"%(i+1))
    
    if (combine_opt==2):
        for i in range(21):
            exec ("s%s = tep.GetBinContent(%s) * scs"%(i+1,i+1))
#            exec ("serror%s = tep.GetBinContent(%s)**0.5 * scs"%(i+1,i+1))
            exec ("serror%s = math.sqrt(s%s)"%(i+1,i+1))

        for i in range(21):
            exec ("z%s = 0"%(i+1))
            exec ("f%s = 0"%(i+1))
            exec ("ff%s = 0"%(i+1))
            exec ("zerror%s = 0"%(i+1))
            exec ("ferror%s = 0"%(i+1))
            exec ("fferror%s = 0"%(i+1))

    if (combine_opt==3):
        for i in range(21):
            exec ("s%s = tep.GetBinContent(%s) * scs"%(i+1,i+1))
#            exec ("serror%s = tep.GetBinContent(%s)**0.5 * scs"%(i+1,i+1))
            exec ("serror%s = math.sqrt(s%s)"%(i+1,i+1))

        for i in range(21):
            exec ("z%s = 0"%(i+1))
            exec ("f%s = 0"%(i+1))
            exec ("ff%s = 0"%(i+1))
            exec ("zerror%s = 0"%(i+1))
            exec ("ferror%s = 0"%(i+1))
            exec ("fferror%s = 0"%(i+1))

    z_raw = 0
    f_raw = 0
    ff_raw = 0
    z_raw_error = 0
    f_raw_error = 0
    ff_raw_error = 0

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
#			z_raw_error += scb*scb*event_ana
                    if tabs.index(t) == 1:
                        f_raw += event_exp
#			f_raw_error += scb*scb*event_ana
                    if tabs.index(t) == 2:
                        ff_raw += event_exp
#			ff_raw_error += scb*scb*event_ana

                    if (combine_opt==1):
                        for i in range(21):
                            exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+1))
#			    exec ("cuterror%s = tep.GetBinContent(%s) * scb * scb"%(i+1,i+1))
                            if tabs.index(t) == 0:
                                exec ("z%s += cut%s"%(i+1,i+1))
#                                exec ("zerror%s += cuterror%s"%(i+1,i+1))
                            if tabs.index(t) == 1:
                                exec ("f%s += cut%s"%(i+1,i+1))
#				exec ("ferror%s += cuterror%s"%(i+1,i+1))
                            if tabs.index(t) == 2:
                                exec ("ff%s += cut%s"%(i+1,i+1))
#				exec ("fferror%s += cuterror%s"%(i+1,i+1))

                    if (combine_opt==2):
                        for i in range(21):
                            exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+1))
#                            exec ("cuterror%s = tep.GetBinContent(%s) * scb * scb"%(i+1,i+1))
                            if tabs.index(t) == 0:
                                exec ("z%s += cut%s"%(i+1,i+1))
#                                exec ("zerror%s += cuterror%s"%(i+1,i+1))
                            if tabs.index(t) == 1:
                                exec ("f%s += cut%s"%(i+1,i+1))
#                                exec ("ferror%s += cuterror%s"%(i+1,i+1))
                            if tabs.index(t) == 2:
                                exec ("ff%s += cut%s"%(i+1,i+1))
#                                exec ("fferror%s += cuterror%s"%(i+1,i+1))

                    if (combine_opt==3):
                        for i in range(21):
                            exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+1))
#                            exec ("cuterror%s = tep.GetBinContent(%s) * scb * scb"%(i+1,i+1))
                            if tabs.index(t) == 0:
                                exec ("z%s += cut%s"%(i+1,i+1))
#                                exec ("zerror%s += cuterror%s"%(i+1,i+1))
                            if tabs.index(t) == 1:
                                exec ("f%s += cut%s"%(i+1,i+1))
#                                exec ("ferror%s += cuterror%s"%(i+1,i+1))
                            if tabs.index(t) == 2:
                                exec ("ff%s += cut%s"%(i+1,i+1))
#                                exec ("fferror%s += cuterror%s"%(i+1,i+1))

#	z_raw_error = math.sqrt(z_raw_error)
#	f_raw_error = math.sqrt(f_raw_error)
#	ff_raw_error = math.sqrt(ff_raw_error)
        z_raw_error = math.sqrt(z_raw)
        f_raw_error = math.sqrt(f_raw)
	ff_raw_error = math.sqrt(ff_raw)

        for i in range(21):
            if tabs.index(t) == 0:
#                exec ("zerror%s = math.sqrt(zerror%s)"%(i+1,i+1))
                exec ("zerror%s = math.sqrt(z%s)"%(i+1,i+1))
            if tabs.index(t) == 1:
#                exec ("ferror%s = math.sqrt(ferror%s)"%(i+1,i+1))
                exec ("ferror%s = math.sqrt(f%s)"%(i+1,i+1))
            if tabs.index(t) == 2:
#                exec ("fferror%s = math.sqrt(fferror%s)"%(i+1,i+1))
                exec ("fferror%s = math.sqrt(ff%s)"%(i+1,i+1))

    print('\n')

    eff_error = (((s21/2+z21+f21+ff21)*serror21)**2+((s21+f21+ff21)*zerror21/2)**2-((s21+z21+ff21)*ferror21/2)**2+((s21+z21+f21)*fferror21/2)**2)**0.5/(s21+z21+f21+ff21)**1.5

    if (combine_opt==1):
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cut','llhzz','ZH','2f','4f','S/sqrt(S+B)'))
    if (combine_opt==2):
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cut','nnhzz','ZH','2f','4f','S/sqrt(S+B)'))
    if (combine_opt==3):
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cut','qqHZZ','ZH','2f','4f','S/sqrt(S+B)'))

    print("%-25s%-7s%-1s%-7s%-7s%-1s%-7s%-9s%-1s%-5s%-7s%-1s%-7s"%('Expected',round(s_raw,2),u'\u00B1',round(s_raw_error,2),int(z_raw),u'\u00B1',int(z_raw_error),int(f_raw),u'\u00B1',int(f_raw_error),int(ff_raw),u'\u00B1',int(ff_raw_error)))
    print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s"%('Pre-selection',round(s1,2),u'\u00B1',round(serror1,2),int(z1),u'\u00B1',int(zerror1),int(f1),u'\u00B1',int(ferror1),int(ff1),u'\u00B1',int(fferror1)))
    print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s"%('Signal or not',round(s2,2),u'\u00B1',round(serror2,2),int(z2),u'\u00B1',int(zerror2),int(f2),u'\u00B1',int(ferror2),int(ff2),u'\u00B1',int(fferror2)))

    if (combine_opt==1):
        if (ZZ_Selection==1):
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(missing)>M(dijet)',round(s3,2),u'\u00B1',round(serror3,2),int(z3),u'\u00B1',int(zerror3),int(f3),u'\u00B1',int(ferror3),int(ff3),u'\u00B1',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Npfo',round(s4,2),u'\u00B1',round(serror4,2),int(z4),u'\u00B1',int(zerror4),int(f4),u'\u00B1',int(ferror4),int(ff4),u'\u00B1',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dimuon)',round(s5,2),u'\u00B1',round(serror5,2),int(z5),u'\u00B1',int(zerror5),int(f5),u'\u00B1',int(ferror5),int(ff5),u'\u00B1',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dijet)',round(s6,2),u'\u00B1',round(serror6,2),int(z6),u'\u00B1',int(zerror6),int(f6),u'\u00B1',int(ferror6),int(ff6),u'\u00B1',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(missing)',round(s7,2),u'\u00B1',round(serror7,2),int(z7),u'\u00B1',int(zerror7),int(f7),u'\u00B1',int(ferror7),int(ff7),u'\u00B1',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Cos',round(s8,2),u'\u00B1',round(serror8,2),int(z8),u'\u00B1',int(zerror8),int(f8),u'\u00B1',int(ferror8),int(ff8),u'\u00B1',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Cos(visible)',round(s9,2),u'\u00B1',round(serror9,2),int(z9),u'\u00B1',int(zerror9),int(f9),u'\u00B1',int(ferror9),int(ff9),u'\u00B1',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Angle(ll-jj) ',round(s10,2),u'\u00B1',round(serror10,2),int(z10),u'\u00B1',int(zerror10),int(f10),u'\u00B1',int(ferror10),int(ff10),u'\u00B1',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Mrec(dimuon)',round(s11,2),u'\u00B1',round(serror11,2),int(z11),u'\u00B1',int(zerror11),int(f11),u'\u00B1',int(ferror11),int(ff11),u'\u00B1',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Mrec(dijet)',round(s12,2),u'\u00B1',round(serror12,2),int(z12),u'\u00B1',int(zerror12),int(f12),u'\u00B1',int(ferror12),int(ff12),u'\u00B1',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*M(visible)',round(s13,2),u'\u00B1',round(serror13,2),int(z13),u'\u00B1',int(zerror13),int(f13),u'\u00B1',int(ferror13),int(ff13),u'\u00B1',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*P(visible)',round(s14,2),u'\u00B1',round(serror14,2),int(z14),u'\u00B1',int(zerror14),int(f14),u'\u00B1',int(ferror14),int(ff14),u'\u00B1',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(visible)',round(s15,2),u'\u00B1',round(serror15,2),int(z15),u'\u00B1',int(zerror15),int(f15),u'\u00B1',int(ferror15),int(ff15),u'\u00B1',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(leading jet)',round(s16,2),u'\u00B1',round(serror16,2),int(z16),u'\u00B1',int(zerror16),int(f16),u'\u00B1',int(ferror16),int(ff16),u'\u00B1',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(leading jet)',round(s17,2),u'\u00B1',round(serror17,2),int(z17),u'\u00B1',int(zerror17),int(f17),u'\u00B1',int(ferror17),int(ff17),u'\u00B1',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(sub-leading jet)',round(s18,2),u'\u00B1',round(serror18,2),int(z18),u'\u00B1',int(zerror18),int(f18),u'\u00B1',int(ferror18),int(ff18),u'\u00B1',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(sub-leading jet)',round(s19,2),u'\u00B1',round(serror19,2),int(z19),u'\u00B1',int(zerror19),int(f19),u'\u00B1',int(ferror19),int(ff19),u'\u00B1',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('not qqhzz',round(s20,2),u'\u00B1',round(serror20,2),int(z20),u'\u00B1',int(zerror20),int(f20),u'\u00B1',int(ferror20),int(ff20),u'\u00B1',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s%-15s"%('not nnhzz',round(s21,2),u'\u00B1',round(serror21,2),int(z21),u'\u00B1',int(zerror21),int(f21),u'\u00B1',int(ferror21),int(ff21),u'\u00B1',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),eff_error))
        if (ZZ_Selection==2):
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(missing)<M(dijet)',round(s3,2),u'\u00B1',round(serror3,2),int(z3),u'\u00B1',int(zerror3),int(f3),u'\u00B1',int(ferror3),int(ff3),u'\u00B1',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Npfo',round(s4,2),u'\u00B1',round(serror4,2),int(z4),u'\u00B1',int(zerror4),int(f4),u'\u00B1',int(ferror4),int(ff4),u'\u00B1',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dimuon)',round(s5,2),u'\u00B1',round(serror5,2),int(z5),u'\u00B1',int(zerror5),int(f5),u'\u00B1',int(ferror5),int(ff5),u'\u00B1',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dijet)',round(s6,2),u'\u00B1',round(serror6,2),int(z6),u'\u00B1',int(zerror6),int(f6),u'\u00B1',int(ferror6),int(ff6),u'\u00B1',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(missing)',round(s7,2),u'\u00B1',round(serror7,2),int(z7),u'\u00B1',int(zerror7),int(f7),u'\u00B1',int(ferror7),int(ff7),u'\u00B1',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Cos',round(s8,2),u'\u00B1',round(serror8,2),int(z8),u'\u00B1',int(zerror8),int(f8),u'\u00B1',int(ferror8),int(ff8),u'\u00B1',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Cos(visible)',round(s9,2),u'\u00B1',round(serror9,2),int(z9),u'\u00B1',int(zerror9),int(f9),u'\u00B1',int(ferror9),int(ff9),u'\u00B1',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Angle(ll-jj) ',round(s10,2),u'\u00B1',round(serror10,2),int(z10),u'\u00B1',int(zerror10),int(f10),u'\u00B1',int(ferror10),int(ff10),u'\u00B1',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Mrec(dimuon)',round(s11,2),u'\u00B1',round(serror11,2),int(z11),u'\u00B1',int(zerror11),int(f11),u'\u00B1',int(ferror11),int(ff11),u'\u00B1',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Mrec(dijet)',round(s12,2),u'\u00B1',round(serror12,2),int(z12),u'\u00B1',int(zerror12),int(f12),u'\u00B1',int(ferror12),int(ff12),u'\u00B1',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(visible)',round(s13,2),u'\u00B1',round(serror13,2),int(z13),u'\u00B1',int(zerror13),int(f13),u'\u00B1',int(ferror13),int(ff13),u'\u00B1',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*P(visible)',round(s14,2),u'\u00B1',round(serror14,2),int(z14),u'\u00B1',int(zerror14),int(f14),u'\u00B1',int(ferror14),int(ff14),u'\u00B1',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(visible)',round(s15,2),u'\u00B1',round(serror15,2),int(z15),u'\u00B1',int(zerror15),int(f15),u'\u00B1',int(ferror15),int(ff15),u'\u00B1',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(leading jet)',round(s16,2),u'\u00B1',round(serror16,2),int(z16),u'\u00B1',int(zerror16),int(f16),u'\u00B1',int(ferror16),int(ff16),u'\u00B1',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(leading jet)',round(s17,2),u'\u00B1',round(serror17,2),int(z17),u'\u00B1',int(zerror17),int(f17),u'\u00B1',int(ferror17),int(ff17),u'\u00B1',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(sub-leading jet)',round(s18,2),u'\u00B1',round(serror18,2),int(z18),u'\u00B1',int(zerror18),int(f18),u'\u00B1',int(ferror18),int(ff18),u'\u00B1',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(sub-leading jet)',round(s19,2),u'\u00B1',round(serror19,2),int(z19),u'\u00B1',int(zerror19),int(f19),u'\u00B1',int(ferror19),int(ff19),u'\u00B1',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('not qqhzz',round(s20,2),u'\u00B1',round(serror20,2),int(z20),u'\u00B1',int(zerror20),int(f20),u'\u00B1',int(ferror20),int(ff20),u'\u00B1',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s%-15s"%('not nnhzz',round(s21,2),u'\u00B1',round(serror21,2),int(z21),u'\u00B1',int(zerror21),int(f21),u'\u00B1',int(ferror21),int(ff21),u'\u00B1',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),eff_error))

    if (combine_opt==2):
        if (ZZ_Selection==1):
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dimuon)>M(dijet)',round(s3,2),u'\u00B1',round(serror3,2),int(z3),u'\u00B1',int(zerror3),int(f3),u'\u00B1',int(ferror3),int(ff3),u'\u00B1',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Npfo',round(s4,2),u'\u00B1',round(serror4,2),int(z4),u'\u00B1',int(zerror4),int(f4),u'\u00B1',int(ferror4),int(ff4),u'\u00B1',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(missing)',round(s5,2),u'\u00B1',round(serror5,2),int(z5),u'\u00B1',int(zerror5),int(f5),u'\u00B1',int(ferror5),int(ff5),u'\u00B1',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dimuon)',round(s6,2),u'\u00B1',round(serror6,2),int(z6),u'\u00B1',int(zerror6),int(f6),u'\u00B1',int(ferror6),int(ff6),u'\u00B1',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dijet)',round(s7,2),u'\u00B1',round(serror7,2),int(z7),u'\u00B1',int(zerror7),int(f7),u'\u00B1',int(ferror7),int(ff7),u'\u00B1',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Cos',round(s8,2),u'\u00B1',round(serror8,2),int(z8),u'\u00B1',int(zerror8),int(f8),u'\u00B1',int(ferror8),int(ff8),u'\u00B1',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Cos(visible)',round(s9,2),u'\u00B1',round(serror9,2),int(z9),u'\u00B1',int(zerror9),int(f9),u'\u00B1',int(ferror9),int(ff9),u'\u00B1',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Angle(ll-jj) ',round(s10,2),u'\u00B1',round(serror10,2),int(z10),u'\u00B1',int(zerror10),int(f10),u'\u00B1',int(ferror10),int(ff10),u'\u00B1',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Mrec(dimuon)',round(s11,2),u'\u00B1',round(serror11,2),int(z11),u'\u00B1',int(zerror11),int(f11),u'\u00B1',int(ferror11),int(ff11),u'\u00B1',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Mrec(dijet)',round(s12,2),u'\u00B1',round(serror12,2),int(z12),u'\u00B1',int(zerror12),int(f12),u'\u00B1',int(ferror12),int(ff12),u'\u00B1',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(visible)',round(s13,2),u'\u00B1',round(serror13,2),int(z13),u'\u00B1',int(zerror13),int(f13),u'\u00B1',int(ferror13),int(ff13),u'\u00B1',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*P(visible)',round(s14,2),u'\u00B1',round(serror14,2),int(z14),u'\u00B1',int(zerror14),int(f14),u'\u00B1',int(ferror14),int(ff14),u'\u00B1',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(visible)',round(s15,2),u'\u00B1',round(serror15,2),int(z15),u'\u00B1',int(zerror15),int(f15),u'\u00B1',int(ferror15),int(ff15),u'\u00B1',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(leading jet)',round(s16,2),u'\u00B1',round(serror16,2),int(z16),u'\u00B1',int(zerror16),int(f16),u'\u00B1',int(ferror16),int(ff16),u'\u00B1',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(leading jet)',round(s17,2),u'\u00B1',round(serror17,2),int(z17),u'\u00B1',int(zerror17),int(f17),u'\u00B1',int(ferror17),int(ff17),u'\u00B1',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(sub-leading jet)',round(s18,2),u'\u00B1',round(serror18,2),int(z18),u'\u00B1',int(zerror18),int(f18),u'\u00B1',int(ferror18),int(ff18),u'\u00B1',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(sub-leading jet)',round(s19,2),u'\u00B1',round(serror19,2),int(z19),u'\u00B1',int(zerror19),int(f19),u'\u00B1',int(ferror19),int(ff19),u'\u00B1',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('not mmhzz',round(s20,2),u'\u00B1',round(serror20,2),int(z20),u'\u00B1',int(zerror20),int(f20),u'\u00B1',int(ferror20),int(ff20),u'\u00B1',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s%-15s"%('not qqhzz',round(s21,2),u'\u00B1',round(serror21,2),int(z21),u'\u00B1',int(zerror21),int(f21),u'\u00B1',int(ferror21),int(ff21),u'\u00B1',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),eff_error))
        if (ZZ_Selection==2):
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dimuon)<M(dijet)',round(s3,2),u'\u00B1',round(serror3,2),int(z3),u'\u00B1',int(zerror3),int(f3),u'\u00B1',int(ferror3),int(ff3),u'\u00B1',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Npfo',round(s4,2),u'\u00B1',round(serror4,2),int(z4),u'\u00B1',int(zerror4),int(f4),u'\u00B1',int(ferror4),int(ff4),u'\u00B1',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(missing)',round(s5,2),u'\u00B1',round(serror5,2),int(z5),u'\u00B1',int(zerror5),int(f5),u'\u00B1',int(ferror5),int(ff5),u'\u00B1',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dimuon)',round(s6,2),u'\u00B1',round(serror6,2),int(z6),u'\u00B1',int(zerror6),int(f6),u'\u00B1',int(ferror6),int(ff6),u'\u00B1',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dijet)',round(s7,2),u'\u00B1',round(serror7,2),int(z7),u'\u00B1',int(zerror7),int(f7),u'\u00B1',int(ferror7),int(ff7),u'\u00B1',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Cos',round(s8,2),u'\u00B1',round(serror8,2),int(z8),u'\u00B1',int(zerror8),int(f8),u'\u00B1',int(ferror8),int(ff8),u'\u00B1',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Cos(visible)',round(s9,2),u'\u00B1',round(serror9,2),int(z9),u'\u00B1',int(zerror9),int(f9),u'\u00B1',int(ferror9),int(ff9),u'\u00B1',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Angle(ll-jj) ',round(s10,2),u'\u00B1',round(serror10,2),int(z10),u'\u00B1',int(zerror10),int(f10),u'\u00B1',int(ferror10),int(ff10),u'\u00B1',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Mrec(dimuon)',round(s11,2),u'\u00B1',round(serror11,2),int(z11),u'\u00B1',int(zerror11),int(f11),u'\u00B1',int(ferror11),int(ff11),u'\u00B1',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Mrec(dijet)',round(s12,2),u'\u00B1',round(serror12,2),int(z12),u'\u00B1',int(zerror12),int(f12),u'\u00B1',int(ferror12),int(ff12),u'\u00B1',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(visible)',round(s13,2),u'\u00B1',round(serror13,2),int(z13),u'\u00B1',int(zerror13),int(f13),u'\u00B1',int(ferror13),int(ff13),u'\u00B1',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*P(visible)',round(s14,2),u'\u00B1',round(serror14,2),int(z14),u'\u00B1',int(zerror14),int(f14),u'\u00B1',int(ferror14),int(ff14),u'\u00B1',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(visible)',round(s15,2),u'\u00B1',round(serror15,2),int(z15),u'\u00B1',int(zerror15),int(f15),u'\u00B1',int(ferror15),int(ff15),u'\u00B1',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(leading jet)',round(s16,2),u'\u00B1',round(serror16,2),int(z16),u'\u00B1',int(zerror16),int(f16),u'\u00B1',int(ferror16),int(ff16),u'\u00B1',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(leading jet)',round(s17,2),u'\u00B1',round(serror17,2),int(z17),u'\u00B1',int(zerror17),int(f17),u'\u00B1',int(ferror17),int(ff17),u'\u00B1',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(sub-leading jet)',round(s18,2),u'\u00B1',round(serror18,2),int(z18),u'\u00B1',int(zerror18),int(f18),u'\u00B1',int(ferror18),int(ff18),u'\u00B1',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(sub-leading jet)',round(s19,2),u'\u00B1',round(serror19,2),int(z19),u'\u00B1',int(zerror19),int(f19),u'\u00B1',int(ferror19),int(ff19),u'\u00B1',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('not mmhzz',round(s20,2),u'\u00B1',round(serror20,2),int(z20),u'\u00B1',int(zerror20),int(f20),u'\u00B1',int(ferror20),int(ff20),u'\u00B1',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s%-15s"%('not qqhzz',round(s21,2),u'\u00B1',round(serror21,2),int(z21),u'\u00B1',int(zerror21),int(f21),u'\u00B1',int(ferror21),int(ff21),u'\u00B1',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),eff_error))

    if (combine_opt==3):
        if (ZZ_Selection==1):
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(missing)>M(dimuon)',round(s3,2),u'\u00B1',round(serror3,2),int(z3),u'\u00B1',int(zerror3),int(f3),u'\u00B1',int(ferror3),int(ff3),u'\u00B1',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Npfo',round(s4,2),u'\u00B1',round(serror4,2),int(z4),u'\u00B1',int(zerror4),int(f4),u'\u00B1',int(ferror4),int(ff4),u'\u00B1',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dijet)',round(s5,2),u'\u00B1',round(serror5,2),int(z5),u'\u00B1',int(zerror5),int(f5),u'\u00B1',int(ferror5),int(ff5),u'\u00B1',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dimuon)',round(s6,2),u'\u00B1',round(serror6,2),int(z6),u'\u00B1',int(zerror6),int(f6),u'\u00B1',int(ferror6),int(ff6),u'\u00B1',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(missing)',round(s7,2),u'\u00B1',round(serror7,2),int(z7),u'\u00B1',int(zerror7),int(f7),u'\u00B1',int(ferror7),int(ff7),u'\u00B1',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Cos',round(s8,2),u'\u00B1',round(serror8,2),int(z8),u'\u00B1',int(zerror8),int(f8),u'\u00B1',int(ferror8),int(ff8),u'\u00B1',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Cos(visible)',round(s9,2),u'\u00B1',round(serror9,2),int(z9),u'\u00B1',int(zerror9),int(f9),u'\u00B1',int(ferror9),int(ff9),u'\u00B1',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Angle(ll-jj)',round(s10,2),u'\u00B1',round(serror10,2),int(z10),u'\u00B1',int(zerror10),int(f10),u'\u00B1',int(ferror10),int(ff10),u'\u00B1',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Mrec(dimuon)',round(s11,2),u'\u00B1',round(serror11,2),int(z11),u'\u00B1',int(zerror11),int(f11),u'\u00B1',int(ferror11),int(ff11),u'\u00B1',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Mrec(dijet)',round(s12,2),u'\u00B1',round(serror12,2),int(z12),u'\u00B1',int(zerror12),int(f12),u'\u00B1',int(ferror12),int(ff12),u'\u00B1',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(visible)',round(s13,2),u'\u00B1',round(serror13,2),int(z13),u'\u00B1',int(zerror13),int(f13),u'\u00B1',int(ferror13),int(ff13),u'\u00B1',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*P(visible)',round(s14,2),u'\u00B1',round(serror14,2),int(z14),u'\u00B1',int(zerror14),int(f14),u'\u00B1',int(ferror14),int(ff14),u'\u00B1',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(visible)',round(s15,2),u'\u00B1',round(serror15,2),int(z15),u'\u00B1',int(zerror15),int(f15),u'\u00B1',int(ferror15),int(ff15),u'\u00B1',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(leading jet)',round(s16,2),u'\u00B1',round(serror16,2),int(z16),u'\u00B1',int(zerror16),int(f16),u'\u00B1',int(ferror16),int(ff16),u'\u00B1',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(leading jet)',round(s17,2),u'\u00B1',round(serror17,2),int(z17),u'\u00B1',int(zerror17),int(f17),u'\u00B1',int(ferror17),int(ff17),u'\u00B1',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(sub-leading jet)',round(s18,2),u'\u00B1',round(serror18,2),int(z18),u'\u00B1',int(zerror18),int(f18),u'\u00B1',int(ferror18),int(ff18),u'\u00B1',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(sub-leading jet)',round(s19,2),u'\u00B1',round(serror19,2),int(z19),u'\u00B1',int(zerror19),int(f19),u'\u00B1',int(ferror19),int(ff19),u'\u00B1',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('not mmhzz',round(s20,2),u'\u00B1',round(serror20,2),int(z20),u'\u00B1',int(zerror20),int(f20),u'\u00B1',int(ferror20),int(ff20),u'\u00B1',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s%-15s"%('not nnhzz',round(s21,2),u'\u00B1',round(serror21,2),int(z21),u'\u00B1',int(zerror21),int(f21),u'\u00B1',int(ferror21),int(ff21),u'\u00B1',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),eff_error))
        if (ZZ_Selection==2):
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(missing)<M(dimuon)',round(s3,2),u'\u00B1',round(serror3,2),int(z3),u'\u00B1',int(zerror3),int(f3),u'\u00B1',int(ferror3),int(ff3),u'\u00B1',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Npfo',round(s4,2),u'\u00B1',round(serror4,2),int(z4),u'\u00B1',int(zerror4),int(f4),u'\u00B1',int(ferror4),int(ff4),u'\u00B1',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dijet)',round(s5,2),u'\u00B1',round(serror5,2),int(z5),u'\u00B1',int(zerror5),int(f5),u'\u00B1',int(ferror5),int(ff5),u'\u00B1',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(dimuon)',round(s6,2),u'\u00B1',round(serror6,2),int(z6),u'\u00B1',int(zerror6),int(f6),u'\u00B1',int(ferror6),int(ff6),u'\u00B1',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(missing)',round(s7,2),u'\u00B1',round(serror7,2),int(z7),u'\u00B1',int(zerror7),int(f7),u'\u00B1',int(ferror7),int(ff7),u'\u00B1',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Cos',round(s8,2),u'\u00B1',round(serror8,2),int(z8),u'\u00B1',int(zerror8),int(f8),u'\u00B1',int(ferror8),int(ff8),u'\u00B1',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Cos(visible)',round(s9,2),u'\u00B1',round(serror9,2),int(z9),u'\u00B1',int(zerror9),int(f9),u'\u00B1',int(ferror9),int(ff9),u'\u00B1',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Angle(ll-jj)',round(s10,2),u'\u00B1',round(serror10,2),int(z10),u'\u00B1',int(zerror10),int(f10),u'\u00B1',int(ferror10),int(ff10),u'\u00B1',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Mrec(dimuon)',round(s11,2),u'\u00B1',round(serror11,2),int(z11),u'\u00B1',int(zerror11),int(f11),u'\u00B1',int(ferror11),int(ff11),u'\u00B1',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('Mrec(dijet)',round(s12,2),u'\u00B1',round(serror12,2),int(z12),u'\u00B1',int(zerror12),int(f12),u'\u00B1',int(ferror12),int(ff12),u'\u00B1',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('M(visible)',round(s13,2),u'\u00B1',round(serror13,2),int(z13),u'\u00B1',int(zerror13),int(f13),u'\u00B1',int(ferror13),int(ff13),u'\u00B1',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*P(visible)',round(s14,2),u'\u00B1',round(serror14,2),int(z14),u'\u00B1',int(zerror14),int(f14),u'\u00B1',int(ferror14),int(ff14),u'\u00B1',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(visible)',round(s15,2),u'\u00B1',round(serror15,2),int(z15),u'\u00B1',int(zerror15),int(f15),u'\u00B1',int(ferror15),int(ff15),u'\u00B1',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(leading jet)',round(s16,2),u'\u00B1',round(serror16,2),int(z16),u'\u00B1',int(zerror16),int(f16),u'\u00B1',int(ferror16),int(ff16),u'\u00B1',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(leading jet)',round(s17,2),u'\u00B1',round(serror17,2),int(z17),u'\u00B1',int(zerror17),int(f17),u'\u00B1',int(ferror17),int(ff17),u'\u00B1',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*E(sub-leading jet)',round(s18,2),u'\u00B1',round(serror18,2),int(z18),u'\u00B1',int(zerror18),int(f18),u'\u00B1',int(ferror18),int(ff18),u'\u00B1',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('*Pt(sub-leading jet)',round(s19,2),u'\u00B1',round(serror19,2),int(z19),u'\u00B1',int(zerror19),int(f19),u'\u00B1',int(ferror19),int(ff19),u'\u00B1',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s"%('not mmhzz',round(s20,2),u'\u00B1',round(serror20,2),int(z20),u'\u00B1',int(zerror20),int(f20),u'\u00B1',int(ferror20),int(ff20),u'\u00B1',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4)))
            print("%-25s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-6s%-1s%-8s%-15s%-15s"%('not nnhzz',round(s21,2),u'\u00B1',round(serror21,2),int(z21),u'\u00B1',int(zerror21),int(f21),u'\u00B1',int(ferror21),int(ff21),u'\u00B1',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),eff_error))
 
    fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('Cut','Signal','ZH Background','2f Background','4f Background','$S\over\sqrt{S+B}$',r'\\ \hline'))
    fout_script.write('%-30s&%-7s%-3s%-5s&%-7s%-3s%-5s&%-9s%-3s%-3s&%-8s%-3s%-4s&%-15s%-5s\n'%('$Expected$',round(s_raw,2),'$\pm$',round(s_raw_error,2),int(z_raw),'$\pm$',int(z_raw_error),int(f_raw),'$\pm$',int(f_raw_error),int(ff_raw),'$\pm$',int(ff_raw_error),'        ',r'\\'))
    fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$Pre-selection$',round(s1,2),'$\pm$',round(serror1,2),int(z1),'$\pm$',int(zerror1),int(f1),'$\pm$',int(ferror1),int(ff1),'$\pm$',int(fferror1),'        ',r'\\'))
    fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$Signal \ or \ not$',round(s2,2),'$\pm$',round(serror2,2),int(z2),'$\pm$',int(zerror2),int(f2),'$\pm$',int(ferror2),int(ff2),'$\pm$',int(fferror2),'        ',r'\\'))

    if (combine_opt==1): # mmHZZ
        if (ZZ_Selection==1): # mmHvvjj
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{missing}>M_{dijet}$',round(s3,2),'$\pm$',round(serror3,2),int(z3),'$\pm$',int(zerror3),int(f3),'$\pm$',int(ferror3),int(ff3),'$\pm$',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$N(pfo)$',round(s4,2),'$\pm$',round(serror4,2),int(z4),'$\pm$',int(zerror4),int(f4),'$\pm$',int(ferror4),int(ff4),'$\pm$',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}$',round(s5,2),'$\pm$',round(serror5,2),int(z5),'$\pm$',int(zerror5),int(f5),'$\pm$',int(ferror5),int(ff5),'$\pm$',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dijet}$',round(s6,2),'$\pm$',round(serror6,2),int(z6),'$\pm$',int(zerror6),int(f6),'$\pm$',int(ferror6),int(ff6),'$\pm$',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{missing}$',round(s7,2),'$\pm$',round(serror7,2),int(z7),'$\pm$',int(zerror7),int(f7),'$\pm$',int(ferror7),int(ff7),'$\pm$',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*cos \ \\theta$',round(s8,2),'$\pm$',round(serror8,2),int(z8),'$\pm$',int(zerror8),int(f8),'$\pm$',int(ferror8),int(ff8),'$\pm$',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',round(s9,2),'$\pm$',round(serror9,2),int(z9),'$\pm$',int(zerror9),int(f9),'$\pm$',int(ferror9),int(ff9),'$\pm$',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$Angle_{\mu j}$',round(s10,2),'$\pm$',round(serror10,2),int(z10),'$\pm$',int(zerror10),int(f10),'$\pm$',int(ferror10),int(ff10),'$\pm$',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}^{rec}$',round(s11,2),'$\pm$',round(serror11,2),int(z11),'$\pm$',int(zerror11),int(f11),'$\pm$',int(ferror11),int(ff11),'$\pm$',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dijet}^{rec}$',round(s12,2),'$\pm$',round(serror12,2),int(z12),'$\pm$',int(zerror12),int(f12),'$\pm$',int(ferror12),int(ff12),'$\pm$',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*M_{visible}$',round(s13,2),'$\pm$',round(serror13,2),int(z13),'$\pm$',int(zerror13),int(f13),'$\pm$',int(ferror13),int(ff13),'$\pm$',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{visible}$',round(s14,2),'$\pm$',round(serror14,2),int(z14),'$\pm$',int(zerror14),int(f14),'$\pm$',int(ferror14),int(ff14),'$\pm$',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',round(s15,2),'$\pm$',round(serror15,2),int(z15),'$\pm$',int(zerror15),int(f15),'$\pm$',int(ferror15),int(ff15),'$\pm$',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',round(s16,2),'$\pm$',round(serror16,2),int(z16),'$\pm$',int(zerror16),int(f16),'$\pm$',int(ferror16),int(ff16),'$\pm$',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',round(s17,2),'$\pm$',round(serror17,2),int(z17),'$\pm$',int(zerror17),int(f17),'$\pm$',int(ferror17),int(ff17),'$\pm$',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',round(s18,2),'$\pm$',round(serror18,2),int(z18),'$\pm$',int(zerror18),int(f18),'$\pm$',int(ferror18),int(ff18),'$\pm$',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',round(s19,2),'$\pm$',round(serror19,2),int(z19),'$\pm$',int(zerror19),int(f19),'$\pm$',int(ferror19),int(ff19),'$\pm$',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$not \ qqHZZ$ ',round(s20,2),'$\pm$',round(serror20,2),int(z20),'$\pm$',int(zerror20),int(f20),'$\pm$',int(ferror20),int(ff20),'$\pm$',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s%-5s\n'%('$not \ \\nu\\nu HZZ$ ',round(s21,2),'$\pm$',round(serror21,2),int(z21),'$\pm$',int(zerror21),int(f21),'$\pm$',int(ferror21),int(ff21),'$\pm$',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),'$\pm$',round(eff_error,4),r'\\'))

        if (ZZ_Selection==2): # mmHjjvv
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{missing}<M_{dijet}$',round(s3,2),'$\pm$',round(serror3,2),int(z3),'$\pm$',int(zerror3),int(f3),'$\pm$',int(ferror3),int(ff3),'$\pm$',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$N(pfo)$',round(s4,2),'$\pm$',round(serror4,2),int(z4),'$\pm$',int(zerror4),int(f4),'$\pm$',int(ferror4),int(ff4),'$\pm$',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}$',round(s5,2),'$\pm$',round(serror5,2),int(z5),'$\pm$',int(zerror5),int(f5),'$\pm$',int(ferror5),int(ff5),'$\pm$',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dijet}$',round(s6,2),'$\pm$',round(serror6,2),int(z6),'$\pm$',int(zerror6),int(f6),'$\pm$',int(ferror6),int(ff6),'$\pm$',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{missing}$',round(s7,2),'$\pm$',round(serror7,2),int(z7),'$\pm$',int(zerror7),int(f7),'$\pm$',int(ferror7),int(ff7),'$\pm$',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*cos \ \\theta$',round(s8,2),'$\pm$',round(serror8,2),int(z8),'$\pm$',int(zerror8),int(f8),'$\pm$',int(ferror8),int(ff8),'$\pm$',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',round(s9,2),'$\pm$',round(serror9,2),int(z9),'$\pm$',int(zerror9),int(f9),'$\pm$',int(ferror9),int(ff9),'$\pm$',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$Angle_{\mu j}$',round(s10,2),'$\pm$',round(serror10,2),int(z10),'$\pm$',int(zerror10),int(f10),'$\pm$',int(ferror10),int(ff10),'$\pm$',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}^{rec}$',round(s11,2),'$\pm$',round(serror11,2),int(z11),'$\pm$',int(zerror11),int(f11),'$\pm$',int(ferror11),int(ff11),'$\pm$',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*M_{dijet}^{rec}$',round(s12,2),'$\pm$',round(serror12,2),int(z12),'$\pm$',int(zerror12),int(f12),'$\pm$',int(ferror12),int(ff12),'$\pm$',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{visible}$',round(s13,2),'$\pm$',round(serror13,2),int(z13),'$\pm$',int(zerror13),int(f13),'$\pm$',int(ferror13),int(ff13),'$\pm$',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{visible}$',round(s14,2),'$\pm$',round(serror14,2),int(z14),'$\pm$',int(zerror14),int(f14),'$\pm$',int(ferror14),int(ff14),'$\pm$',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',round(s15,2),'$\pm$',round(serror15,2),int(z15),'$\pm$',int(zerror15),int(f15),'$\pm$',int(ferror15),int(ff15),'$\pm$',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',round(s16,2),'$\pm$',round(serror16,2),int(z16),'$\pm$',int(zerror16),int(f16),'$\pm$',int(ferror16),int(ff16),'$\pm$',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',round(s17,2),'$\pm$',round(serror17,2),int(z17),'$\pm$',int(zerror17),int(f17),'$\pm$',int(ferror17),int(ff17),'$\pm$',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',round(s18,2),'$\pm$',round(serror18,2),int(z18),'$\pm$',int(zerror18),int(f18),'$\pm$',int(ferror18),int(ff18),'$\pm$',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',round(s19,2),'$\pm$',round(serror19,2),int(z19),'$\pm$',int(zerror19),int(f19),'$\pm$',int(ferror19),int(ff19),'$\pm$',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$not \ qqHZZ$ ',round(s20,2),'$\pm$',round(serror20,2),int(z20),'$\pm$',int(zerror20),int(f20),'$\pm$',int(ferror20),int(ff20),'$\pm$',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s%-5s\n'%('$not \ \\nu\\nu HZZ$ ',round(s21,2),'$\pm$',round(serror21,2),int(z21),'$\pm$',int(zerror21),int(f21),'$\pm$',int(ferror21),int(ff21),'$\pm$',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),'$\pm$',round(eff_error,4),r'\\'))

    if (combine_opt==2): # vvHZZ
        if (ZZ_Selection==1): # vvHmmjj
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}>M_{dijet}$',round(s3,2),'$\pm$',round(serror3,2),int(z3),'$\pm$',int(zerror3),int(f3),'$\pm$',int(ferror3),int(ff3),'$\pm$',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$N(pfo)$',round(s4,2),'$\pm$',round(serror4,2),int(z4),'$\pm$',int(zerror4),int(f4),'$\pm$',int(ferror4),int(ff4),'$\pm$',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{missing}$',round(s5,2),'$\pm$',round(serror5,2),int(z5),'$\pm$',int(zerror5),int(f5),'$\pm$',int(ferror5),int(ff5),'$\pm$',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}$',round(s6,2),'$\pm$',round(serror6,2),int(z6),'$\pm$',int(zerror6),int(f6),'$\pm$',int(ferror6),int(ff6),'$\pm$',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dijet}$',round(s7,2),'$\pm$',round(serror7,2),int(z7),'$\pm$',int(zerror7),int(f7),'$\pm$',int(ferror7),int(ff7),'$\pm$',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*cos \ \\theta$',round(s8,2),'$\pm$',round(serror8,2),int(z8),'$\pm$',int(zerror8),int(f8),'$\pm$',int(ferror8),int(ff8),'$\pm$',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',round(s9,2),'$\pm$',round(serror9,2),int(z9),'$\pm$',int(zerror9),int(f9),'$\pm$',int(ferror9),int(ff9),'$\pm$',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$Angle_{\mu j}$',round(s10,2),'$\pm$',round(serror10,2),int(z10),'$\pm$',int(zerror10),int(f10),'$\pm$',int(ferror10),int(ff10),'$\pm$',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*M_{dimuon}^{rec}$',round(s11,2),'$\pm$',round(serror11,2),int(z11),'$\pm$',int(zerror11),int(f11),'$\pm$',int(ferror11),int(ff11),'$\pm$',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*M_{dijet}^{rec}$',round(s12,2),'$\pm$',round(serror12,2),int(z12),'$\pm$',int(zerror12),int(f12),'$\pm$',int(ferror12),int(ff12),'$\pm$',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{visible}$',round(s13,2),'$\pm$',round(serror13,2),int(z13),'$\pm$',int(zerror13),int(f13),'$\pm$',int(ferror13),int(ff13),'$\pm$',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{visible}$',round(s14,2),'$\pm$',round(serror14,2),int(z14),'$\pm$',int(zerror14),int(f14),'$\pm$',int(ferror14),int(ff14),'$\pm$',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',round(s15,2),'$\pm$',round(serror15,2),int(z15),'$\pm$',int(zerror15),int(f15),'$\pm$',int(ferror15),int(ff15),'$\pm$',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',round(s16,2),'$\pm$',round(serror16,2),int(z16),'$\pm$',int(zerror16),int(f16),'$\pm$',int(ferror16),int(ff16),'$\pm$',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',round(s17,2),'$\pm$',round(serror17,2),int(z17),'$\pm$',int(zerror17),int(f17),'$\pm$',int(ferror17),int(ff17),'$\pm$',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',round(s18,2),'$\pm$',round(serror18,2),int(z18),'$\pm$',int(zerror18),int(f18),'$\pm$',int(ferror18),int(ff18),'$\pm$',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',round(s19,2),'$\pm$',round(serror19,2),int(z19),'$\pm$',int(zerror19),int(f19),'$\pm$',int(ferror19),int(ff19),'$\pm$',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$not \ \mu^{+}\mu^{-}HZZ$ ',round(s20,2),'$\pm$',round(serror20,2),int(z20),'$\pm$',int(zerror20),int(f20),'$\pm$',int(ferror20),int(ff20),'$\pm$',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s%-5s\n'%('$not \ qqHZZ$ ',round(s21,2),'$\pm$',round(serror21,2),int(z21),'$\pm$',int(zerror21),int(f21),'$\pm$',int(ferror21),int(ff21),'$\pm$',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),'$\pm$',round(eff_error,4),r'\\'))

        if (ZZ_Selection==2): # vvHjjmm
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}<M_{dijet}$',round(s3,2),'$\pm$',round(serror3,2),int(z3),'$\pm$',int(zerror3),int(f3),'$\pm$',int(ferror3),int(ff3),'$\pm$',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$N(pfo)$',round(s4,2),'$\pm$',round(serror4,2),int(z4),'$\pm$',int(zerror4),int(f4),'$\pm$',int(ferror4),int(ff4),'$\pm$',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{missing}$',round(s5,2),'$\pm$',round(serror5,2),int(z5),'$\pm$',int(zerror5),int(f5),'$\pm$',int(ferror5),int(ff5),'$\pm$',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}$',round(s6,2),'$\pm$',round(serror6,2),int(z6),'$\pm$',int(zerror6),int(f6),'$\pm$',int(ferror6),int(ff6),'$\pm$',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dijet}$',round(s7,2),'$\pm$',round(serror7,2),int(z7),'$\pm$',int(zerror7),int(f7),'$\pm$',int(ferror7),int(ff7),'$\pm$',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*cos \ \\theta$',round(s8,2),'$\pm$',round(serror8,2),int(z8),'$\pm$',int(zerror8),int(f8),'$\pm$',int(ferror8),int(ff8),'$\pm$',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',round(s9,2),'$\pm$',round(serror9,2),int(z9),'$\pm$',int(zerror9),int(f9),'$\pm$',int(ferror9),int(ff9),'$\pm$',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$Angle_{\mu j}$',round(s10,2),'$\pm$',round(serror10,2),int(z10),'$\pm$',int(zerror10),int(f10),'$\pm$',int(ferror10),int(ff10),'$\pm$',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}^{rec}$',round(s11,2),'$\pm$',round(serror11,2),int(z11),'$\pm$',int(zerror11),int(f11),'$\pm$',int(ferror11),int(ff11),'$\pm$',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*M_{dijet}^{rec}$',round(s12,2),'$\pm$',round(serror12,2),int(z12),'$\pm$',int(zerror12),int(f12),'$\pm$',int(ferror12),int(ff12),'$\pm$',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{visible}$',round(s13,2),'$\pm$',round(serror13,2),int(z13),'$\pm$',int(zerror13),int(f13),'$\pm$',int(ferror13),int(ff13),'$\pm$',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{visible}$',round(s14,2),'$\pm$',round(serror14,2),int(z14),'$\pm$',int(zerror14),int(f14),'$\pm$',int(ferror14),int(ff14),'$\pm$',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',round(s15,2),'$\pm$',round(serror15,2),int(z15),'$\pm$',int(zerror15),int(f15),'$\pm$',int(ferror15),int(ff15),'$\pm$',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',round(s16,2),'$\pm$',round(serror16,2),int(z16),'$\pm$',int(zerror16),int(f16),'$\pm$',int(ferror16),int(ff16),'$\pm$',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',round(s17,2),'$\pm$',round(serror17,2),int(z17),'$\pm$',int(zerror17),int(f17),'$\pm$',int(ferror17),int(ff17),'$\pm$',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',round(s18,2),'$\pm$',round(serror18,2),int(z18),'$\pm$',int(zerror18),int(f18),'$\pm$',int(ferror18),int(ff18),'$\pm$',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',round(s19,2),'$\pm$',round(serror19,2),int(z19),'$\pm$',int(zerror19),int(f19),'$\pm$',int(ferror19),int(ff19),'$\pm$',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$not \ \mu^{+}\mu^{-}HZZ$ ',round(s20,2),'$\pm$',round(serror20,2),int(z20),'$\pm$',int(zerror20),int(f20),'$\pm$',int(ferror20),int(ff20),'$\pm$',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s%-5s\n'%('$not \ qqHZZ$ ',round(s21,2),'$\pm$',round(serror21,2),int(z21),'$\pm$',int(zerror21),int(f21),'$\pm$',int(ferror21),int(ff21),'$\pm$',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),'$\pm$',round(eff_error,4),r'\\'))

    if (combine_opt==3): # qqHZZ
        if (ZZ_Selection==1): # qqHvvmm
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{missing}>M_{dimuon}$',round(s3,2),'$\pm$',round(serror3,2),int(z3),'$\pm$',int(zerror3),int(f3),'$\pm$',int(ferror3),int(ff3),'$\pm$',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$N(pfo)$',round(s4,2),'$\pm$',round(serror4,2),int(z4),'$\pm$',int(zerror4),int(f4),'$\pm$',int(ferror4),int(ff4),'$\pm$',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dijet}$',round(s5,2),'$\pm$',round(serror5,2),int(z5),'$\pm$',int(zerror5),int(f5),'$\pm$',int(ferror5),int(ff5),'$\pm$',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}$',round(s6,2),'$\pm$',round(serror6,2),int(z6),'$\pm$',int(zerror6),int(f6),'$\pm$',int(ferror6),int(ff6),'$\pm$',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{missing}$',round(s7,2),'$\pm$',round(serror7,2),int(z7),'$\pm$',int(zerror7),int(f7),'$\pm$',int(ferror7),int(ff7),'$\pm$',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*cos \ \\theta$',round(s8,2),'$\pm$',round(serror8,2),int(z8),'$\pm$',int(zerror8),int(f8),'$\pm$',int(ferror8),int(ff8),'$\pm$',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',round(s9,2),'$\pm$',round(serror9,2),int(z9),'$\pm$',int(zerror9),int(f9),'$\pm$',int(ferror9),int(ff9),'$\pm$',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*Angle_{\mu j}$',round(s10,2),'$\pm$',round(serror10,2),int(z10),'$\pm$',int(zerror10),int(f10),'$\pm$',int(ferror10),int(ff10),'$\pm$',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}^{rec}$',round(s11,2),'$\pm$',round(serror11,2),int(z11),'$\pm$',int(zerror11),int(f11),'$\pm$',int(ferror11),int(ff11),'$\pm$',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dijet}^{rec}$',round(s12,2),'$\pm$',round(serror12,2),int(z12),'$\pm$',int(zerror12),int(f12),'$\pm$',int(ferror12),int(ff12),'$\pm$',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{visible}$',round(s13,2),'$\pm$',round(serror13,2),int(z13),'$\pm$',int(zerror13),int(f13),'$\pm$',int(ferror13),int(ff13),'$\pm$',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{visible}$',round(s14,2),'$\pm$',round(serror14,2),int(z14),'$\pm$',int(zerror14),int(f14),'$\pm$',int(ferror14),int(ff14),'$\pm$',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',round(s15,2),'$\pm$',round(serror15,2),int(z15),'$\pm$',int(zerror15),int(f15),'$\pm$',int(ferror15),int(ff15),'$\pm$',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',round(s16,2),'$\pm$',round(serror16,2),int(z16),'$\pm$',int(zerror16),int(f16),'$\pm$',int(ferror16),int(ff16),'$\pm$',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',round(s17,2),'$\pm$',round(serror17,2),int(z17),'$\pm$',int(zerror17),int(f17),'$\pm$',int(ferror17),int(ff17),'$\pm$',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',round(s18,2),'$\pm$',round(serror18,2),int(z18),'$\pm$',int(zerror18),int(f18),'$\pm$',int(ferror18),int(ff18),'$\pm$',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',round(s19,2),'$\pm$',round(serror19,2),int(z19),'$\pm$',int(zerror19),int(f19),'$\pm$',int(ferror19),int(ff19),'$\pm$',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$not \ \mu^{+}\mu^{-}HZZ$ ',round(s20,2),'$\pm$',round(serror20,2),int(z20),'$\pm$',int(zerror20),int(f20),'$\pm$',int(ferror20),int(ff20),'$\pm$',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s%-5s\n'%('$not \ \\nu \\nu HZZ$ ',round(s21,2),'$\pm$',round(serror21,2),int(z21),'$\pm$',int(zerror21),int(f21),'$\pm$',int(ferror21),int(ff21),'$\pm$',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),'$\pm$',round(eff_error,4),r'\\'))

        if (ZZ_Selection==2): # qqHmmvv
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{missing}<M_{dimuon}$',round(s3,2),'$\pm$',round(serror3,2),int(z3),'$\pm$',int(zerror3),int(f3),'$\pm$',int(ferror3),int(ff3),'$\pm$',int(fferror3),round(s3/math.sqrt(s3+z3+f3+ff3),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$N(pfo)$',round(s4,2),'$\pm$',round(serror4,2),int(z4),'$\pm$',int(zerror4),int(f4),'$\pm$',int(ferror4),int(ff4),'$\pm$',int(fferror4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dijet}$',round(s5,2),'$\pm$',round(serror5,2),int(z5),'$\pm$',int(zerror5),int(f5),'$\pm$',int(ferror5),int(ff5),'$\pm$',int(fferror5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}$',round(s6,2),'$\pm$',round(serror6,2),int(z6),'$\pm$',int(zerror6),int(f6),'$\pm$',int(ferror6),int(ff6),'$\pm$',int(fferror6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{missing}$',round(s7,2),'$\pm$',round(serror7,2),int(z7),'$\pm$',int(zerror7),int(f7),'$\pm$',int(ferror7),int(ff7),'$\pm$',int(fferror7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*cos \ \\theta$',round(s8,2),'$\pm$',round(serror8,2),int(z8),'$\pm$',int(zerror8),int(f8),'$\pm$',int(ferror8),int(ff8),'$\pm$',int(fferror8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$cos \\theta_{visible} $ ',round(s9,2),'$\pm$',round(serror9,2),int(z9),'$\pm$',int(zerror9),int(f9),'$\pm$',int(ferror9),int(ff9),'$\pm$',int(fferror9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$Angle_{\mu j}$',round(s10,2),'$\pm$',round(serror10,2),int(z10),'$\pm$',int(zerror10),int(f10),'$\pm$',int(ferror10),int(ff10),'$\pm$',int(fferror10),round(s10/math.sqrt(s10+z10+f10+ff10),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dimuon}^{rec}$',round(s11,2),'$\pm$',round(serror11,2),int(z11),'$\pm$',int(zerror11),int(f11),'$\pm$',int(ferror11),int(ff11),'$\pm$',int(fferror11),round(s11/math.sqrt(s11+z11+f11+ff11),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{dijet}^{rec}$',round(s12,2),'$\pm$',round(serror12,2),int(z12),'$\pm$',int(zerror12),int(f12),'$\pm$',int(ferror12),int(ff12),'$\pm$',int(fferror12),round(s12/math.sqrt(s12+z12+f12+ff12),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$M_{visible}$',round(s13,2),'$\pm$',round(serror13,2),int(z13),'$\pm$',int(zerror13),int(f13),'$\pm$',int(ferror13),int(ff13),'$\pm$',int(fferror13),round(s13/math.sqrt(s13+z13+f13+ff13),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{visible}$',round(s14,2),'$\pm$',round(serror14,2),int(z14),'$\pm$',int(zerror14),int(f14),'$\pm$',int(ferror14),int(ff14),'$\pm$',int(fferror14),round(s14/math.sqrt(s14+z14+f14+ff14),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{visible}}$ ',round(s15,2),'$\pm$',round(serror15,2),int(z15),'$\pm$',int(zerror15),int(f15),'$\pm$',int(ferror15),int(ff15),'$\pm$',int(fferror15),round(s15/math.sqrt(s15+z15+f15+ff15),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{leading \ jet}$ ',round(s16,2),'$\pm$',round(serror16,2),int(z16),'$\pm$',int(zerror16),int(f16),'$\pm$',int(ferror16),int(ff16),'$\pm$',int(fferror16),round(s16/math.sqrt(s16+z16+f16+ff16),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{leading \ jet}}$ ',round(s17,2),'$\pm$',round(serror17,2),int(z17),'$\pm$',int(zerror17),int(f17),'$\pm$',int(ferror17),int(ff17),'$\pm$',int(fferror17),round(s17/math.sqrt(s17+z17+f17+ff17),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*E_{sub-leading \ jet}$ ',round(s18,2),'$\pm$',round(serror18,2),int(z18),'$\pm$',int(zerror18),int(f18),'$\pm$',int(ferror18),int(ff18),'$\pm$',int(fferror18),round(s18/math.sqrt(s18+z18+f18+ff18),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$*P_{T_{sub-leading \ jet}}$ ',round(s19,2),'$\pm$',round(serror19,2),int(z19),'$\pm$',int(zerror19),int(f19),'$\pm$',int(ferror19),int(ff19),'$\pm$',int(fferror19),round(s19/math.sqrt(s19+z19+f19+ff19),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-15s%-5s\n'%('$not \ \mu^{+}\mu^{-}HZZ$ ',round(s20,2),'$\pm$',round(serror20,2),int(z20),'$\pm$',int(zerror20),int(f20),'$\pm$',int(ferror20),int(ff20),'$\pm$',int(fferror20),round(s20/math.sqrt(s20+z20+f20+ff20),4),r'\\'))
            fout_script.write('%-30s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s&%-6s%-3s%-6s%-5s\n'%('$not \ \\nu \\nu HZZ$ ',round(s21,2),'$\pm$',round(serror21,2),int(z21),'$\pm$',int(zerror21),int(f21),'$\pm$',int(ferror21),int(ff21),'$\pm$',int(fferror21),round(s21/math.sqrt(s21+z21+f21+ff21),4),'$\pm$',round(eff_error,4),r'\\'))
    fout_script.close()
    
if __name__ == '__main__':
    main()
