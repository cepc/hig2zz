#!/usr/bin/env python

import sys
import os
import math
import ROOT
from array import array
from time import time
from tools import duration, check_outfile_path

import pandas as pd
import pandas.core.common as com
from pandas.core.index import Index
#import pandas.plotting._tools as pdpl
from pandas.plotting import scatter_matrix

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.externals import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split

def usage():
    sys.stdout.write('''
NAME 
    add_BDTscore.py

SYNOPSIS
  
    ./add_BDTscore.py infile outfile bdt_model combine_opt (1: llhzz, 2: nnhzz, 3: qqhzz) 

AUTHOR 
    Min Zhong <zmind@mail.ustc.edu.cn>

DATE
    JULY 2019
\n''')


def main():

    args = sys.argv[1:]
    if len(args) < 4:
        return usage()

    infile = args[0]
    outfile = args[1]
    bdt_module = args[2]
    combine_opt = int(args[3])
    bdt = joblib.load(bdt_module)

    fin = ROOT.TFile(infile)
    t_in = fin.Get('tree')
    entries = t_in.GetEntriesFast()

    time_start = time()

    # output file
    fout = ROOT.TFile(outfile, "RECREATE")
    t = ROOT.TTree('tree', 'tree')

    dimuon_m =  array( 'd', [0] )
    dijet_m =  array( 'd', [0] )
    vis_all_rec_m =  array( 'd', [0] )
    n_col_reco =  array( 'i', [0] )
    cos =  array( 'd', [0] )
    vis_all_cos =  array( 'd', [0] )
    dimuon_dijet_angle =  array( 'd', [0] )
    dimuon_rec_m =  array( 'd', [0] )
    dijet_rec_m = array( 'd', [0] )
    vis_all_m =  array( 'd', [0] )
    vis_all_p =  array( 'd', [0] )
    vis_all_pt = array( 'd', [0] )
    jet_lead_e =  array( 'd', [0] )
    jet_lead_pt =  array( 'd', [0] )
    jet_sub_e =  array( 'd', [0] )
    jet_sub_pt =  array( 'd', [0] )
    BDT_score = array( 'd', [0] )

    t.Branch( 'dimuon_m', dimuon_m, 'dimuon_m/D')
    t.Branch( 'dijet_m', dijet_m, 'dijet_m/D')
    t.Branch( 'vis_all_rec_m', vis_all_rec_m, 'vis_all_rec_m/D')
    t.Branch( 'n_col_reco', n_col_reco, 'n_col_reco/I')
    t.Branch( 'cos', cos, 'cos/D')
    t.Branch( 'vis_all_cos', vis_all_cos, 'vis_all_cos/D')
    t.Branch( 'dimuon_dijet_angle', dimuon_dijet_angle, 'dimuon_dijet_angle/D')
    t.Branch( 'dimuon_rec_m', dimuon_rec_m, 'dimuon_rec_m/D')
    t.Branch( 'dijet_rec_m', dijet_rec_m, 'dijet_rec_m/D')
    t.Branch( 'vis_all_m', vis_all_m, 'vis_all_m/D')
    t.Branch( 'vis_all_p', vis_all_p, 'vis_all_p/D')
    t.Branch( 'vis_all_pt', vis_all_pt, 'vis_all_pt/D')
    t.Branch( 'jet_lead_e', jet_lead_e, 'jet_lead_e/D')
    t.Branch( 'jet_lead_pt', jet_lead_pt, 'jet_lead_pt/D')
    t.Branch( 'jet_sub_e', jet_sub_e, 'jet_sub_e/D')
    t.Branch( 'jet_sub_pt', jet_sub_pt, 'jet_sub_pt/D')
    t.Branch( 'BDT_score', BDT_score, 'BDT_score/D')

    # read trees
    for jentry in range(entries):

        #get the next tree in the chain and verify
        ientry = t_in.LoadTree(jentry)
        if ientry < 0:
            break

        # copy next entry into memory and verify
        nb = t_in.GetEntry(jentry)
        if nb<=0:
            continue

        # fill trees
        dimuon_m[0] =  t_in.dimuon_m
        dijet_m[0] = t_in.dijet_m
        vis_all_rec_m[0] = t_in.vis_all_rec_m
        n_col_reco[0] = t_in.n_col_reco
        cos[0] = t_in.cos
        vis_all_cos[0] = t_in.vis_all_cos
        dimuon_dijet_angle[0] = t_in.dimuon_dijet_angle
        dimuon_rec_m[0] =  t_in.dimuon_rec_m
        dijet_rec_m[0] = t_in.dijet_rec_m
        vis_all_m[0] = t_in.vis_all_m
        vis_all_p[0] = t_in.vis_all_p
        vis_all_pt[0] = t_in.vis_all_pt
        jet_lead_e[0] = t_in.jet_lead_e
        jet_lead_pt[0] = t_in.jet_lead_pt
        jet_sub_e[0] =  t_in.jet_sub_e
        jet_sub_pt[0] = t_in.jet_sub_pt

        # BDT score calculating
        if (combine_opt == 1):
            X_event = np.array([[t_in.dimuon_m, t_in.dijet_m, t_in.vis_all_rec_m, t_in.n_col_reco, t_in.cos, t_in.vis_all_cos, t_in.dimuon_dijet_angle, t_in.dijet_rec_m, t_in.vis_all_m, t_in.vis_all_p, t_in.vis_all_pt, t_in.jet_lead_e, t_in.jet_lead_pt, t_in.jet_sub_e, t_in.jet_sub_pt]])
        if (combine_opt == 2):
            X_event = np.array([[t_in.dimuon_m, t_in.dijet_m, t_in.vis_all_rec_m, t_in.n_col_reco, t_in.cos, t_in.vis_all_cos, t_in.dimuon_dijet_angle, t_in.dimuon_rec_m, t_in.dijet_rec_m,  t_in.vis_all_p, t_in.vis_all_pt, t_in.jet_lead_e, t_in.jet_lead_pt, t_in.jet_sub_e, t_in.jet_sub_pt]])
        if (combine_opt == 3):
            X_event = np.array([[t_in.dimuon_m, t_in.dijet_m, t_in.vis_all_rec_m, t_in.n_col_reco, t_in.cos, t_in.vis_all_cos, t_in.dimuon_dijet_angle, t_in.dimuon_rec_m, t_in.vis_all_m,  t_in.vis_all_p, t_in.vis_all_pt, t_in.jet_lead_e, t_in.jet_lead_pt, t_in.jet_sub_e, t_in.jet_sub_pt]])

        BDT_score[0] = bdt.decision_function(X_event) 

        t.Fill()
         
    fout.Write()
    fout.Close()

#    if entries > 0 :
#        pbar.finish()

    dur = round(time()-time_start)
    sys.stdout.write(' \nDone in %s seconds. \n' % dur)

if __name__ == '__main__':
        main()                                                                                                                                             
