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

    args = sys.argv[1:]
    tab = open(args[0] , 'r' )

    path = args[1]

    c = ROOT.TCanvas('c', 'c', 3200, 1600)

    # draw_signal_bg(tab, path, 'h_m_dimuon_raw', c)
    # draw_signal_bg(tab, path, 'h_mrec_dimuon_raw', c)
    # draw_signal_bg(tab, path, 'h_npfo', c)
    # draw_signal_bg(tab, path, 'h_vis_all_pt', c)
    # draw_signal_bg(tab, path, 'h_min_angle', c)
    # draw_signal_bg(tab, path, 'h_single_jet1_pt', c)
    # draw_signal_bg(tab, path, 'h_single_jet2_pt', c)
    # draw_signal_bg(tab, path, 'h_single_jet1_e', c)
    draw_signal_bg(tab, path, 'h_single_jet_theta', c)
    # draw_signal_bg(tab, path, 'h_n_lepton', c)
    # draw_signal_bg(tab, path, 'h_m_dimuon_final', c)    

def draw_signal_bg(tab, path, pic, c):

    figfile = './doc/fig/sbg_%s.pdf'%pic
    check_outfile_path(figfile)

    hc = ROOT.THStack("hc","signal_bg_%s"%pic)

    signal_sample =  ROOT.TFile('./run/llh2zz/hist/ana_File_merged_1.root')

    evah = signal_sample.Get('hevtflw_pre')
    eva = evah.GetBinContent(1)
    scs = 5050 * 6.77 * 0.0266 / (eva * (6.77 / (7.04 + 6.77 + 6.75)))

    # tep = signal_sample.Get('hevtflw_sel')
    # for i in range(9):
    #     exec ("c%s = tep.GetBinContent(%s) * scs"%(i+1,i+3))



    b1 = signal_sample.Get(pic)
    b = copy.copy(b1)
    b.Scale(scs)
    b.SetFillColor(ROOT.kRed)
    hc.Add(b)

    i = 1
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0
    print("%-25s%-25s%-25s%-25s"%('name','scale','event1','event2'))
    for s_line in tab :
        if not s_line.startswith('#'):
            l = [x.strip() for x in s_line.split(',')]
            dname = l[0]
            event_exp = float(l[3])

            sample = ROOT.TFile('./run' + '/' + path + '/hist' + '/' + dname + '/' + 'ana_File_merged_1.root')
            exec ("h%s=sample.Get('hevtflw_pre')"%i)
            exec ("event_ana = h%s.GetBinContent(1)"%i)

            if event_ana != 0:
                scb = (event_exp / event_ana)
                exec ("tem%s=sample.Get(pic)"%i)
                exec ("a%s=copy.copy(tem%s)"%(i,i))
                exec ("a%s.Scale(scb)"%i)
                exec ("a%s.SetFillColor(ROOT.kBlue)"%i)
                exec ("a%s.SetLineColor(ROOT.kBlue)"%i)
                exec ("hc.Add(a%s)"%i)

                # #print information
                # tep = sample.Get('hevtflw_sel')
                # evt1 = tep.GetBinContent(3)
                # evt2 = tep.GetBinContent(11)
                # ss = round(scb,3)
                # e1 = round(evt1,3)
                # e2 = round(evt2,3)
                # print("%-25s%-25s%-25s%-25s"%(dname,ss,evt1,evt2))

                # #calculate cut flow
                # tep = sample.Get('hevtflw_sel')
                # for i in range(9):
                #     exec ("cut%s = tep.GetBinContent(%s) * scb"%(i+1,i+3))
                #     exec ("print(cut%s)"%(i+1))
                #     exec ("c%s += cut%s"%(i+1,i+1))

        i = i+1


    ROOT.gPad.SetLogy(1)
    hc.SetMinimum(0.1)

    hc.Draw()
    # hc.GetXaxis().SetLimits(0, 100)

    # # draw cut lines
    # ymax = hc.GetMaximum()
    # line1 = ROOT.TLine(80,0,80,ymax)
    # line2 = ROOT.TLine(100,0,100,ymax)
    # line1.SetLineColor(ROOT.kGreen)
    # line2.SetLineColor(ROOT.kGreen)
    # line1.Draw()
    # line2.Draw()

    c.SaveAs(figfile)  

    # print("cut1:%s\n"%c1)
    # print("cut2:%s\n"%c2)
    # print("cut3:%s\n"%c3)
    # print("cut4:%s\n"%c4)
    # print("cut5:%s\n"%c5)
    # print("cut6:%s\n"%c6)
    # print("cut7:%s\n"%c7)
    # print("cut8:%s\n"%c8)
    # print("cut9:%s\n"%c9)


if __name__ == '__main__':
    main()
