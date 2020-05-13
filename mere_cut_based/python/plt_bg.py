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

    SetCEPCCDRStyle()

    log_opt_f = 1 # not log scale
    log_opt_r = 2 # log scale
    if (combine_opt==1):
        if (opt==1): 
            draw_signal_bg('h_npfo_cut', 0, 140, 'Particle Flow Object',combine_opt,opt,log_opt_r,20,90)
            draw_signal_bg('h_m_dimuon_cut',50,130,'Dimuon Mass(GeV)',combine_opt, opt,log_opt_r,80,100)
            draw_signal_bg('h_m_dijet_cut',0,80,'Dijets Mass(GeV)',combine_opt, opt,log_opt_r,15,60)
            draw_signal_bg('h_vis_all_rec_m_cut',30,130,'Missing Mass(GeV)',combine_opt, opt,log_opt_r,75,105)
            draw_signal_bg('h_cos_cut',-1,1,'cos theta',combine_opt, opt,log_opt_r,0,0)
            draw_signal_bg('h_vis_all_cos_cut',-1,1,'cos theta_{visible}',combine_opt,opt,log_opt_r,-0.95,0.95)
            draw_signal_bg('h_angle_mj_cut',0,180,'Angle(dimuon-dijet)',combine_opt,opt,log_opt_r,60,170)
            draw_signal_bg('h_mrec_dimuon_cut',100,150, 'Dimuon Recoil Mass (GeV)',combine_opt,opt,log_opt_r,110,140)
            draw_signal_bg('h_mrec_dijet_cut',160,230,'Dijet Recoil Mass(GeV)',combine_opt, opt,log_opt_r,185,220)
            draw_signal_bg('h_vis_all_m_cut',100,160,'Visible Mass(GeV)',combine_opt, opt,log_opt_f,0,0)
            draw_signal_bg('h_vis_all_p_cut',0,70,'Visible P(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_vis_all_pt_cut',0,70,'Visible Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_lead_e_cut',0,60,'Leading Jet E(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_lead_pt_cut',0,50,'Leading Jet Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_sub_e_cut',0,40,'Sub-leading Jet E(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_sub_pt_cut',0,30,'Sub-leading Jet Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_mrec_dimuon_final',100,150,'Dimuon Recoil Mass(GeV)',combine_opt,opt,log_opt_f,0,0)

	if (opt==2):
            draw_signal_bg('h_npfo_cut', 0, 140, 'Particle Flow Object',combine_opt,opt,log_opt_r,30,100)
            draw_signal_bg('h_m_dimuon_cut',50,130,'Dimuon Mass(GeV)',combine_opt, opt,log_opt_r,80,100)
            draw_signal_bg('h_m_dijet_cut',30,130,'Dijets Mass(GeV)',combine_opt, opt,log_opt_r,60,105)
            draw_signal_bg('h_vis_all_rec_m_cut',0,80,'Missing Mass(GeV)',combine_opt, opt,log_opt_r,10,55)
            draw_signal_bg('h_cos_cut',-1,1,'cos theta',combine_opt, opt,log_opt_r,0,0)
            draw_signal_bg('h_vis_all_cos_cut',-1,1,'cos theta_{visible}',combine_opt,opt,log_opt_r,-0.95,0.95)
            draw_signal_bg('h_angle_mj_cut',0,180,'Angle(dimuon-dijet)',combine_opt,opt,log_opt_r,60,170)
            draw_signal_bg('h_mrec_dimuon_cut',100,150, 'Dimuon Recoil Mass (GeV)',combine_opt,opt,log_opt_r,110,140)
            draw_signal_bg('h_mrec_dijet_cut',90,190,'Dijet Recoil Mass(GeV)',combine_opt, opt,log_opt_r,0,0)
            draw_signal_bg('h_vis_all_m_cut',170,230,'Visible Mass(GeV)',combine_opt, opt,log_opt_r,175,215)
            draw_signal_bg('h_vis_all_p_cut',0,60,'Visible P(GeV)',combine_opt,opt,log_opt_r,0,0)
            draw_signal_bg('h_vis_all_pt_cut',0,60,'Visible Pt(GeV)',combine_opt,opt,log_opt_r,0,0)
            draw_signal_bg('h_jet_lead_e_cut',30,110,'Leading Jet E(GeV)',combine_opt,opt,log_opt_r,0,0)
            draw_signal_bg('h_jet_lead_pt_cut',0,90,'Leading Jet Pt(GeV)',combine_opt,opt,log_opt_r,0,0)
            draw_signal_bg('h_jet_sub_e_cut',0,70,'Sub-leading Jet E(GeV)',combine_opt,opt,log_opt_r,0,0)
            draw_signal_bg('h_jet_sub_pt_cut',0,60,'Sub-leading Jet Pt(GeV)',combine_opt,opt,log_opt_r,0,0)
            draw_signal_bg('h_mrec_dimuon_final',100,150,'Dimuon Recoil Mass(GeV)',combine_opt,opt,log_opt_f,0,0) 

    if (combine_opt==2):
	if (opt==1):
            draw_signal_bg('h_npfo_cut', 0, 120, 'Particle Flow Object',combine_opt,opt,log_opt_r,20,60)
            draw_signal_bg('h_vis_all_rec_m_cut',50,130,'Missing Mass(GeV)',combine_opt, opt,log_opt_r,75,110)
            draw_signal_bg('h_m_dimuon_cut',30,120,'Dimuon Mass(GeV)',combine_opt, opt,log_opt_r,60,100)
            draw_signal_bg('h_m_dijet_cut',0,80,'Dijets Mass(GeV)',combine_opt, opt,log_opt_r,10,55)
            draw_signal_bg('h_cos_cut',-1,1,'cos theta',combine_opt, opt,log_opt_r,0,0)
            draw_signal_bg('h_vis_all_cos_cut',-1,1,'cos theta_{visible}',combine_opt,opt,log_opt_r,-0.95,0.95)
            draw_signal_bg('h_angle_mj_cut',0,180,'Angle(dimuon-dijet)',combine_opt,opt,log_opt_r,0,135)
            draw_signal_bg('h_mrec_dimuon_cut',100,180, 'Dimuon Recoil Mass (GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_mrec_dijet_cut',140,240,'Dijet Recoil Mass(GeV)',combine_opt, opt,log_opt_f,0,0)
            draw_signal_bg('h_vis_all_m_cut',90,160,'Visible Mass(GeV)',combine_opt, opt,log_opt_f,110,140)
            draw_signal_bg('h_vis_all_p_cut',0,80,'Visible P(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_vis_all_pt_cut',0,80,'Visible Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_lead_e_cut',0,60,'Leading Jet E(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_lead_pt_cut',0,60,'Leading Jet Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_sub_e_cut',0,40,'Sub-leading Jet E(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_sub_pt_cut',0,40,'Sub-leading Jet Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_vis_all_m_final',100,150,'Visible Mass(GeV)',combine_opt,opt,log_opt_f,0,0)
	if (opt==2):
            draw_signal_bg('h_npfo_cut', 0, 120, 'Particle Flow Object',combine_opt,opt,log_opt_r,30,100)
            draw_signal_bg('h_vis_all_rec_m_cut',50,130,'Missing Mass(GeV)',combine_opt, opt,log_opt_r,75,110)
            draw_signal_bg('h_m_dimuon_cut',0,80,'Dimuon Mass(GeV)',combine_opt, opt,log_opt_r,10,60)
            draw_signal_bg('h_m_dijet_cut',30,120,'Dijets Mass(GeV)',combine_opt, opt,log_opt_r,60,100)
            draw_signal_bg('h_cos_cut',-1,1,'cos theta',combine_opt, opt,log_opt_r,0,0)
            draw_signal_bg('h_vis_all_cos_cut',-1,1,'cos theta_{visible}',combine_opt,opt,log_opt_r,-0.95,0.95)
            draw_signal_bg('h_angle_mj_cut',0,180,'Angle(dimuon-dijet)',combine_opt,opt,log_opt_r,0,135)
#            draw_signal_bg('h_mrec_dimuon_cut',140,240, 'Dimuon Recoil Mass (GeV)',combine_opt,opt,log_opt_f,165,215)
            draw_signal_bg('h_mrec_dijet_cut',80,200,'Dijet Recoil Mass(GeV)',combine_opt, opt,log_opt_f,0,0)
            draw_signal_bg('h_vis_all_m_cut',90,160,'Visible Mass(GeV)',combine_opt, opt,log_opt_f,110,140)
            draw_signal_bg('h_vis_all_p_cut',0,80,'Visible P(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_vis_all_pt_cut',0,80,'Visible Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_lead_e_cut',0,100,'Leading Jet E(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_lead_pt_cut',0,100,'Leading Jet Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_sub_e_cut',0,70,'Sub-leading Jet E(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_sub_pt_cut',0,70,'Sub-leading Jet Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_vis_all_m_final',100,150,'Visible Mass(GeV)',combine_opt,opt,log_opt_f,0,0)
    if (combine_opt==3):
	if (opt==1):
            draw_signal_bg('h_npfo_cut', 0, 120, 'Particle Flow Object',combine_opt,opt,log_opt_r,40,95)
            draw_signal_bg('h_m_dijet_cut',50,130,'Dijets Mass(GeV)',combine_opt, opt,log_opt_r,75,105)
            draw_signal_bg('h_m_dimuon_cut',0,80,'Dimuon Mass(GeV)',combine_opt, opt,log_opt_r,15,55)
            draw_signal_bg('h_vis_all_rec_m_cut',10,140,'Missing Mass(GeV)',combine_opt, opt,log_opt_r,70,110)
            draw_signal_bg('h_cos_cut',-1,1,'cos theta',combine_opt, opt,log_opt_r,0,0)
            draw_signal_bg('h_vis_all_cos_cut',-1,1,'cos theta_{visible}',combine_opt,opt,log_opt_r,-0.95,0.95)
            draw_signal_bg('h_angle_mj_cut',0,180,'Angle(dimuon-dijet)',combine_opt,opt,log_opt_r,0,0)
            draw_signal_bg('h_mrec_dimuon_cut',140,240, 'Dimuon Recoil Mass (GeV)',combine_opt,opt,log_opt_r,175,215)
            draw_signal_bg('h_mrec_dijet_cut',90,160,'Dijet Recoil Mass(GeV)',combine_opt, opt,log_opt_f,110,140)
            draw_signal_bg('h_vis_all_m_cut',100,180,'Visible Mass(GeV)',combine_opt, opt,log_opt_f,115,155)
            draw_signal_bg('h_vis_all_p_cut',0,80,'Visible P(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_vis_all_pt_cut',0,80,'Visible Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_lead_e_cut',40,100,'Leading Jet E(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_lead_pt_cut',0,80,'Leading Jet Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_sub_e_cut',0,60,'Sub-leading Jet E(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_sub_pt_cut',0,60,'Sub-leading Jet Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_mrec_dijet_final',100,150,'Dijet Recoil Mass(GeV)',combine_opt,opt,log_opt_f,0,0)
	if (opt==2):
            draw_signal_bg('h_npfo_cut', 0, 120, 'Particle Flow Object',combine_opt,opt,log_opt_r,40,95)
            draw_signal_bg('h_m_dijet_cut',50,130,'Dijets Mass(GeV)',combine_opt, opt,log_opt_r,75,105)
            draw_signal_bg('h_m_dimuon_cut',0,120,'Dimuon Mass(GeV)',combine_opt, opt,log_opt_r,75,100)
            draw_signal_bg('h_vis_all_rec_m_cut',0,80,'Missing Mass(GeV)',combine_opt, opt,log_opt_r,10,50)
            draw_signal_bg('h_cos_cut',-1,1,'cos theta',combine_opt, opt,log_opt_r,0,0)
            draw_signal_bg('h_vis_all_cos_cut',-1,1,'cos theta_{visible}',combine_opt,opt,log_opt_r,-0.95,0.95)
            draw_signal_bg('h_angle_mj_cut',0,180,'Angle(dimuon-dijet)',combine_opt,opt,log_opt_r,120,170)
            draw_signal_bg('h_mrec_dimuon_cut',80,180, 'Dimuon Recoil Mass (GeV)',combine_opt,opt,log_opt_r,115,155)
            draw_signal_bg('h_mrec_dijet_cut',90,160,'Dijet Recoil Mass(GeV)',combine_opt, opt,log_opt_f,110,140)
            draw_signal_bg('h_vis_all_m_cut',170,250,'Visible Mass(GeV)',combine_opt, opt,log_opt_f,185,215)
            draw_signal_bg('h_vis_all_p_cut',0,50,'Visible P(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_vis_all_pt_cut',0,50,'Visible Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_lead_e_cut',40,100,'Leading Jet E(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_lead_pt_cut',0,100,'Leading Jet Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_sub_e_cut',0,70,'Sub-leading Jet E(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_jet_sub_pt_cut',0,70,'Sub-leading Jet Pt(GeV)',combine_opt,opt,log_opt_f,0,0)
            draw_signal_bg('h_mrec_dijet_final',100,150,'Dijet Recoil Mass(GeV)',combine_opt,opt,log_opt_f,0,0)
#        draw_signal_bg('h_mrec_dijet_raw',100,150,'Dijet rec mass(GeV)',combine_opt, opt,log_opt_f)
#        draw_signal_bg('h_m_dimuon_raw',0,150,'Dimuon mass(GeV)',combine_opt, opt,log_opt_r)
#        draw_signal_bg('h_m_dijet_raw',50,130,'Dijets mass(GeV)',combine_opt, opt,log_opt_r)
#        draw_signal_bg('h_vis_all_m_raw',100,250,'Visible mass(GeV)',combine_opt, opt,log_opt_r)
#        draw_signal_bg('h_cos_raw',-1,1,'cos_raw(GeV)',combine_opt, opt,log_opt_r)
#        draw_signal_bg('h_mrec_dimuon_raw',100,250, 'Dimuon rec mass (GeV)',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_jet_lead_e_raw',0,100,'jet_lead_e_raw(GeV)',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_jet_sub_e_raw',0,100,'jet_sub_e_raw(GeV)',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_angle_mj_raw',0,180,'h_angle_mj_raw',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_vis_all_pt_raw',0,250,'Visible Pt(GeV)',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_vis_all_cos_raw',-1,1,'vis_all_cos',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_vis_all_rec_m_raw',0,100,'vis_all_rec_m_raw((GeV)',combine_opt, opt,log_opt_r)
#        draw_signal_bg('h_npfo_raw', 0, 120, 'Particle flow object(GeV)',combine_opt,opt,log_opt_r)

#        draw_signal_bg('h_mrec_dijet_final',100,150,'Dijet rec mass(GeV)',combine_opt, opt,log_opt_f)
#        draw_signal_bg('h_m_dimuon_final',0,150,'Dimuon mass(GeV)',combine_opt, opt,log_opt_r)
#        draw_signal_bg('h_m_dijet_final',50,130,'Dijets mass(GeV)',combine_opt, opt,log_opt_r)
#        draw_signal_bg('h_vis_all_m_final',100,250,'Visible mass(GeV)',combine_opt, opt,log_opt_r)
#        draw_signal_bg('h_cos_final',-1,1,'cos_final(GeV)',combine_opt, opt,log_opt_r)
#        draw_signal_bg('h_mrec_dimuon_final',100,250, 'Dimuon rec mass (GeV)',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_jet_lead_e_final',0,100,'jet_lead_e_final(GeV)',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_jet_sub_e_final',0,100,'jet_sub_e_final(GeV)',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_angle_mj_final',0,180,'h_angle_mj_final',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_vis_all_pt_final',0,250,'Visible Pt(GeV)',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_vis_all_cos_final',-1,1,'vis_all_cos',combine_opt,opt,log_opt_r)
#        draw_signal_bg('h_vis_all_rec_m_final',0,100,'vis_all_rec_m_final((GeV)',combine_opt, opt,log_opt_r)
#        draw_signal_bg('h_npfo_final', 30, 110, 'Particle flow object(GeV)',combine_opt,opt,log_opt_r)

#        draw_2d('h_2D_dimuon_missing_raw',combine_opt,opt,1)
#        draw_2d('h_2D_dimuon_missing_final',combine_opt,opt,2)

def draw_signal_bg(pic, x1, x2, title, combine_opt, opt, log_opt,left,right):

    tabs = sys.argv[3:]

    c = ROOT.TCanvas('c', 'c', 800, 800)

    #leg = ROOT.TLegend(0.63, 0.7, 0.90, 0.90)
    leg = ROOT.TLegend(0.70, 0.83, 0.95, 0.97)
    stack = ROOT.THStack('stack','')

    leg.SetTextFont(60)
    leg.SetTextSize(0.02)

    if (combine_opt==1):
        figfile = './fig/channel_ll_%s/sbg_%s.png'%(opt,pic)
        signal_sample =  ROOT.TFile('./run/channel_ll_%s/llh2zz/hist/ana_File_merged_1.root'%opt)
    if (combine_opt==2):
        figfile = './fig/channel_nn_%s/sbg_%s.png'%(opt,pic)
        signal_sample =  ROOT.TFile('./run/channel_nn_%s/nnh2zz/hist/ana_File_merged_1.root'%opt)
    if (combine_opt==3):
        figfile = './fig/channel_qq_%s/sbg_%s.png'%(opt,pic)
        signal_sample =  ROOT.TFile('./run/channel_qq_%s/qqh2zz/hist/ana_File_merged_1.root'%opt)

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
                    sample = ROOT.TFile('./run/channel_ll_%s/'%opt + path + '/hist/' + dname + '/ana_File_merged_1.root')
                if (combine_opt==2):
                    sample = ROOT.TFile('./run/channel_nn_%s/'%opt + path + '/hist/' + dname + '/ana_File_merged_1.root')
                if (combine_opt==3):
                    sample = ROOT.TFile('./run/channel_qq_%s/'%opt + path + '/hist/' + dname + '/ana_File_merged_1.root')
 
                h=sample.Get('hevtflw_pre')
                event_ana = h.GetBinContent(1)

                if event_ana != 0:
                    scb = (event_exp / event_ana)
                    tem=sample.Get(pic)
                    a=copy.copy(tem)
                    a.Scale(scb)
                    exec('b%s.Add(a)'%tabs.index(t))

    #SetCEPCCDRStyle()

    max0=0
    max1=0
    max2=0    

    for i in range(3):
        exec('max%s = b%s.GetMaximum()'%(i,i))

    max_signal = s.GetMaximum()
    max = max_signal

    if max0+max1+max2 > max:
        max = max0+max1+max2

    ROOT.gStyle.SetOptStat(000)

    if (log_opt==2):
    	ROOT.gPad.SetLogy(1)
        s.SetMinimum(0.01)
    if (log_opt==2):
	s.SetMaximum(max*31)
    if (log_opt==1):
	s.SetMaximum(max*1.35)
    s.GetXaxis().SetRangeUser(x1, x2)
    s.SetXTitle(title)

    if 'angle' in pic:
        s.SetYTitle('Events/Degree') 
    elif ('npfo' in pic) or ('cos' in pic) :
        s.SetYTitle('Events')
    else:
        s.SetYTitle('Events/GeV') 

    s.GetYaxis().SetTitleOffset(1.4)
    s.GetYaxis().SetLabelFont(50)
    s.GetYaxis().SetLabelSize(0.034)
    s.GetXaxis().SetLabelFont(50)
    s.GetXaxis().SetLabelSize(0.034)
    s.SetLineColor(2)
    s.Draw('Hist')
    leg.AddEntry(s, "signal")
   
    b0.SetFillColor(ROOT.kOrange-2)
    stack.Add(b0)
    leg.AddEntry(b0, '2fermion background')

    b1.SetFillColor(ROOT.kCyan-9)
    stack.Add(b1)
    leg.AddEntry(b1, '4fermion background')

    b2.SetFillColor(ROOT.kSpring-5)
    stack.Add(b2)
    leg.AddEntry(b2, 'ZH background')

    leg.Draw()
    stack.Draw('Hist same')
    s.Draw('Hist same')
    
    if left!=right:
        if log_opt==2:
    	    arrow_up = max*0.8
	    arrow_down = 0.01
        if log_opt==1:
	    arrow_up = max*0.8
            arrow_down = 1

        ar1 = ROOT.TArrow(left, arrow_up, left, arrow_down, 0.02, "|>")
        ar1.SetLineWidth(2)
        ar1.SetLineStyle(2)
        ar1.SetLineColor(1)
        ar1.Draw()

        ar2 = ROOT.TArrow(right, arrow_up, right, arrow_down, 0.02, "|>")
        ar2.SetLineWidth(2)
        ar2.SetLineStyle(2)
        ar2.SetLineColor(1)
        ar2.Draw()

    c.SaveAs(figfile)

def draw_2d(pic, combine_opt, opt, draw_opt):

    c = ROOT.TCanvas('c', 'c', 1600, 1600)

    if (combine_opt==1):
        figfile = './fig/channel_ll_%s/2d_%s.png'%(opt,pic)
        sample =  ROOT.TFile('./run/channel_ll_%s/llh2zz/hist/ana_File_merged_1.root'%opt)
    if (combine_opt==2):
        figfile = './fig/channel_nn_%s/2d_%s.png'%(opt,pic)
        sample =  ROOT.TFile('./run/channel_nn_%s/nnh2zz/hist/ana_File_merged_1.root'%opt)
    if (combine_opt==3):
        figfile = './fig/channel_qq_%s/2d_%s.png'%(opt,pic)
        sample =  ROOT.TFile('./run/channel_qq_%s/qqh2zz/hist/ana_File_merged_1.root'%opt)

    check_outfile_path(figfile)

    s = sample.Get(pic)

    if (combine_opt==1):
    	s.SetXTitle('Dijet mass (GeV)')
    	s.SetYTitle('Missing mass (GeV)') 
    if (combine_opt==3):
	s.SetXTitle('Dimuon mass (GeV)')
	s.SetYTitle('Missing mass(GeV)')

    ROOT.gStyle.SetOptStat(000)

    s.SetContour(99)
    if (draw_opt==1):
    	s.Draw("")
    if (draw_opt==2):
    	s.Draw("colz1")
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
