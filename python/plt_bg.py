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
 
    draw_signal_bg('h_m_dimuon',0 , 210, 1)
    draw_signal_bg('h_mrec_dimuon',50 ,160, 1)
    draw_signal_bg('h_npfo', 0, 100, 1)
    draw_signal_bg('h_vis_all_pt', 0, 30, 1)
    draw_signal_bg('h_min_angle',0,120, 1)
    draw_signal_bg('h_m_dijet', 0, 160, 1)
    draw_signal_bg('h_n_lepton', 0, 10,0)
    draw_signal_bg('h_mrec_dimuon_final',110,150,0) 
    draw_2d('h_2D_visible_missing')  

    #hvvjj
    draw_signal_bg('h_single_jet1_pt',0,40,1)
    draw_signal_bg('h_single_jet2_pt',0,40,1)
    draw_signal_bg('h_single_jet1_e',0,50,1)
    draw_signal_bg('h_single_jet2_e',0,40,1)
    draw_signal_bg('h_single_jet_theta',0,180,1)  

    #hjjvv
    # draw_signal_bg('h_single_jet1_pt',0,100,1)
    # draw_signal_bg('h_single_jet2_pt',0,100,1)
    # draw_signal_bg('h_single_jet1_e',0,100,1)
    # draw_signal_bg('h_single_jet2_e',0,120,1)
    # draw_signal_bg('h_single_jet_theta',0,180,1)

def draw_signal_bg(pic, x1, x2, log):

    tabs = sys.argv[1:]

    leg = ROOT.TLegend(0.7, 0.71, 0.9, 0.91)
    c = ROOT.TCanvas('c', 'c', 1600, 1600)

    figfile = './fig/sbg_%s.pdf'%pic
    check_outfile_path(figfile)

    signal_sample =  ROOT.TFile('./run/llh2zz/hist/ana_File_merged_1.root')

    evah = signal_sample.Get('hevtflw_sel')
    eva = evah.GetBinContent(3)  #number of e2e2hvvjj
    scs = 5600 * 6.77 * 0.0264 * 0.2 * 0.69 / eva
    s = signal_sample.Get(pic)
    s.Scale(scs)

    for t in tabs: 

        tab = open(t , 'r' )
        name = t.split('/')[-1]
        exec('b%s = copy.copy(s)'%tabs.index(t))
        exec('b%s.Scale(0)'%tabs.index(t))
        
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
                    tem=sample.Get(pic)
                    a=copy.copy(tem)
                    a.Scale(scb)
                    exec('b%s.Add(a)'%tabs.index(t))

        if tabs.index(t) == 0:  

            ROOT.gPad.SetLogy(log)
            b0.SetMinimum(0.1)
            if pic == 'h_n_lepton' or pic == 'h_mrec_dimuon_final':
                b0.SetMaximum(30)
            b0.GetXaxis().SetRangeUser(x1, x2)
            b0.SetXTitle('%s'%pic)
            b0.SetYTitle('Number of events') 
            b0.SetLineColor(40)
            b0.Draw()
            leg.AddEntry(b0, name)
            leg.Draw()


        if tabs.index(t) == 1:  

            b1.SetLineColor(41)
            b1.Draw('same')
            leg.AddEntry(b1, name)
            leg.Draw()

    zh = './table/bg_zh.txt'
    zhtab = open(zh , 'r' )

    i = 1
    for s_line in zhtab :

        if not s_line.startswith('#'):
            l = [x.strip() for x in s_line.split(',')]
            dname = l[0]
            event_exp = 1.11 * float(l[3])
            sample = ROOT.TFile('./run/bg/hist/' + dname + '/ana_File_merged_1.root')
            h=sample.Get('hevtflw_pre')
            event_ana = h.GetBinContent(1)

            if event_ana != 0:
                scb = (event_exp / event_ana)
                tem=sample.Get(pic)
                exec('zh%s = copy.copy(tem)'%i)
                exec('zh%s.Scale(scb)'%i)
                exec('zh%s.SetLineColor(%s)'%(i,i+2))
                exec("zh%s.Draw('same')"%i)
                exec('leg.AddEntry(zh%s, dname)'%i)
                leg.Draw()
                i = i + 1

    s.SetLineColor(ROOT.kRed)
    s.Draw('same')
    leg.AddEntry(s, "signal")
    leg.Draw()

    c.SaveAs(figfile)

def draw_2d(pic):

    c = ROOT.TCanvas('c', 'c', 1600, 1600)

    figfile = './fig/2d_%s.pdf'%pic
    check_outfile_path(figfile)

    sample =  ROOT.TFile('./run/llh2zz/hist/ana_File_merged_1.root')
    # sample =  ROOT.TFile('run/zh/hist/e2e2h_X/ana_File_merged_1.root')
    # sample =  ROOT.TFile('run/bg/hist/zz_sl0mu_down/ana_File_merged_1.root')

    s = sample.Get(pic)

    s.SetXTitle('dijet mass')
    s.SetYTitle('missing mass') 

    s.SetContour(99)
    s.Draw("colz")
    c.SaveAs(figfile)

if __name__ == '__main__':
    main()