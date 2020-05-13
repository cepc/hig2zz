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


def main():

    combine_opt = int(sys.argv[1])
    flag_zz = int(sys.argv[2])
    tabs = sys.argv[3:]

    signal_path = './run/'
    save_path = './table/'
    if (combine_opt==1):
        signal_path += 'channel_ll_'
        signal_path += str(flag_zz)
        signal_path += '/llh2zz'
        save_path += 'channel_ll_'
        save_path += str(flag_zz)
    if (combine_opt==2):
        signal_path += 'channel_nn_'
	signal_path += str(flag_zz)
        signal_path += '/nnh2zz'
        save_path += 'channel_nn_'
	save_path += str(flag_zz)
    if (combine_opt==3):
        signal_path += 'channel_qq_'
        signal_path += str(flag_zz)
        signal_path += '/qqh2zz'
        save_path += 'channel_qq_'
        save_path += str(flag_zz)
    signal_path += '/hist/'

    signal_sample =  ROOT.TFile(signal_path+'ana_File_merged_1.root')

    evah = signal_sample.Get('hevtflw_sel')
    eva = evah.GetBinContent(1)  #number of mmHZZ
    if (combine_opt == 1):
        xsec = 6.77
    if (combine_opt == 2):
        xsec = 46.3
    if (combine_opt == 3):
        xsec = 137
    scs = 5600 * xsec * 0.0264 / eva
    print('scale for signal is %s'%scs)

    s_raw = evah.GetBinContent(1) * scs

    for i in range(15):
        exec ("s%s = evah.GetBinContent(%s) * scs"%(i+1,i+1))

    for i in range(15):
        exec ("z%s = 0"%(i+1))
        exec ("f%s = 0"%(i+1))
        exec ("ff%s = 0"%(i+1))
    
    z_raw = 0
    f_raw = 0
    ff_raw = 0

    print("%-25s%-25s%-25s"%('name','scale','final'))

    outname = save_path + '/cut_info.txt'
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
                event_exp = 5600.0 / 5050.0 * float(l[3])

		if (combine_opt==1):
	            bg_path = 'channel_ll_' + str(flag_zz) + '/'
	        if (combine_opt==2):
	            bg_path = 'channel_nn_' + str(flag_zz) + '/'
	        if (combine_opt==3):
	            bg_path = 'channel_qq_' + str(flag_zz) + '/'

                sample = ROOT.TFile('./run/' + bg_path + path + '/hist/' + dname + '/ana_File_merged_1.root')
                h=sample.Get('hevtflw_sel')
                event_ana = h.GetBinContent(1)

                if event_ana != 0:
                    scb = (event_exp / event_ana)

                    tep = sample.Get('hevtflw_sel')

                    if (combine_opt==1):
		        evt = tep.GetBinContent(9) * scb
		    if (combine_opt==2):
			evt = tep.GetBinContent(9) * scb
		    if (combine_opt==3):
			evt = tep.GetBinContent(9) * scb

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

                    for i in range(10):
                        exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+1))

                        if tabs.index(t) == 0:
                            exec ("z%s += cut%s"%(i+1,i+1))

                        if tabs.index(t) == 1:
                            exec ("f%s += cut%s"%(i+1,i+1))

                        if tabs.index(t) == 2:
                            exec ("ff%s += cut%s"%(i+1,i+1))

    print('\n')
    print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cut','llhzz','ZH','2f','4f','S/sqrt(S+B)'))
    print("%-25s%-15s%-15s%-15s%-15s"%('Expected',int(s_raw),int(z_raw),int(f_raw),int(ff_raw)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Pre-selection',int(s2),int(z2),int(f2),int(ff2)))
    print("%-25s%-15s%-15s%-15s%-15s"%('Is signal',int(s3),int(z3),int(f3),int(ff3)))

    if (combine_opt == 1):
	if (flag_zz == 1):
	    print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Miss Mass>Dijet Mass',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
	if (flag_zz == 2):
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Miss Mass<Dijet Mass',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))

	print("%-25s%-15s%-15s%-15s%-15s%-15s"%('N(pfo)',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
	print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dimuon)',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
	print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Mrec(Dimuon)',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
	print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cos(visible)',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
	print("%-25s%-15s%-15s%-15s%-15s%-15s"%('BDT',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))
 
    if (combine_opt == 2):
        if (flag_zz == 1):
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Dimuon Mass>Dijet Mass',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
        if (flag_zz == 2):
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Dimuon Mass<Dijet Mass',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))

        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('N(pfo)',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(missing)',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(visible)',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cos(visible)',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('BDT',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))

    if (combine_opt == 3):
        if (flag_zz == 1):
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Missing Mass>Dimuon Mass',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))
        if (flag_zz == 2):
            print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Missing Mass<Dimuon Mass',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4)))

        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('N(pfo)',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4)))
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('M(dijet)',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4)))
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Mrec(dijet)',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4)))
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('Cos(visible)',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4)))
        print("%-25s%-15s%-15s%-15s%-15s%-15s"%('BDT',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4)))

    fout_script.write('    \hline \hline \n')
    fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('Cut','Signal','ZH Background','2f Background','4f Background','$S\over\sqrt{S+B}$',r'\\ \hline'))
    fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$Expected$',int(s_raw),int(z_raw),int(f_raw),int(ff_raw),'        ',r'\\'))
    fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$Pre-selection$',int(s2),int(z2),int(f2),int(ff2),'        ',r'\\'))
    fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$Signal \ or \ not$',int(s3),int(z3),int(f3),int(ff3),'        ',r'\\'))

    if (combine_opt == 1):
        if (flag_zz == 1):
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}>M_{dijet}$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
	if (flag_zz == 2):
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}<M_{dijet}$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))

        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$N(pfo)$',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}$',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}^{rec}$',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$cos \\theta_{visible}$',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$BDT \ score$ ',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))

    if (combine_opt == 2):
        if (flag_zz == 1):
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}>M_{dijet}$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
        if (flag_zz == 2):
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dimuon}<M_{dijet}$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))

        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$N(pfo)$',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}$',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{visible}$',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$cos \\theta_{visible}$',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$BDT \ score$ ',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))

    if (combine_opt == 3):
        if (flag_zz == 1):
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}>M_{dimuon}$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))
        if (flag_zz == 2):
            fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{missing}<M_{dimuon}$',int(s4),int(z4),int(f4),int(ff4),round(s4/math.sqrt(s4+z4+f4+ff4),4),r'\\'))

        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$N(pfo)$',int(s5),int(z5),int(f5),int(ff5),round(s5/math.sqrt(s5+z5+f5+ff5),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dijet}$',int(s6),int(z6),int(f6),int(ff6),round(s6/math.sqrt(s6+z6+f6+ff6),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$M_{dijet}^{rec}$',int(s7),int(z7),int(f7),int(ff7),round(s7/math.sqrt(s7+z7+f7+ff7),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$cos \\theta_{visible}$',int(s8),int(z8),int(f8),int(ff8),round(s8/math.sqrt(s8+z8+f8+ff8),4),r'\\'))
        fout_script.write('%-30s&%-15s&%-15s&%-15s&%-15s&%-15s%-5s\n'%('$BDT \ score$ ',int(s9),int(z9),int(f9),int(ff9),round(s9/math.sqrt(s9+z9+f9+ff9),4),r'\\'))

    fout_script.close()
    
if __name__ == '__main__':
    main()
