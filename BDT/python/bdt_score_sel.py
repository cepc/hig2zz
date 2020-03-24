#!/usr/bin/env python
"""
Plot S/sqrt(S+B) versus BDT cut histogram
"""

__author__ = "Min Zhong <zmind@mail.ustc.edu.cn>"
__copyright__ = "Copyright (c) Min Zhong"
__created__ = "[2019-11-23]" 

import sys,os,copy
import math
import ROOT 
from tools import check_outfile_path

def main():

    sig_bg_bdt = ROOT.TH1D('sig_bg_bdt_cut', 'sig_bg_bdt_cut', 401, -2.005, 2.005) 
    sig_n = ROOT.TH1D('sig_n', 'sig_n', 401, -2.005, 2.005)
    ## Set the range of interest
    x1 = -0.6
    x2 = 0.5

    combine_opt = int(sys.argv[1])
    flag_zz = int(sys.argv[2])
    tabs = sys.argv[3:]

    c = ROOT.TCanvas('c', 'c', 1000, 640)

    signal_path = './run/'
    save_path = './fig/'
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

    figfile = save_path+'/sig_bg_bdt_cut.png'
    check_outfile_path(figfile)
 
    signal_sample =  ROOT.TFile(signal_path+'ana_File_merged_1.root')
    evah = signal_sample.Get('hevtflw_sel')
    eva = evah.GetBinContent(1)  #number of e2e2hvvjj
    if (combine_opt == 1):
	xsec = 6.77
    if (combine_opt == 2):
	xsec = 46.3
    if (combine_opt == 3):
	xsec = 137
    scs = 5600 * xsec * 0.0264 / eva
    s = signal_sample.Get('h_BDT_score_raw')
    s.Scale(scs)
    
    for t in tabs: 

        tab = open(t , 'r' )
        name = t.split('/')[-1]
        path = name.split('_')[0]
        exec('b%s = copy.copy(s)'%tabs.index(t))
        exec('b%s.Scale(0)'%tabs.index(t))
        
	if (combine_opt==1):
	    bg_path = 'channel_ll_' + str(flag_zz) + '/'
	if (combine_opt==2):
	    bg_path = 'channel_nn_' + str(flag_zz) + '/'
	if (combine_opt==3):
	    bg_path = 'channel_qq_' + str(flag_zz) + '/'

        for s_line in tab :
            
            if not s_line.startswith('#'):
                l = [x.strip() for x in s_line.split(',')]
                dname = l[0]
                event_exp = 5600.0 / 5050.0 * float(l[3]) # 5050 fb-1 to 5600 fb-1
                sample = ROOT.TFile('./run/' + bg_path + path + '/hist/' + dname + '/ana_File_merged_1.root')
                h=sample.Get('hevtflw_sel')
                event_ana = h.GetBinContent(1)
                
                if event_ana != 0:
                    scb = (event_exp / event_ana)
                    tem=sample.Get('h_BDT_score_raw')
                    a=copy.copy(tem)
                    a.Scale(scb)
                    exec('b%s.Add(a)'%tabs.index(t))

    SetCEPCCDRStyle()

    b = b0 + b1 + b2
    ROOT.gStyle.SetOptStat(000)
#    ROOT.gPad.SetLogy(1)
#    b0.SetMinimum(0.1)
#    b0.SetMaximum(10 * max)

    for i in range (400):
	bdt_cut = -2.00+0.01*i
	n_sig = 0
	n_bg = 0

	for ibin in range(i+1, 401, 1):
	    n_sig += s.GetBinContent(ibin+1)
	    n_bg += b.GetBinContent(ibin+1)
    
	sig_n.SetBinContent(i+1, n_sig)

	if (n_bg!=0):
            ratio = n_sig/math.sqrt(n_bg+n_sig)
#	    ratio = n_sig/math.sqrt(n_bg)
#           ratio = n_sig/n_bg
	    print 'BDT Cut: %.2f, Ratio: %.4f'%(bdt_cut, ratio)
	    sig_bg_bdt.SetBinContent(i+1, ratio)
#    	    sig_bg_bdt.SetBinContent(i+1, 0)

    pad1 = ROOT.TPad("pad1", "pad1", 0, 0.4, 1.0, 1.0); 
    pad2 = ROOT.TPad("pad2","pad2", 0, 0, 1.0, 0.4);	    

    sig_bg_bdt.GetXaxis().SetRangeUser(x1, x2)
    sig_bg_bdt.SetXTitle('')
    sig_bg_bdt.SetYTitle('S\over\sqrt{S+B}')
    #sig_bg_bdt.SetYTitle('S\over\sqrt{B}')
    #sig_bg_bdt.SetYTitle('S\over{B}')
    sig_bg_bdt.GetYaxis().SetTitleOffset(0.45)
    sig_bg_bdt.GetYaxis().SetTitleSize(0.057)
    sig_bg_bdt.GetYaxis().SetLabelFont(50)
    sig_bg_bdt.GetYaxis().SetLabelSize(0.05)
    sig_bg_bdt.GetXaxis().SetLabelFont(50)
    sig_bg_bdt.GetXaxis().SetLabelSize(0.05)
    sig_bg_bdt.SetLineColor(2)
    pad1.SetBottomMargin(0);
    pad1.Draw()
    pad1.cd()
    sig_bg_bdt.Draw('Hist')
    c.cd()
    pad2.SetTopMargin(0)
    pad2.SetBottomMargin(0.25)
    pad2.Draw()
    pad2.cd()
    sig_n.GetXaxis().SetRangeUser(x1, x2)
    sig_n.SetXTitle('BDT score cut')
    sig_n.SetYTitle('Number of Signals')
    sig_n.GetYaxis().SetTitleSize(0.06)
    sig_n.GetYaxis().SetTitleOffset(0.35)
    sig_n.GetYaxis().SetLabelFont(50)
    sig_n.GetYaxis().SetLabelSize(0.072)
    sig_n.GetXaxis().SetTitleSize(0.072)
    sig_n.GetXaxis().SetTitleOffset(1.1)
    sig_n.GetXaxis().SetLabelFont(50)
    sig_n.GetXaxis().SetLabelSize(0.072)
    sig_n.SetLineColor(6)
    sig_n.Draw('Hist')

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
