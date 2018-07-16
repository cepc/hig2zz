#!/usr/bin/env python
"""
Event Selection

## Inspired from an event selection script for J/psi->invisible
"""

__author__ = "R. Kiuchi <kiuchi@ihep.ac.cn>"
__copyright__ = "Copyright (c) Ryuta Kiuchi"
__created__ = "[2018-06-06 ]" 

import sys
import os
import math
import ROOT
from progressbar import Bar, Percentage, ProgressBar
from array import array
from time import time
from tools import duration, check_outfile_path

#TEST=True 
TEST=False

# Global constants 
Z_MASS = 91.2

# Global histograms

h_evtflw = ROOT.TH1D('hevtflw_sel','eventflow',15,0,15)
h_evtflw.GetXaxis().SetBinLabel(1,'raw')
h_evtflw.GetXaxis().SetBinLabel(2,'M(miss)> M(dijet)')
h_evtflw.GetXaxis().SetBinLabel(3,'M(dimuon)')
h_evtflw.GetXaxis().SetBinLabel(4,'RecM(dimuon)')
h_evtflw.GetXaxis().SetBinLabel(5,'Npfo > 15')
h_evtflw.GetXaxis().SetBinLabel(6,'Total PT > 10GeV')
h_evtflw.GetXaxis().SetBinLabel(7,'Mininum angle')
h_evtflw.GetXaxis().SetBinLabel(8,'M(miss)>60GeV, M(dijet)<45GeV')

h_evtflw_pre = ROOT.TH1D('hevtflw_pre','eventflow',15,0,15)

h_m_dimuon_raw = ROOT.TH1D('h_m_dimuon_raw', 'm_dimuon_raw', 260, 0, 260)
h_mrec_dimuon_raw = ROOT.TH1D('h_mrec_dimuon_raw', 'mrec_dimuon_raw', 260, 0, 260)
h_m_dijet_raw =  ROOT.TH1D('h_m_dijet_raw', 'm_dijet_raw', 260, 0, 260)
h_mrec_dijet_raw =  ROOT.TH1D('h_mrec_dijet_raw', 'mrec_dijet_raw', 260, 0, 260)
h_m_visible_raw =  ROOT.TH1D('h_m_visible_raw', 'm_visible_raw', 260, 0, 260)
h_m_missing_raw =  ROOT.TH1D('h_m_missing_raw', 'm_missing_raw', 260, 0, 260)
h_vis_all_pt_raw =  ROOT.TH1D('h_vis_all_pt_raw', 'vis_all_pt_raw', 100, 0, 100)

h_2D_visible_missing_raw =  ROOT.TH2D('h_2D_visible_missing_raw', '2D_visible_missing_raw', 240, -20, 220, 240, -40, 200)
h_2D_dijet_missing_raw =  ROOT.TH2D('h_2D_dijet_missing_raw', '2D_dijet_missing_raw', 240, -20, 220, 240, -40, 200)

h_2D_visible_missing =  ROOT.TH2D('h_2D_visible_missing', '2D_visible_missing', 240, -20, 220, 240, -40, 200)
h_2D_dijet_missing =  ROOT.TH2D('h_2D_dijet_missing', '2D_dijet_missing', 240, -20, 220, 240, -40, 200)
h_min_angle =  ROOT.TH1D('h_min_angle', 'm_min_angle', 40, 0, 200)
h_npfo =  ROOT.TH1D('h_npfo', 'npfo', 100, 0, 100)
h_mrec_dimuon = ROOT.TH1D('h_mrec_dimuon', 'mrec_dimuon', 260, 0, 260)
h_m_dimuon = ROOT.TH1D('h_m_dimuon', 'm_dimuon', 260, 0, 260)
	
h_m_dimuon_final = ROOT.TH1D('h_m_dimuon_final', 'm_dimuon_final', 260, 0, 260)
h_mrec_dimuon_final = ROOT.TH1D('h_mrec_dimuon_final', 'mrec_dimuon_final', 260, 0, 260)



def usage():
    sys.stdout.write('''
NAME
    sel_events.py 

SYNOPSIS

    ./sel_events.py infile outfile 

AUTHOR 
    Ryuta Kiuchi  <kiuchi@ihep.ac.cn> 

DATE
    June 2018 
\n''')


def main():

    args = sys.argv[1:]
    if len(args)<2:
        return usage()

    infile = args[0]
    outfile = args[1]

    fin = ROOT.TFile(infile)
    t_in = fin.Get('tree')
    entries = t_in.GetEntriesFast()

    if entries > 0 :
        pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=entries).start()

    time_start = time()

    # output file & TTree definition
    fout = ROOT.TFile(outfile, "RECREATE")

    for jentry in xrange(entries):
        pbar.update(jentry+1)
        # get the next tree in the chain and verify
        ientry = t_in.LoadTree(jentry)
        if ientry < 0:
            break
        # copy next entry into memory and verify
		
        if TEST and ientry > 10000:
            break
		
        nb = t_in.GetEntry(jentry)
        if nb<=0:
            continue
		
        fill_histograms(t_in)

        if select_higgs_to_zz(t_in): 
            index = select_zpole_muon(t_in)
            h_m_dimuon_final.Fill( t_in.dimuon_m[index] )
            h_mrec_dimuon_final.Fill( t_in.dimuon_rec_m[index] )
		
            
    # Get event flow histogram @ Higgs2zz.cc
    copy_histo(fin, 'hevtflw', h_evtflw_pre) 
 
    # Writ histograms & Close file
    write_histograms()
    fout.Close()

    if entries > 0 :
        pbar.finish()
	
    # dur = time()-time_start
    dur = duration(time()-time_start)
    sys.stdout.write(' \nDone in %s. \n' % dur)


def copy_histo(f, hname, h_copy):
    
    h_in = f.Get(hname)
    for i in range(1, 10):
        c1 = h_in.GetBinContent(i)
        t1 = h_in.GetXaxis().GetBinLabel(i)
        h_copy.SetBinContent(i, c1)
        h_copy.GetXaxis().SetBinLabel(i,t1)


def fill_histograms(t):
    
    index = select_zpole_muon(t)

    Cut_InvMass_miss   = ( t.vis_all_rec_m > t.dijet_m[0] )
    Cut_InvMass_dimuon = ( t.dimuon_m[index] > 80.0 and t.dimuon_m[index] < 100.0 )
    Cut_RecMass_dimuon = ( t.dimuon_rec_m[index] > 120.0 and t.dimuon_rec_m[index] < 160.0 )
    Cut_npfo           = ( t.n_col_reco > 15 )
    Cut_Pt_visible     = ( t.vis_all_pt > 10 )
    Cut_Min_angle      = ( t.lj_minangle > 17.2 )
    Cut_InvMass_dijet  = ( t.vis_all_rec_m > 60 and t.dijet_m[0] <45 )

    if( Cut_InvMass_miss ):
        h_m_dimuon.Fill( t.dimuon_m[index] )

    if( Cut_InvMass_miss and Cut_InvMass_dimuon ):
        h_mrec_dimuon.Fill( t.dimuon_rec_m[index] )

    if( Cut_InvMass_miss and Cut_InvMass_dimuon and Cut_RecMass_dimuon ):
        h_npfo.Fill( t.n_col_reco )

    if( Cut_InvMass_miss and Cut_InvMass_dimuon and Cut_RecMass_dimuon and Cut_npfo and 
        Cut_Pt_visible ):
        h_min_angle.Fill( t.lj_minangle )
        
    if( Cut_InvMass_miss and Cut_InvMass_dimuon and Cut_RecMass_dimuon and Cut_npfo and 
        Cut_Pt_visible and Cut_Min_angle ):
        h_2D_visible_missing.Fill( t.vis_ex_dimuon_m, t.vis_all_rec_m )
        h_2D_dijet_missing.Fill( t.dijet_m[0] , t.vis_all_rec_m )
        
 
    # Raw histograms (  muon_p>=1, muon_m>=1, njet=2, is applied at the pre-selection ) 
    h_m_dimuon_raw.Fill( t.dimuon_m[index] )
    h_mrec_dimuon_raw.Fill( t.dimuon_rec_m[index] )
    h_m_dijet_raw.Fill( t.dijet_m[0] )
    h_mrec_dijet_raw.Fill( t.dijet_rec_m[0] )
    h_m_visible_raw.Fill( t.vis_ex_dimuon_m )
    h_m_missing_raw.Fill( t.vis_all_rec_m )
    h_vis_all_pt_raw.Fill( t.vis_all_pt )

    h_2D_visible_missing_raw.Fill( t.vis_ex_dimuon_m, t.vis_all_rec_m )
    h_2D_dijet_missing_raw.Fill( t.dijet_m[0], t.vis_all_rec_m )

def write_histograms():
	
    h_evtflw.Write()
    h_evtflw_pre.Write()

    h_m_dimuon_raw.Write()
    h_mrec_dimuon_raw.Write()
    h_m_dijet_raw.Write()
    h_mrec_dijet_raw.Write()
    h_m_visible_raw.Write()
    h_m_missing_raw.Write()
    h_vis_all_pt_raw.Write()

    h_2D_visible_missing_raw.Write()
    h_2D_dijet_missing_raw.Write()

    h_2D_visible_missing.Write()
    h_2D_dijet_missing.Write()
    h_min_angle.Write()
    h_npfo.Write()
    h_mrec_dimuon.Write()
    h_m_dimuon.Write()
	
    h_m_dimuon_final.Write()
    h_mrec_dimuon_final.Write()

def select_higgs_to_zz(t):
    
    index = select_zpole_muon(t)

    h_evtflw.Fill(0)
    
    # Select ZZ*->nunu,jj ( Z->nunu, Z*->jj ) events : Mass(missing) > Mass(dijet)
    if not ( t.vis_all_rec_m > t.dijet_m[0] ):
        return False
    h_evtflw.Fill(1)
    
    # Invariant mass of muon pairs :  80.0 GeV/c^2 < M(dimuon) < 100.0 GeV/c^2
    if not ( t.dimuon_m[index] > 80.0 and t.dimuon_m[index] < 100.0 ):
        return False
    h_evtflw.Fill(2)
    
    # Recoil mass of muon pairs : 120.0 GeV/c^2 < M_rec(dimuon) < 160.0 GeV/c^2
    if not ( t.dimuon_rec_m[index] > 120.0 and t.dimuon_rec_m[index] < 160.0 ):
        return False
    h_evtflw.Fill(3)
    
    # Number of Particle flow objects > 15 
    if not ( t.n_col_reco > 15 ):
        return False
    h_evtflw.Fill(4)
    
    # Total(visible) Pt > 10 GeV/c
    if not ( t.vis_all_pt > 10 ):
        return False
    h_evtflw.Fill(5)
    
    # Minimum angle between a muon and a jet > 0.3 rad ( == 0.3*180.0/3.141592 = 17.2 degree ) 
    if not ( t.lj_minangle > 17.2 ):
        return False
    h_evtflw.Fill(6)
    
    # Tight selection on ZZ*->nunu,jj : Mass(missing) > 60 GeV/c^2,  Mass(dijet) < 45 GeV/c^2
    if not ( t.vis_all_rec_m > 60 and t.dijet_m[0] <45 ):
        return False
    h_evtflw.Fill(7)
    
    
    # Tranverse momentum of muon pairs : 10 GeV/c < Pt(di-lepton) < 70 GeV/c
    #if not (t.dimuon_pt[0] > 10.0 and t.dimuon_pt < 70.0 ):
    #	return False
    #h_evtflw.Fill(8)                                   
    
    return True


def select_zpole_muon(t):

    nentry = t.n_muon_plus * t.n_muon_minus
    min_diff = 1000.0
    for i in range(nentry):
       if ( abs( t.dimuon_m[i] - Z_MASS ) < min_diff ):
           min_diff = abs( t.dimuon_m[i] - Z_MASS )
           index = i


    return index



if __name__ == '__main__':
	main()
