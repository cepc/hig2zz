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
 
    draw_signal_bg('h_m_dimuon')
    draw_signal_bg('h_mrec_dimuon')
    draw_signal_bg('h_npfo')
    draw_signal_bg('h_vis_all_pt')
    draw_signal_bg('h_min_angle')
    draw_signal_bg('h_m_dijet')
    draw_signal_bg('h_single_jet1_pt')
    draw_signal_bg('h_single_jet2_pt')
    draw_signal_bg('h_single_jet1_e')
    draw_signal_bg('h_single_jet2_e')
    draw_signal_bg('h_single_jet_theta')
    draw_signal_bg('h_n_lepton')
    draw_signal_bg('h_m_dimuon_final')     

def draw_signal_bg(pic):

    path = sys.argv[1]
    tabs = sys.argv[2:]

    leg = ROOT.TLegend(0.7, 0.71, 0.9, 0.91)
    c = ROOT.TCanvas('c', 'c', 1600, 1600)

    figfile = './doc/fig/sbg_%s.pdf'%pic
    check_outfile_path(figfile)

    signal_sample =  ROOT.TFile('./run/llh2zz/hist/ana_File_merged_1.root')

    evah = signal_sample.Get('hevtflw_pre')
    eva = evah.GetBinContent(1)
    scs = 5050 * 6.77 * 0.0266 / (eva * (6.77 / (7.04 + 6.77 + 6.75)))

    s = signal_sample.Get(pic)
    s.Scale(scs)
    for t in tabs: 

        tab = open(t , 'r' )
        exec('b%s = copy.copy(s)'%tabs.index(t))
        
        for s_line in tab :
            if not s_line.startswith('#'):
                l = [x.strip() for x in s_line.split(',')]
                dname = l[0]
                event_exp = float(l[3])
                sample = ROOT.TFile('./run' + '/' + path + '/hist' + '/' + dname + '/' + 'ana_File_merged_1.root')
                h=sample.Get('hevtflw_pre')
                event_ana = h.GetBinContent(1)

                if event_ana != 0:
                    scb = (event_exp / event_ana)
                    tem=sample.Get(pic)
                    a=copy.copy(tem)
                    a.Scale(scb)
                    exec('b%s.Add(a)'%tabs.index(t))

        if tabs.index(t) == 0:

            b0.SetLineColor(ROOT.kBlue)
            b0.Draw()
            leg.AddEntry(b0, 'ZH backgroung')
            leg.Draw()


        if tabs.index(t) == 1:

            b1.SetLineColor(ROOT.kGreen)
            b1.Draw('same')
            leg.AddEntry(b1, '2f background')
            leg.Draw()

        if tabs.index(t) == 2:

            b2.SetLineColor(ROOT.kYellow)
            b2.Draw('same')
            leg.AddEntry(b2, '4f background')
            leg.Draw()
    

    s.SetLineColor(ROOT.kRed)
    s.Draw('same')
    leg.AddEntry(s, "signal")
    leg.Draw()

    c.SaveAs(figfile)


if __name__ == '__main__':
    main()
