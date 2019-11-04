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
    combine_opt = int(sys.argv[2])

    if (combine_opt==1):
        draw_signal_bg('h_m_dimuon',0 , 210, 'Dimuon mass (GeV)',1)
        draw_signal_bg('h_mrec_dimuon',50 ,160, 'Dimuon rec mass (GeV)',1)
        draw_signal_bg('h_vis_all_pt', 0, 100, 'Transverse momentum (GeV)',1)
        draw_signal_bg('h_min_angle',0, 120, 'Muon-jet angle (degree)',1)
        draw_signal_bg('h_single_jet_theta',0,180, 'Two jet angle (degree)',1)  
        draw_signal_bg('h_mrec_dimuon_final',110,150, 'Dimuon rec mass (GeV)',1) 
        draw_2d('h_2D_dijet_missing',1)
        draw_2d('h_2D_dijet_missing_raw',1)  

        if opt == 1: 
            print('plotting hvvjj channel...')
            draw_signal_bg('h_npfo', 0, 100, 'Particle flow object',1)
            draw_signal_bg('h_single_jet1_pt',0,50, 'Transverse momentum (GeV)',1)
            draw_signal_bg('h_single_jet2_pt',0,50, 'Transverse momentum (GeV)',1)
            draw_signal_bg('h_single_jet1_e',0,50, 'Energy (GeV)',1)
            draw_signal_bg('h_single_jet2_e',0,50, 'Energy (GeV)',1)
    
        else:
            print('plotting hjjvv channel...')
            draw_signal_bg('h_npfo', 0, 180, 'Particle flow object',1)
            draw_signal_bg('h_single_jet1_pt',0,100, 'Transverse momentum (GeV)',1)
            draw_signal_bg('h_single_jet2_pt',0,100, 'Transverse momentum (GeV)',1)
            draw_signal_bg('h_single_jet1_e',0,100, 'Energy (GeV)',1)
            draw_signal_bg('h_single_jet2_e',0,120, 'Energy (GeV)',1)

    if (combine_opt==2):
        draw_signal_bg('h_vis_all_m_final',115,135,'vis_all_m_final(GeV)',2)

    if (combine_opt==3):
        draw_signal_bg('h_m_dimuon_final',0,100,'Dimuon mass(GeV)')
        draw_signal_bg('h_m_dijet_final',10,100,'Dijet mass(GeV)')
        draw_signal_bg('h_mrec_dijet_final',110,220,'Dijet rec mass(GeV)')
        draw_signal_bg('h_mrec_dimuon_final',110,220, 'Dimuon rec mass (GeV)')
        draw_signal_bg('h_m_visible_final',10,100,'visible_mass_final(GeV)')
        draw_signal_bg('h_m_missing_final',65,105,'missing_mass_final(GeV)')
        draw_signal_bg('h_vis_all_pt_final',20,70,'vis_all_pt_final(GeV)')
        draw_signal_bg('h_vis_all_m_final',115,135,'vis_all_m_final(GeV)')
        draw_signal_bg('h_vis_all_p_final',10,50,'vis_all_p_final(GeV)')
        draw_signal_bg('h_vis_all_rec_m_final',65,105,'vis_all_rec_m_final((GeV)')
        draw_signal_bg('h_vis_all_cos_final',-1,1,'vis_all_cos_final(GeV)')
        draw_signal_bg('h_cos_final',-1,1,'cos_final(GeV)')
        draw_signal_bg('h_npfo', 0, 200, 'Particle flow object(GeV)')
        draw_signal_bg('h_npfo_final', 0, 200, 'Particle flow object(GeV)')
        draw_signal_bg('h_npfo_raw', 0, 200, 'Particle flow object(GeV)')
        draw_signal_bg('h_vis_all_m',0,240,'vis_all_m(GeV)')
        draw_signal_bg('h_cos',-1,1,'cos')
        draw_signal_bg('h_jet_lead_e_final',10,75,'jet_lead_e_final(GeV)')
        draw_signal_bg('h_jet_sub_e_final',0,50,'jet_sub_e_final(GeV)')
        draw_signal_bg('h_angle_mj_final',0,180,'h_angle_mj_final')
        draw_signal_bg('h_m_dimuon_raw',0,260,'Dimuon mass(GeV)')
        draw_signal_bg('h_mrec_dimuon_raw',0,260,'Dimuon rec mass (GeV)')
        draw_signal_bg('h_m_dijet_raw',0,260,'Dijet mass(GeV)')
        draw_signal_bg('h_mrec_dijet_raw',0,260,'Dijet rec mass(GeV)')
        draw_signal_bg('h_m_visible_raw',0,260,'visible mass(GeV)')
        draw_signal_bg('h_m_missing_raw',0,260,'missing_mass(GeV)')
        draw_signal_bg('h_vis_all_pt_raw',0,100,'vis_all_pt(GeV)')
        draw_signal_bg('h_vis_all_m_raw',0,240,'vis_all_m(GeV)')
        draw_signal_bg('h_vis_all_p_raw',0,80,'vis_all_p(GeV)')
        draw_signal_bg('h_vis_all_rec_m_raw',-50,250,'vis_all_rec_m(GeV)')
        draw_signal_bg('h_vis_all_cos_raw',-1,1,'vis_all_cos')
        draw_signal_bg('h_cos_raw',-1,1,'cos')
        draw_signal_bg('h_jet_lead_e_raw',0,200,'jet_lead_e_raw(GeV)')
        draw_signal_bg('h_jet_sub_e_raw',0,200,'jet_sub_e_raw(GeV)')
        draw_signal_bg('h_angle_mj_raw',0,180,'h_angle_mj_raw(GeV)')

def draw_signal_bg(pic, x1, x2, title, combine_opt):

    tabs = sys.argv[3:]

    c = ROOT.TCanvas('c', 'c', 800, 800)

    leg = ROOT.TLegend(0.63, 0.7, 0.90, 0.90)
    stack = ROOT.THStack('stack','')

    leg.SetTextFont(60)
    leg.SetTextSize(0.02)

    if (combine_opt==1):
        figfile = './fig/channel_ll/sbg_%s.pdf'%pic
        signal_sample =  ROOT.TFile('./run/channel_ll/llh2zz/hist/ana_File_merged_1.root')
    if (combine_opt==2):
        figfile = './fig/channel_nn/sbg_%s.pdf'%pic
        signal_sample =  ROOT.TFile('./run/channel_nn/nnh2zz/hist/ana_File_merged_1.root')
    if (combine_opt==3):
        figfile = './fig/channel_qq/sbg_%s.pdf'%pic
        signal_sample =  ROOT.TFile('./run/channel_qq/qqh2zz/hist/ana_File_merged_1.root')

    check_outfile_path(figfile)

    evah = signal_sample.Get('hevtflw_pre')
    eva = evah.GetBinContent(1)  #number of e2e2hvvjj
    if (combine_opt==1):
        scs = 5600 * 6.77 * 0.0264 / eva
    if (combine_opt==2):
        scs = 5600 * 46.3 * 0.0264 / eva
    if (combine_opt==3):
        scs = 5600 * 137 *0.0264 /eva
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
                event_exp = 5600.0/5050.0 * float(l[3]) # 5050 fb-1 to 5600 fb-1
                if (combine_opt==1): 
                    sample = ROOT.TFile('./run/channel_ll/' + path + '/hist/' + dname + '/ana_File_merged_1.root')
                if (combine_opt==2):
                    sample = ROOT.TFile('./run/channel_nn/' + path + '/hist/' + dname + '/ana_File_merged_1.root')
                if (combine_opt==3):
                    sample = ROOT.TFile('./run/channel_qq/' + path + '/hist/' + dname + '/ana_File_merged_1.root')
 
                h=sample.Get('hevtflw_pre')
                event_ana = h.GetBinContent(1)

                if event_ana != 0:
                    scb = (event_exp / event_ana)
                    tem=sample.Get(pic)
                    a=copy.copy(tem)
                    a.Scale(scb)
                    exec('b%s.Add(a)'%tabs.index(t))

    SetCEPCCDRStyle()

    max0=0
    max1=0
    max2=0    

    for i in range(3):
        exec('max%s = b%s.GetMaximum()'%(i,i))

    max_signal = s.GetMaximum()
    max = max_signal

    if max0 > max:
        max = max0

    if max1 > max:
        max = max1
    
    if max2 > max:
        max = max2


    ROOT.gStyle.SetOptStat(000)

#    ROOT.gPad.SetLogy(1)
#    b0.SetMinimum(0.1)
#    b0.SetMaximum(10 * max)
    s.SetMaximum(max*1.15)
    s.GetXaxis().SetRangeUser(x1, x2)
    s.SetXTitle(title)

    if pic == 'h_min_angle' or pic == 'h_single_jet_theta':
        s.SetYTitle('Events/degree') 
    elif pic == 'h_npfo' or pic == 'h_npfo_raw' or pic == 'h_npfo_final':
        s.SetYTitle('Events')
    else:
        s.SetYTitle('Events/GeV') 

    s.GetYaxis().SetTitleOffset(1.4)
    s.GetYaxis().SetLabelFont(50)
    s.GetYaxis().SetLabelSize(0.034)
    s.GetXaxis().SetLabelFont(50)
    s.GetXaxis().SetLabelSize(0.034)
    s.SetLineColor(2)
    s.Draw('')
    leg.AddEntry(s, "signal")
   
    b0.SetFillColor(6)
    stack.Add(b0)
    leg.AddEntry(b0, '2fermion background')

    b1.SetFillColor(4)
    stack.Add(b1)
    leg.AddEntry(b1, '4fermion background')

    b2.SetFillColor(8)
    stack.Add(b2)
    leg.AddEntry(b2, 'ZH background')

    leg.Draw()
    stack.Draw('sameH')
    s.Draw('same')

    c.SaveAs(figfile)

def draw_2d(pic, combine_opt):

    c = ROOT.TCanvas('c', 'c', 1600, 1600)

    if (combine_opt==1):
        figfile = './fig/channel_ll/2d_%s.pdf'%pic
        sample =  ROOT.TFile('./run/channel_ll/llh2zz/hist/ana_File_merged_1.root')
    if (combine_opt==2):
        figfile = './fig/channel_nn/2d_%s.pdf'%pic
        sample =  ROOT.TFile('./run/channel_nn/nnh2zz/hist/ana_File_merged_1.root')
    if (combine_opt==3):
        figfile = './fig/channel_qq/2d_%s.pdf'%pic
        sample =  ROOT.TFile('./run/channel_qq/qqh2zz/hist/ana_File_merged_1.root')

    check_outfile_path(figfile)

    s = sample.Get(pic)

    s.SetXTitle('Dijet mass (GeV)')
    s.SetYTitle('Missing mass (GeV)') 

    s.SetContour(99)
    s.Draw("colz")
    c.SaveAs(figfile)

def SetCEPCCDRStyle():

    CEPCCDRStyle = ROOT.TStyle("CEPCCDRStyle","Style for CEPC CDR by Kaili")

    #canvas
    CEPCCDRStyle.SetCanvasBorderMode(0)
    CEPCCDRStyle.SetCanvasColor(0)
    CEPCCDRStyle.SetCanvasDefH(800)
    CEPCCDRStyle.SetCanvasDefW(800)
    CEPCCDRStyle.SetCanvasDefX(0)
    CEPCCDRStyle.SetCanvasDefY(0)

    #pad
    CEPCCDRStyle.SetPadBorderMode(0)
    CEPCCDRStyle.SetPadColor(0)
    CEPCCDRStyle.SetGridStyle(3)
    CEPCCDRStyle.SetGridWidth(1)

    #frame
    CEPCCDRStyle.SetFrameBorderMode(0);
    CEPCCDRStyle.SetFrameBorderSize(1);
    CEPCCDRStyle.SetFrameFillColor(0);
    CEPCCDRStyle.SetFrameFillStyle(0);
    CEPCCDRStyle.SetFrameLineColor(1);
    CEPCCDRStyle.SetFrameLineStyle(1);
    CEPCCDRStyle.SetFrameLineWidth(2);

    #hist
    CEPCCDRStyle.SetHistLineStyle(0)
    CEPCCDRStyle.SetEndErrorSize(2)
    CEPCCDRStyle.SetMarkerStyle(20)

    #fit
    CEPCCDRStyle.SetOptFit(0)
    CEPCCDRStyle.SetFitFormat("5.4g")
    CEPCCDRStyle.SetFuncColor(2)
    CEPCCDRStyle.SetFuncStyle(1)
    CEPCCDRStyle.SetFuncWidth(2)

    #date
    CEPCCDRStyle.SetOptDate(0)

    #statistics box
    CEPCCDRStyle.SetOptFile(0)
    CEPCCDRStyle.SetOptStat(0)
    CEPCCDRStyle.SetStatColor(0)
    CEPCCDRStyle.SetStatTextColor(1)
    CEPCCDRStyle.SetStatFormat("6.4g")
    CEPCCDRStyle.SetStatBorderSize(1)
    CEPCCDRStyle.SetStatH(0.1)
    CEPCCDRStyle.SetStatW(0.15)

    #margins
    CEPCCDRStyle.SetPadLeftMargin(0.18)
    CEPCCDRStyle.SetPadRightMargin(0.04)
    CEPCCDRStyle.SetPadBottomMargin(0.11)
    CEPCCDRStyle.SetPadTopMargin(0.02)

    #title
    CEPCCDRStyle.SetOptTitle(0)
    CEPCCDRStyle.SetTitleFont(43)
    CEPCCDRStyle.SetTitleColor(1)
    CEPCCDRStyle.SetTitleTextColor(1)
    CEPCCDRStyle.SetTitleFillColor(0)
    CEPCCDRStyle.SetTitleFontSize(36)
    CEPCCDRStyle.SetTitleXOffset(0.9)
    CEPCCDRStyle.SetTitleYOffset(1.0)
    #axis
    CEPCCDRStyle.SetTitleColor(1, "XYZ")
    CEPCCDRStyle.SetTitleFont(43, "XYZ")
    CEPCCDRStyle.SetTitleSize(36, "XYZ")
    CEPCCDRStyle.SetLabelColor(1, "XYZ")
    CEPCCDRStyle.SetLabelFont(43, "XYZ")
    CEPCCDRStyle.SetLabelOffset(0.005, "XYZ")
    CEPCCDRStyle.SetLabelSize(34, "XYZ")
    CEPCCDRStyle.SetAxisColor(1, "XYZ")
    CEPCCDRStyle.SetStripDecimals(1)
    CEPCCDRStyle.SetTickLength(0.02, "XYZ")
    CEPCCDRStyle.SetNdivisions(508, "XYZ")
    CEPCCDRStyle.SetPadTickX(1)
    CEPCCDRStyle.SetPadTickY(1)

    #others
    CEPCCDRStyle.SetPaperSize(20.,20.)
    CEPCCDRStyle.SetHatchesLineWidth(5)
    CEPCCDRStyle.SetHatchesSpacing(0.05)
    CEPCCDRStyle.cd()

if __name__ == '__main__':
    main()
