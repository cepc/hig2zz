#!/usr/bin/env python
"""
Plot signal-bg histograms 
"""

__author__ = "Kong Lingteng <konglingteng15@mails.ucas.ac.cn>"
__copyright__ = "Copyright (c) Kong Lingteng"
__created__ = "[2018-09-26 Wed 10:53]" 

import sys,os,copy
import ROOT 
from tools import check_outfile_path, set_root_style


def main():
 
    draw_fit('h_mrec_dimuon_final',110,150) 


def draw_fit(pic, x1, x2):

    tabs = sys.argv[1:]

    leg = ROOT.TLegend(0.7, 0.71, 0.9, 0.91)
    c = ROOT.TCanvas('c', 'c', 1600, 1600)

    figfile = './doc/fig/fit_%s.pdf'%pic
    check_outfile_path(figfile)

    signal_sample =  ROOT.TFile('./run/llh2zz/hist/ana_File_merged_1.root')

    evah = signal_sample.Get('hevtflw_pre')
    eva = evah.GetBinContent(1)
    scs = 5050 * 6.77 * 0.0266 / (eva * (6.77 / (7.04 + 6.77 + 6.75)))
    s = signal_sample.Get(pic)
    s.Scale(scs)
    s.GetXaxis().SetRangeUser(x1, x2)
    
    b = copy.copy(s)

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
                    tem=sample.Get(pic)
                    a=copy.copy(tem)
                    a.Scale(scb)
                    b.Add(a)



    s.SetLineColor(ROOT.kRed)
    b.SetLineColor(ROOT.kBlue)
    b.SetMarkerStyle(3)

    s.Fit("gaus")
    b.Fit("gaus")

    b.Draw('P')
    s.Draw('same')
    
    # leg.AddEntry(s, "signal")
    # leg.Draw()
    # leg.AddEntry(b, "background")
    # leg.Draw()

    c.SaveAs(figfile)

if __name__ == '__main__':
    main()