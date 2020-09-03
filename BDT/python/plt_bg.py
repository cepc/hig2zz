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

    combine_opt = int(sys.argv[1])
    flag_zz = int(sys.argv[2])

    SetCEPCCDRStyle()

    log_opt_f = 1 # not log scale
    log_opt_r = 2 # log scale

    if (combine_opt == 1):
        if (flag_zz == 1):
            draw_signal_bg('h_dimuon_rec_m_raw',110,140,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dijet_rec_m_raw',100,250,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_rec_m_raw',10,150,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
	    draw_signal_bg('h_vis_all_p_raw',0,100,'Visible p(GeV)', combine_opt, flag_zz, log_opt_r)
	    draw_signal_bg('h_vis_all_pt_raw',0,90,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_r)
	    draw_signal_bg('h_vis_all_m_raw',80,200,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_r)
	    draw_signal_bg('h_dimuon_m_raw',80,100,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_r)
	    draw_signal_bg('h_dijet_m_raw',0,80,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_r)
	    draw_signal_bg('h_jet_lead_e_raw',0,80,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_lead_pt_raw',0,70,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
	    draw_signal_bg('h_jet_sub_e_raw',0,60,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_sub_pt_raw',0,50,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
	    draw_signal_bg('h_dimuon_dijet_angle_raw',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_r)
	    draw_signal_bg('h_n_col_reco_raw',20,90,'N(pfo)', combine_opt, flag_zz, log_opt_r)
	    draw_signal_bg('h_cos_raw',-1,1,'cos theta', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_cos_raw',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_r)
	    draw_signal_bg('h_BDT_score_raw',-0.50,0.35,'BDT score', combine_opt, flag_zz, log_opt_r)

            draw_signal_bg('h_dimuon_rec_m_final',110,140,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_rec_m_final',100,250,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_rec_m_final',10,150,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_p_final',0,100,'Visible p(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_pt_final',0,90,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_m_final',80,200,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_m_final',80,100,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_m_final',0,80,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_e_final',0,80,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_pt_final',0,70,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_e_final',0,60,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_pt_final',0,50,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_dijet_angle_final',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_n_col_reco_final',20,90,'N(pfo)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_cos_final',-1,1,'cos theta', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_cos_final',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_BDT_score_final',-0.50,0.35,'BDT score', combine_opt, flag_zz, log_opt_f)

	if (flag_zz == 2):
            draw_signal_bg('h_dimuon_rec_m_raw',110,140,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dijet_rec_m_raw',0,200,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_rec_m_raw',-50,80,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_p_raw',0,110,'Visible p(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_pt_raw',0,100,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_m_raw',100,250,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dimuon_m_raw',80,100,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dijet_m_raw',0,200,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_lead_e_raw',0,140,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_lead_pt_raw',0,120,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_sub_e_raw',0,100,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_sub_pt_raw',0,80,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dimuon_dijet_angle_raw',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_n_col_reco_raw',30,100,'N(pfo)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_cos_raw',-1,1,'cos theta', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_cos_raw',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_BDT_score_raw',-0.9,0.2,'BDT score', combine_opt, flag_zz, log_opt_r)

            draw_signal_bg('h_dimuon_rec_m_final',110,140,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_rec_m_final',0,200,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_rec_m_final',-50,80,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_p_final',0,110,'Visible p(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_pt_final',0,100,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_m_final',100,250,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_m_final',80,100,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_m_final',0,200,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_e_final',0,140,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_pt_final',0,120,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_e_final',0,100,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_pt_final',0,80,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_dijet_angle_final',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_n_col_reco_final',30,100,'N(pfo)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_cos_final',-1,1,'cos theta', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_cos_final',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_BDT_score_final',-0.9,0.2,'BDT score', combine_opt, flag_zz, log_opt_f)

    if (combine_opt == 2):
        if (flag_zz == 1):
            draw_signal_bg('h_dimuon_rec_m_raw',70,200,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dijet_rec_m_raw',100,250,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_rec_m_raw',75,110,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_p_raw',0,90,'Visible p(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_pt_raw',0,70,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_m_raw',110,140,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dimuon_m_raw',0,150,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dijet_m_raw',0,80,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_lead_e_raw',0,100,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_lead_pt_raw',0,80,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_sub_e_raw',0,60,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_sub_pt_raw',0,40,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dimuon_dijet_angle_raw',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_n_col_reco_raw',20,60,'N(pfo)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_cos_raw',-1,1,'cos theta', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_cos_raw',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_BDT_score_raw',-0.50,0.30,'BDT score', combine_opt, flag_zz, log_opt_r)

            draw_signal_bg('h_dimuon_rec_m_final',70,200,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_rec_m_final',100,250,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_rec_m_final',75,110,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_p_final',0,90,'Visible p(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_pt_final',0,70,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_m_final',110,140,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_m_final',0,150,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_m_final',0,80,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_e_final',0,100,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_pt_final',0,80,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_e_final',0,60,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_pt_final',0,40,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_dijet_angle_final',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_n_col_reco_final',20,60,'N(pfo)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_cos_final',-1,1,'cos theta', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_cos_final',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_BDT_score_final',-0.50,0.30,'BDT score', combine_opt, flag_zz, log_opt_f)

        if (flag_zz == 2):
            draw_signal_bg('h_dimuon_rec_m_raw',100,250,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dijet_rec_m_raw',80,200,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_rec_m_raw',75,110,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_p_raw',0,90,'Visible p(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_pt_raw',0,80,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_m_raw',110,140,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dimuon_m_raw',0,70,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dijet_m_raw',10,140,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_lead_e_raw',0,110,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_lead_pt_raw',0,100,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_sub_e_raw',0,90,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_sub_pt_raw',0,80,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dimuon_dijet_angle_raw',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_n_col_reco_raw',30,100,'N(pfo)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_cos_raw',-1,1,'cos theta', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_cos_raw',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_BDT_score_raw',-0.80,0.20,'BDT score', combine_opt, flag_zz, log_opt_r)

            draw_signal_bg('h_dimuon_rec_m_final',100,250,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_rec_m_final',80,200,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_rec_m_final',75,110,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_p_final',0,90,'Visible p(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_pt_final',0,80,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_m_final',110,140,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_m_final',0,70,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_m_final',10,140,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_e_final',0,110,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_pt_final',0,100,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_e_final',0,90,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_pt_final',0,80,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_dijet_angle_final',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_n_col_reco_final',30,100,'N(pfo)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_cos_final',-1,1,'cos theta', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_cos_final',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_BDT_score_final',-0.80,0.20,'BDT score', combine_opt, flag_zz, log_opt_f)

    if (combine_opt == 3):
	if (flag_zz == 1):
            draw_signal_bg('h_dimuon_rec_m_raw',80,240,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dijet_rec_m_raw',110,140,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_rec_m_raw',0,140,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_p_raw',0,100,'Visible p(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_pt_raw',0,100,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_m_raw',80,220,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dimuon_m_raw',0,80,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dijet_m_raw',75,105,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_lead_e_raw',40,110,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_lead_pt_raw',0,100,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_sub_e_raw',0,70,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_sub_pt_raw',0,60,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dimuon_dijet_angle_raw',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_n_col_reco_raw',40,95,'N(pfo)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_cos_raw',-1,1,'cos theta', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_cos_raw',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_BDT_score_raw',-0.50,0.10,'BDT score', combine_opt, flag_zz, log_opt_r)

            draw_signal_bg('h_dimuon_rec_m_final',80,240,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_rec_m_final',110,140,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_rec_m_final',0,140,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_p_final',0,100,'Visible p(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_pt_final',0,100,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_m_final',80,220,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_m_final',0,80,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_m_final',75,105,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_e_final',40,110,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_pt_final',0,100,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_e_final',0,70,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_pt_final',0,60,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_dijet_angle_final',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_n_col_reco_final',40,95,'N(pfo)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_cos_final',-1,1,'cos theta', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_cos_final',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_BDT_score_final',-0.50,0.10,'BDT score', combine_opt, flag_zz, log_opt_f)

	if (flag_zz == 2):
            draw_signal_bg('h_dimuon_rec_m_raw',60,200,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dijet_rec_m_raw',110,140,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_rec_m_raw',-50,80,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_p_raw',0,120,'Visible p(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_pt_raw',0,100,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_m_raw',130,250,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dimuon_m_raw',0,160,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dijet_m_raw',75,105,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_lead_e_raw',40,110,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_lead_pt_raw',0,100,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_sub_e_raw',0,70,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_jet_sub_pt_raw',0,70,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_dimuon_dijet_angle_raw',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_n_col_reco_raw',40,95,'N(pfo)', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_cos_raw',-1,1,'cos theta', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_vis_all_cos_raw',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_r)
            draw_signal_bg('h_BDT_score_raw',-0.70,0.10,'BDT score', combine_opt, flag_zz, log_opt_r)

            draw_signal_bg('h_dimuon_rec_m_final',60,200,'Dimuon rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_rec_m_final',110,140,'Dijet rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_rec_m_final',-50,80,'Visible rec mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_p_final',0,120,'Visible p(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_pt_final',0,100,'Visible pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_m_final',130,250,'Visible mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_m_final',0,160,'Dimuon mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dijet_m_final',75,105,'Dijet mass(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_e_final',40,110,'Leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_lead_pt_final',0,100,'Leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_e_final',0,70,'Sub-leading Jet E(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_jet_sub_pt_final',0,70,'Sub-leading Jet Pt(GeV)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_dimuon_dijet_angle_final',0,180,'Angle(dimuon-dijet)(Degree)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_n_col_reco_final',40,95,'N(pfo)', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_cos_final',-1,1,'cos theta', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_vis_all_cos_final',-1,1,'cos theta_{visible}', combine_opt, flag_zz, log_opt_f)
            draw_signal_bg('h_BDT_score_final',-0.70,0.10,'BDT score', combine_opt, flag_zz, log_opt_f)

def draw_signal_bg(pic, x1, x2, title, combine_opt, flag_zz, log_opt):

    tabs = sys.argv[3:]

    c = ROOT.TCanvas('c', 'c', 800, 800)
    leg = ROOT.TLegend(0.70, 0.83, 0.95, 0.97)
    leg.SetTextFont(60)
    leg.SetTextSize(0.02)

    stack = ROOT.THStack('stack', '')

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

    figfile = save_path+'/sbg_%s.png'%pic
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
    s = signal_sample.Get(pic)
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
                    tem=sample.Get(pic)
                    a=copy.copy(tem)
                    a.Scale(scb)
                    exec('b%s.Add(a)'%tabs.index(t))

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
        s.SetMinimum(0.1)
    if (log_opt==2):
        s.SetMaximum(max*31)
    if (log_opt==1):
        s.SetMaximum(max*1.35)
    s.GetXaxis().SetRangeUser(x1, x2)
    s.SetXTitle(title)

## Plot Settings
    if 'angle' in pic:
        s.SetYTitle('Events/Degree')
    elif ('npfo' in pic) or ('cos' in pic):
        s.SetYTitle('Events')
    else:
        s.SetYTitle('Events/GeV') 

    s.GetYaxis().SetTitleOffset(1.4)
    s.GetYaxis().SetLabelFont(52)
    s.GetYaxis().SetLabelSize(0.034)
    s.GetXaxis().SetLabelFont(52)
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
