#!/usr/bin/env python
"""
Plot signal-bg histograms 
"""

__author__ = "Kong Lingteng <konglingteng15@mails.ucas.ac.cn>"
__copyright__ = "Copyright (c) Kong Lingteng"
__created__ = "[2018-09-26 Wed 10:53]" 

import sys,os,copy
import ROOT 
from tools import check_outfile_path


def main():

    opt = int(sys.argv[1])

    draw_signal_bg('h_m_dimuon',0 , 210, 'Dimuon mass (GeV)')
    draw_signal_bg('h_mrec_dimuon',50 ,160, 'Dimuon rec mass (GeV)')
    draw_signal_bg('h_vis_all_pt', 0, 100, 'Transverse momentum (GeV)')
    draw_signal_bg('h_min_angle',0, 120, 'Muon-jet angle (degree)')
    draw_signal_bg('h_single_jet_theta',0,180, 'Two jet angle (degree)')  
    draw_signal_bg('h_mrec_dimuon_final',110,150, 'Dimuon rec mass (GeV)') 
    draw_2d('h_2D_dijet_missing')
    draw_2d('h_2D_dijet_missing_raw')  

    if opt == 1: 
        print('plotting hvvjj channel...')
        draw_signal_bg('h_npfo', 0, 100, 'Particle flow object')
        draw_signal_bg('h_single_jet1_pt',0,50, 'Transverse momentum (GeV)')
        draw_signal_bg('h_single_jet2_pt',0,50, 'Transverse momentum (GeV)')
        draw_signal_bg('h_single_jet1_e',0,50, 'Energy (GeV)')
        draw_signal_bg('h_single_jet2_e',0,50, 'Energy (GeV)')

    else:
        print('plotting hjjvv channel...')
        draw_signal_bg('h_npfo', 0, 180, 'Particle flow object')
        draw_signal_bg('h_single_jet1_pt',0,100, 'Transverse momentum (GeV)')
        draw_signal_bg('h_single_jet2_pt',0,100, 'Transverse momentum (GeV)')
        draw_signal_bg('h_single_jet1_e',0,100, 'Energy (GeV)')
        draw_signal_bg('h_single_jet2_e',0,120, 'Energy (GeV)')

def draw_signal_bg(pic, x1, x2, title):

    tabs = sys.argv[2:]

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
        path = name.split('_')[0]
        exec('b%s = copy.copy(s)'%tabs.index(t))
        exec('b%s.Scale(0)'%tabs.index(t))
        
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
                    tem=sample.Get(pic)
                    a=copy.copy(tem)
                    a.Scale(scb)
                    exec('b%s.Add(a)'%tabs.index(t))

    max0=0
    max1=0
    max2=0    

    for i in range(3):
        exec('max%s = b%s.GetMaximum()'%(i,i))

    max = max0
    if max1 > max:
        max = max1
    
    if max2 > max:
        max = max2

    ROOT.gPad.SetLogy(1)
    b0.SetMinimum(0.1)
    b0.SetMaximum(10 * max)
    b0.GetXaxis().SetRangeUser(x1, x2)
    b0.SetXTitle(title)

    if pic == 'h_min_angle' or pic == 'h_single_jet_theta':
        b0.SetYTitle('Events/degree') 
    elif pic == 'h_npfo':
        b0.SetYTitle('Events')
    else:
        b0.SetYTitle('Events/GeV') 

    b0.SetLineColor(6)
    b0.Draw()
    leg.AddEntry(b0, '2fermion background')
    leg.Draw()

    b1.SetLineColor(3)
    b1.Draw('same')
    leg.AddEntry(b1, '4fermion background')
    leg.Draw()

    b2.SetLineColor(4)
    b2.Draw('same')
    leg.AddEntry(b2, 'ZH background')
    leg.Draw()

    s.SetLineColor(2)
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

    s.SetXTitle('Dijet mass (GeV)')
    s.SetYTitle('Missing mass (GeV)') 

    s.SetContour(99)
    s.Draw("colz")
    c.SaveAs(figfile)

if __name__ == '__main__':
    main()