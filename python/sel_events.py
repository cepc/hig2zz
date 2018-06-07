#!/usr/bin/env python
"""
Event Selection

## Inspired from an event selection script for J/psi->invisible
"""

__author__ = "R. Kiuchi <kiuchi@ihep.ac.cn>"
__copyright__ = "Copyright (c) Ryuta Kiuchi"
__created__ = "[2018-06-06       ]" 

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

# Global histograms

h_evtflw = ROOT.TH1F('hevtflw','eventflow',15,0,15)
h_evtflw.GetXaxis().SetBinLabel(1,'raw')
h_evtflw.GetXaxis().SetBinLabel(2,'N(jet)=2')
h_evtflw.GetXaxis().SetBinLabel(3,'Di-Jet Invariant Mass Cut')
h_evtflw.GetXaxis().SetBinLabel(4,'N(l+)=1 & N(l-)=1')
h_evtflw.GetXaxis().SetBinLabel(5,'N_{#gamma}<=1')
h_evtflw.GetXaxis().SetBinLabel(6,'10GeV<P_{t}^{e^{+}e^{-}}<70GeV')
h_evtflw.GetXaxis().SetBinLabel(7,'|P_{z}^{e^{+}e^{-}}|<60GeV')
h_evtflw.GetXaxis().SetBinLabel(8,'|cos#theta_{e^{+}e^{-}}|<0.8')
h_evtflw.GetXaxis().SetBinLabel(9,'90GeV<|Visible Energy|<120GeV')
h_evtflw.GetXaxis().SetBinLabel(10,'70GeV<|M_{e^{+}e^{-}}|<100GeV')


h_invmass_ll = ROOT.TH1D('h_invmass_ll', 'invmass_ll', 260, 0, 260)
h_recoil_ll = ROOT.TH1D('h_recoil_ll', 'recoil_ll', 260, 0, 260)

h_invmass_jj_fast = ROOT.TH1D('h_invmass_jj_fast', 'invmass_jj_fast', 260, 0, 260)
h_recoil_jj_fast = ROOT.TH1D('h_recoil_jj_fast', 'recoil_jj_fast', 260, 0, 260)

h_invmass_jj_lcfi = ROOT.TH1D('h_invmass_jj_lcfi', 'invmass_jj_lcfi', 260, 0, 260)
h_recoil_jj_lcfi = ROOT.TH1D('h_recoil_jj_lcfi', 'recoil_jj_lcfi', 260, 0, 260)

h_recoil_jjll_fast = ROOT.TH1D('h_recoil_jjll_fast', 'recoil_jjll_fast', 260, 0, 260)
h_recoil_jjll_lcfi = ROOT.TH1D('h_recoil_jjll_lcfi', 'recoil_jjll_lcfi', 260, 0, 260)



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

	args=sys.argv[1:]
	if len(args)<2:
		return usage()

	infile=args[0]
	outfile=args[1]

	fin=ROOT.TFile(infile)
	t_in=fin.Get('MCPart')
	entries=t_in.GetEntriesFast()

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
		
		if select_higgs_to_zz(t_in): 

			# Fill to histogram
			h_invmass_ll.Fill(t_in.m_m_visble)
			h_recoil_ll.Fill(t_in.m_m_recoil)
			
			h_invmass_jj_fast.Fill(t_in.m_invMass_FastJet)
			h_recoil_jj_fast.Fill(t_in.m_recoil_fast_jet)
			
			h_invmass_jj_lcfi.Fill(t_in.m_invMass_LcfiJet)
			h_recoil_jj_lcfi.Fill(t_in.m_recoil_lcfi_jet)
			
			h_recoil_jjll_lcfi.Fill(t_in.m_recoil_lcfijj_ll)
			h_recoil_jjll_fast.Fill(t_in.m_recoil_fastjj_ll)
		
		
	write_histograms()
	fout.Close()
	pbar.finish()
	
	# dur = time()-time_start
	dur = duration(time()-time_start)
	sys.stdout.write(' \nDone in %s. \n' % dur)

def write_histograms():
	
	h_evtflw.Write()

	h_invmass_ll.Write()
	h_recoil_ll.Write()

	h_invmass_jj_fast.Write()
	h_recoil_jj_fast.Write()

	h_invmass_jj_lcfi.Write()
	h_recoil_jj_lcfi.Write()

	h_recoil_jjll_fast.Write()
	h_recoil_jjll_lcfi.Write()
	

def select_higgs_to_zz(t_in):
	h_evtflw.Fill(0)
		
	# N(jet)=2
	if not (t_in.m_nlcfijet == 2):
	       	return False
	h_evtflw.Fill(1)

	# Invariant mass of Z (decays to di-jets) ## Not Used !
	if not (t_in.m_m_visble>70 and t_in.m_m_visble<100): 
	       	return False
	h_evtflw.Fill(2)

	# N(l+)=1, N(l-)=1
	if not ( t_in.m_n_leptonp==1 and t_in.m_n_leptonm==1):
		return False
	h_evtflw.Fill(3)
		
	# N(gamma)=0
	if not (t_in.m_n_gamma<=1):
		return False	
	h_evtflw.Fill(4)

	# 10 < Pt(di-lepton) < 70 
	if not (t_in.m_pt_dilepton>10 and t_in.m_pt_dilepton<70):
		return False
	h_evtflw.Fill(5)                                   
        	                          
	# Pz(di-lepton) < 60
	if not (abs(t_in.m_p_dilepton[2])<60):                
		return False
	h_evtflw.Fill(6)                                   

	# cos(theta) < 0.8
	TotalP=math.sqrt(t_in.m_p_charged[3]*t_in.m_p_charged[3]-t_in.m_p_charged[0]*t_in.m_p_charged[0]-t_in.m_p_charged[1]*t_in.m_p_charged[1]-t_in.m_p_charged[2]*t_in.m_p_charged[2])
	TotalPz=t_in.m_p_charged[2]
	if TotalP!=0:
		costheta=TotalPz/TotalP
	if not (abs(costheta)<0.8):
		return False
	h_evtflw.Fill(7)

	# Energy of Z (decays to di-lepton) 
	if not (t_in.m_energy_visble>90 and t_in.m_energy_visble<120):
		return False
	h_evtflw.Fill(8)

	# Invariant mass of Z (decays to di-lepton)
	if not (t_in.m_m_visble>70 and t_in.m_m_visble<100):
		return False
	h_evtflw.Fill(9)

	return True


if __name__ == '__main__':
	main()
