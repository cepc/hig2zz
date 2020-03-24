#!/usr/bin/env python

import sys
import os
import random
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import ROOT

import imblearn
from imblearn.combine import SMOTETomek
from imblearn.over_sampling import SMOTE

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
    BDT_pre.py

SYNOPSIS

    ./BDT_pre.py infile outfile combine_opt (1: llhzz, 2: nnhzz, 3: qqhzz) flag_zz (1: vv jj/ll, 2: jj/ll vv)

AUTHOR
    Min Zhong <zmind@mail.ustc.edu.cn>

DATE
    November 2019
\n''')

def main():

    args = sys.argv[1:]
    if len(args) < 2:
        return usage()

    combine_opt = int(args[0])
    flag_zz = int(args[1])

    # get root files and convert them to array
    if (combine_opt == 1):
        branch_names = """dijet_rec_m,vis_all_p,vis_all_pt,vis_all_m,dijet_m,jet_lead_e,jet_sub_e,dimuon_dijet_angle,n_col_reco,dimuon_m,cos,vis_all_rec_m""".split(",")
        fin1 = ROOT.TFile("./sample/channel_ll_"+args[1]+"/Before/signal.root")
        fin2 = ROOT.TFile("./sample/channel_ll_"+args[1]+"/Before/bkg_all.root")

    if (combine_opt == 2):
        branch_names = """dimuon_rec_m,dijet_rec_m,vis_all_p,vis_all_pt,dijet_m,jet_lead_e,jet_sub_e,dimuon_dijet_angle,n_col_reco,dimuon_m,cos,vis_all_rec_m""".split(",")
        fin1 = ROOT.TFile("./sample/channel_nn_"+args[1]+"/Before/signal.root")
        fin2 = ROOT.TFile("./sample/channel_nn_"+args[1]+"/Before/bkg_all.root")

    if (combine_opt == 3):
        branch_names = """dimuon_rec_m,vis_all_p,vis_all_pt,vis_all_m,dijet_m,jet_lead_e,jet_sub_e,dimuon_dijet_angle,n_col_reco,dimuon_m,cos,vis_all_rec_m""".split(",")
        fin1 = ROOT.TFile("./sample/channel_qq_"+args[1]+"/Before/signal.root")
        fin2 = ROOT.TFile("./sample/channel_qq_"+args[1]+"/Before/bkg_all.root")

    tree1 = fin1.Get("tree")
    signal = tree1.AsMatrix(columns=branch_names)
    tree2 = fin2.Get("tree")
    backgr = tree2.AsMatrix(columns=branch_names)

    # for sklearn data is usually organised into one 2D array of shape (n_samples * n_features)
    # containing all the data and one array of categories of length n_samples
    X_raw = np.concatenate((signal, backgr))
    y_raw = np.concatenate((np.ones(signal.shape[0]), np.zeros(backgr.shape[0])))

    n_sig = len(y_raw[y_raw==1])
    n_bkg = len(y_raw[y_raw==0])
    sb_ratio = len(y_raw[y_raw==1])/(1.0*len(y_raw[y_raw==0]))
    if (sb_ratio > 0.2 and sb_ratio < 0.5):
        smote = SMOTE(ratio=0.5)
        X, y = smote.fit_sample(X_raw, y_raw)
        print ('Number of events: ')
        print ('before: signal: ', len(y_raw[y_raw==1]), ' background: ', len(y_raw[y_raw==0]))
        print ('after: signal: ', len(y[y==1]), ' background: ', len(y[y==0]))
    elif (n_sig > 1000 and sb_ratio < 0.2 and sb_ratio > 0.1):
        smote = SMOTE(ratio=0.2)
        X, y = smote.fit_sample(X_raw, y_raw)
        print ('Number of events: ')
        print ('before: signal: ', len(y_raw[y_raw==1]), ' background: ', len(y_raw[y_raw==0]))
        print ('after: signal: ', len(y[y==1]), ' background: ', len(y[y==0]))
    elif (n_sig < 1000 and sb_ratio < 0.2 and sb_ratio > 0.1):
        smote = SMOTE(ratio=0.4)
        X, y = smote.fit_sample(X_raw, y_raw)
        print ('Number of events: ')
        print ('before: signal: ', len(y_raw[y_raw==1]), ' background: ', len(y_raw[y_raw==0]))
        print ('after: signal: ', len(y[y==1]), ' background: ', len(y[y==0]))
    elif (sb_ratio < 0.1):
        smote = SMOTE(ratio=0.15)
        X, y = smote.fit_sample(X_raw, y_raw)
        print ('Number of events: ')
        print ('before: signal: ', len(y_raw[y_raw==1]), ' background: ', len(y_raw[y_raw==0]))
        print ('after: signal: ', len(y[y==1]), ' background: ', len(y[y==0]))
    else:
        X = X_raw
        y = y_raw

    """
    Training Part
    """
    # Train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=318)

    if (combine_opt == 1):
        if (flag_zz == 1):
            dt = DecisionTreeClassifier(max_depth=1, min_samples_leaf=10, min_samples_split=20)
        if (flag_zz == 2):
            dt = DecisionTreeClassifier(max_depth=2, min_samples_leaf=10, min_samples_split=20)
    if (combine_opt == 2):
        dt = DecisionTreeClassifier(max_depth=1, min_samples_leaf=10, min_samples_split=20)
    if (combine_opt == 3):
        if (flag_zz == 1):
            dt = DecisionTreeClassifier(max_depth=1, min_samples_leaf=10, min_samples_split=20)
        if (flag_zz == 2):
            dt = DecisionTreeClassifier(max_depth=1, min_samples_leaf=10, min_samples_split=20)

    bdt = AdaBoostClassifier(dt, algorithm='SAMME', n_estimators=800, learning_rate=0.5)
    bdt.fit(X_train, y_train)

    importances = bdt.feature_importances_
    print (importances)

    y_predicted = bdt.predict(X_train)
    print (classification_report(y_train, y_predicted, target_names=["background", "signal"]))
    print ("Area under ROC curve: %.4f"%(roc_auc_score(y_train, bdt.decision_function(X_train))))

    y_predicted = bdt.predict(X_test)
    print (classification_report(y_test, y_predicted, target_names=["background", "signal"]))
    print ("Area under ROC curve: %.4f"%(roc_auc_score(y_test, bdt.decision_function(X_test))))

    decisions1 = bdt.decision_function(X_train)
    decisions2 = bdt.decision_function(X_test)

    if (combine_opt == 1):
        if (flag_zz == 1):
            filepath = 'channel_ll_1'
        if (flag_zz == 2):
            filepath = 'channel_ll_2'
    if (combine_opt == 2):
        filepath = 'channel_nn_1'
    if (combine_opt == 3):
        if (flag_zz == 1):
            filepath = 'channel_qq_1'
        if (flag_zz == 2):
            filepath = 'channel_qq_2'

    # Compute ROC curve and area under the curve
    fpr1, tpr1, thresholds1 = roc_curve(y_train, decisions1)
    fpr2, tpr2, thresholds2 = roc_curve(y_test, decisions2)
    roc_auc1 = auc(fpr1, tpr1)
    roc_auc2 = auc(fpr2, tpr2)
    fig=plt.figure(figsize=(8,6))
    fig.patch.set_color('white')
    plt.plot(fpr1, tpr1, lw=1.2, label='train:ROC (area = %0.4f)'%(roc_auc1), color="r")
    plt.plot(fpr2, tpr2, lw=1.2, label='test: ROC (area = %0.4f)'%(roc_auc2), color="b")
    plt.plot([0,1], [0,1], '--', color=(0.6, 0.6, 0.6), label = 'Luck')
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating  characteristic')
    plt.legend(loc = "lower right")
    plt.grid()
    plt.savefig('./bdt_results/'+filepath+'/ROC.png')
#    plt.show()

    compare_train_test(bdt, X_train, y_train, X_test, y_test, filepath)

    joblib.dump(bdt, './bdt_results/'+filepath+'/bdt_model.pkl')

# Comparing train and test results
def compare_train_test(clf, X_train, y_train, X_test, y_test, savepath, bins=30):

    decisions = []
    for X,y in ((X_train, y_train), (X_test, y_test)):
        d1 = clf.decision_function(X[y>0.5]).ravel()
        d2 = clf.decision_function(X[y<0.5]).ravel()
        decisions += [d1, d2]

    low = min(np.min(d) for d in decisions)
    high = max(np.max(d) for d in decisions)
    low_high = (low, high)
    fig=plt.figure(figsize=(8,5.5))
    fig.patch.set_color('white')
    plt.hist(decisions[0], color='r', alpha=0.5, range=low_high, bins=bins, histtype='stepfilled', density = True, label='Signal (train)')
    plt.hist(decisions[1], color='b', alpha=0.5, range=low_high, bins=bins, histtype='stepfilled', density = True, label='Background (train)')
    
    hist, bins = np.histogram(decisions[2], bins=bins, range=low_high, density=True)
    scale = len(decisions[2])/sum(hist)
    err = np.sqrt(hist*scale)/scale

    width = (bins[1]-bins[0])
    center = (bins[:-1]+bins[1:])/2
    plt.errorbar(center, hist, yerr=err, fmt='o', c='r', label='Signal (test)')

    hist, bins = np.histogram(decisions[3], bins=bins, range=low_high, density=True)
    scale = len(decisions[2])/sum(hist)
    err = np.sqrt(hist*scale)/scale

    plt.errorbar(center, hist, yerr=err, fmt='o', c='b', label='Background (test)')
  
    plt.xlabel("BDT score")
    plt.ylabel("Normalized Unit")
    plt.legend(loc='best')
    plt.savefig("./bdt_results/"+savepath+"/BDTscore.png")
#    plt.show()

if __name__ == '__main__':
        main()
