//2018.04.01 remove some old configurations.
#include "head.h"
#include "TDatime.h"
using namespace std;
using namespace RooFit;
#include "shapeFit.h"
#include "CEPCCDRstyle.cxx"
//顺序
#include "RooGaussExp.h"
#include "RooGaussDoubleSidedExp.h"
#include "HggTwoSidedCBPdf.h"
string time_str;
  
TString part="part";
//   TString part="20180718_240";
//   TString part="20180718_250";
  bool import=true;
//   bool import=false;
  const int ch =5;
//   const int ch =2;
  const TString CN[ch] = {
    "mzjv",
    //"mzvj"
    //"vzjm"
    //"qzvm"
    //"qzmv"
  };

void plotFit(RooWorkspace *wchannel,  channel c, TString proc, TString lu_n) 
{
    SetCEPCCDRStyle();
    TString cname=c.name;
    int n_bkg=c.nbkg;
    TString e_cname= namesetting(cname);
    TString e_m    =xnamesetting(cname);
    TString e_rec  = xrecsetting(cname);
    
    checkcname(cname);
    // if (is2d) return 0;

    TString ECM="250"; 
    if (!is250) ECM="240";
    // if (DEBUG)  cerr << "Begin "<<ECM<<" workspace plot"<<endl;
    cout<<"begin to plot "<<cname<<" "<<endl;
    // if ()  proc="bb";
    if ( isbcg || cname.Contains("eeqq") ||cname.Contains("mmqq") ||cname.Contains("qqqq") ||cname.Contains("vvqq"))           proc="bb";
    if ( cname.Contains("w4q"))   proc="ww";  
    if ( istautau || cname.Contains("_imp"))               proc="tt";  
    // if ( cname.Contains("imp") )  proc="s";   
    TString e_proc=proc;
    if (proc=="s" || istautau || cname.Contains("_imp") ) e_proc="Signal";
    if (proc=="b") e_proc="Background";

    TCanvas *canvas = new TCanvas("c1", "c1", 800, 800);
    canvas->SetMargin(0.16, 0.04, 0.11, 0.02); // left, right, bottom, top
    gPad->SetTicks(1,1);
    RooPlot *frame;

    if (cname.Contains("cos")) 
    { 
        frame = (*wchannel->var("invMass_" + cname)).frame(-1,1, 20);
        frame->SetAxisRange(-1.2,1.2,"X");
        frame->SetMaximum(0.22);
    }
    else if (isbinned)         
    {
        Float_t binnumber=50;
        if (cname.Contains("imp")) binnumber=25;
        frame = (*wchannel->var("invMass_" + cname)).frame(binnumber);
    }
    else 
        frame = (*wchannel->var("invMass_" + cname)).frame(25);
    //始终先画data 再画pdf. 否则:归一化不正确; 多维pdf显示也有问题

    if (cname.Contains("zhaoh")) 
    {
        frame = (*wchannel->var("invMass_" + cname)).frame(500);
        
        wchannel->data("AsimovSB")->plotOn( frame,      DataError(RooAbsData::Poisson),XErrorSize(0), Invisible()); 
        
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("data"), LineColor(0), FillColor(kCyan), FillStyle(3060), DrawOption("f"));
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("Fit"),  LineColor(kRed), LineWidth(3));
    }
    if (!cname.Contains("cos") && (!cname.Contains("zhaoh"))) wchannel->data("AsimovSB")->plotOn(frame,DataError(RooAbsData::Poisson),XErrorSize(0),MarkerSize(2));          
        // weighted data should poisson->SumW2
        // wchannel->data("AsimovSB")->statOn(frame, What("NM"));
    if (!cname.Contains("cos") && (!cname.Contains("zhaoh")))
    {
    // if (!cname.Contains("qqzy"))
    // wchannel->data("d_tot")->plotOn(frame, DataError(RooAbsData::SumW2), XErrorSize(1),Name("MCdata"));
    // wchannel->data("d_tot")->plotOn(frame, DataError(RooAbsData::Poisson), XErrorSize(1),Name("MCdata"));
    // wchannel->data("AsimovSB")->plotOn(frame,DataError(RooAbsData::SumW2),XErrorSize(1),Name("MCdata")); 
    // wchannel->data("d_tot")->plotOn(frame, DataError(RooAbsData::SumW2), XErrorSize(1), MarkerStyle(6),Name("MCdata"));

    wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("Fit"), LineColor(4));
    wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name(proc),  Components((*wchannel->pdf("pdf_"+proc+"_" + cname))), LineColor(kRed),LineStyle(2));//s

    if ( cname.Contains("mzvj") )
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"),Components(RooArgSet( (*wchannel->pdf("pdf_zz_" + cname)), (*wchannel->pdf("pdf_ww_" + cname)),(*wchannel->pdf("pdf_tt_" + cname)),(*wchannel->pdf("pdf_zy_" + cname)),(*wchannel->pdf("pdf_b_" + cname)) )),LineColor(kGreen),LineWidth(2),LineStyle(2));
    //    }  // original code from Z. Kaili. 

    else if ( cname.Contains("mzjv") )
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"),Components(RooArgSet( (*wchannel->pdf("pdf_zz_" + cname)), (*wchannel->pdf("pdf_ww_" + cname)),(*wchannel->pdf("pdf_tt_" + cname)),(*wchannel->pdf("pdf_zy_" + cname)),(*wchannel->pdf("pdf_bb_" + cname)), (*wchannel->pdf("pdf_cc_" + cname)), (*wchannel->pdf("pdf_gg_" + cname)),(*wchannel->pdf("pdf_b_" + cname)) )),LineColor(kGreen),LineWidth(2),LineStyle(2)); 

    else if ( cname.Contains("vzjm") )
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"),Components(RooArgSet( (*wchannel->pdf("pdf_zz_" + cname)), (*wchannel->pdf("pdf_ww_" + cname)),(*wchannel->pdf("pdf_tt_" + cname)),(*wchannel->pdf("pdf_bb_" + cname)), (*wchannel->pdf("pdf_b_" + cname)) )),LineColor(kGreen),LineWidth(2),LineStyle(2));

    else if ( cname.Contains("qzvm") )
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"),Components(RooArgSet( (*wchannel->pdf("pdf_zz_" + cname)), (*wchannel->pdf("pdf_ww_" + cname)),(*wchannel->pdf("pdf_tt_" + cname)),(*wchannel->pdf("pdf_bb_" + cname)), (*wchannel->pdf("pdf_b_" + cname)) )),LineColor(kGreen),LineWidth(2),LineStyle(2));

    else if ( cname.Contains("qzmv") )
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"),Components(RooArgSet( (*wchannel->pdf("pdf_zz_" + cname)), (*wchannel->pdf("pdf_ww_" + cname)),(*wchannel->pdf("pdf_tt_" + cname)),(*wchannel->pdf("pdf_bb_" + cname)), (*wchannel->pdf("pdf_cc_" + cname)),(*wchannel->pdf("pdf_b_" + cname)) )),LineColor(kGreen),LineWidth(2),LineStyle(2));

    }   // modified.  09/20/2019
    else if (cname.Contains("cos"))
    { //cos
        wchannel->data("d_mass_s")->plotOn(frame, DataError(RooAbsData::SumW2),XErrorSize(1),Name(proc),MarkerColor(kRed));
        wchannel->data("d_mass_zh")->plotOn(frame,DataError(RooAbsData::SumW2),XErrorSize(1),Name("ZH"),MarkerColor(kMagenta));
        wchannel->data("d_mass_b")->plotOn(frame, DataError(RooAbsData::SumW2),XErrorSize(1),Name("bkg"),MarkerColor(kGreen));
    }
        if (cname.Contains("eeqq") ||cname.Contains("mmqq") ||cname.Contains("qqqq") ||cname.Contains("vvqq"))
        {
            wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("cc"),Components((*wchannel->pdf("pdf_cc_" + cname))),LineColor(kCyan),   LineWidth(2),LineStyle(2)); 
            wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("gg"),Components((*wchannel->pdf("pdf_gg_" + cname))),LineColor(kMagenta),LineWidth(2),LineStyle(2)); 
            wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"),Components(RooArgSet( (*wchannel->pdf("pdf_zz_" + cname)), (*wchannel->pdf("pdf_ww_" + cname)),(*wchannel->pdf("pdf_tt_" + cname)),(*wchannel->pdf("pdf_b_" + cname)) )),LineColor(kGreen), LineWidth(2),LineStyle(2)); 
        }
        if ( cname.Contains("w4q"))
            wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"),Components(RooArgSet( (*wchannel->pdf("pdf_bb_" + cname)), (*wchannel->pdf("pdf_cc_" + cname)), (*wchannel->pdf("pdf_gg_" + cname)), (*wchannel->pdf("pdf_zz_" + cname)),(*wchannel->pdf("pdf_b_" + cname)) )),LineColor(kGreen),LineWidth(2)); 
        if ( cname=="vvhbb")
            wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("ZH"),Components((*wchannel->pdf("pdf_zh_" + cname))),LineColor(kMagenta),LineStyle(2),LineWidth(2)); 
        if ( cname.Contains("tt") )
            wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"),Components( RooArgSet((*wchannel->pdf("pdf_ww_" + cname)), (*wchannel->pdf("pdf_b_" + cname)) )),LineColor(kGreen),LineWidth(2),LineStyle(2)); 
    frame->SetTitle(""); 
    //不设置会成为 A rooplot of…… 设为空
    // frame->SetTitleOffset(0.1); 
    // frame->SetYTitle("Entries");

    TString ytitle=frame->GetYaxis()->GetTitle();
    ytitle.Remove(8,2);
    ytitle.Remove(ytitle.Length()-1,1);
    if (!cname.Contains("imp")) ytitle+=" GeV";
    cout<<"Prime:"<<ytitle<<endl;
    frame->SetYTitle(ytitle);
    // if (cname.Contains("imp")) frame->SetYTitle("Entries");  
    frame->SetXTitle("M_{#kern[-0.8]{ }"+e_m+"}^{#kern[-0.8]{ }"+e_rec+"}#kern[-0.5]{ }[GeV]");   
    // use #kern[-0.8]{ } to control space. stupid but ……anyway
    if (cname.Contains("imp"))  frame->SetXTitle("Log_{10}(D^{2}_{0}+Z^{2}_{0})");   
    if (cname.Contains("qqzy")) frame->SetXTitle("#DeltaM#kern[-0.5]{ }[GeV]");   
    if (cname.Contains("cos")) 
    { 
      frame->SetXTitle("cos(#theta)");
      frame->SetYTitle("Arbitrary Unit"); 
      frame->SetMaximum(0.22);
    }

    FormatAxis(frame->GetYaxis(), 1.0);
    FormatAxis(frame->GetXaxis(), 0.9);
    
    frame->GetXaxis()->SetTitleSize(40);
    frame->SetMinimum(0.);
    frame->SetStats(0);

    if ( SetPlotMaximum(cname) )  frame->SetMaximum(PlotMaximum); 
    if ( cname.Contains("imp") )  frame->SetMaximum(1.5*frame->GetMaximum());

    if ( frame->GetMaximum()<=1)   frame->GetYaxis()->SetTitleOffset(1.55);
    if ( frame->GetMaximum()>=1e2) frame->GetYaxis()->SetTitleOffset(1.25);
    if ( frame->GetMaximum()>=1e3) frame->GetYaxis()->SetTitleOffset(1.55);
    if ( frame->GetMaximum()>=1e4) frame->GetYaxis()->SetTitleOffset(1.85);
    
    // frame->SetMinimum(0.01);
    // if ( frame->GetMaximum()>=1e4) frame->GetYaxis()->SetLabelSize(14);
    // if ( frame->GetMaximum()>=1e3) frame->GetYaxis()->SetLabelSize(22);
    // else if (frame->GetMaximum()>=2e2) frame->GetYaxis()->SetLabelSize(28);
    //  else TGaxis::SetMaxDigits(5);
    // frame->GetXaxis()->SetLabelSize(24);
    frame->GetYaxis()->ChangeLabel(1, -1, 0); //after ROOT version 6.07/07: 去掉最下方0
    frame->Draw();


    if (cname.Contains("cos"))
    {
        TH1 *H1=wchannel->data("d_mass_s") ->createHistogram("H1",(*wchannel->var("invMass_" + cname)), Binning(20));
        TH1 *H2=wchannel->data("d_mass_zh")->createHistogram("H2",(*wchannel->var("invMass_" + cname)), Binning(20));
        TH1 *H3=wchannel->data("d_mass_b") ->createHistogram("H3",(*wchannel->var("invMass_" + cname)), Binning(20));
        H1->SetLineColor(kRed);
        H2->SetLineColor(kMagenta);
        H3->SetLineColor(kGreen);
        H1->SetLineWidth(2);
        H2->SetLineWidth(2);
        H3->SetLineWidth(2);
        H3->Draw("same,HIST");
        H1->Draw("same,HIST");
        H2->Draw("same,HIST");
    }

    Float_t lxmin,lxmax,lymin,lymax, tx,ty;
    tx=0.6;      ty=0.78;
    lxmin=0.2;   lymin=0.76; 
    int n_ent=4;
    if (cname=="qqyy")            lymin=0.3;  //4行 高0.2
    if (cname.Contains("4v")) 
    {      
         if (cname.Contains("qz4v")  )  ty=0.2; 
        //  if (cname.Contains("m")  ){ lymin=0.3; ty=0.3; }
         if (cname.Contains("ez4v")  )  lymin=0.3; 
    }
    if (cname.Contains("eeqq") ||cname.Contains("mmqq") ||cname.Contains("qqqq") ||cname.Contains("vvqq")) { lymin= 0.66; n_ent=6; } 
    if (cname.Contains("mw") || cname.Contains("minc") || cname.Contains("ew") || cname=="mmtt" || cname=="eett"  || cname.Contains("mzvj") || cname.Contains("mzjv") || cname.Contains("vzjm") || cname.Contains("qzmv") || cname.Contains("qzvm") || cname=="mmqq" || cname=="eeqq_inv" )

    {
        lxmin= 0.6; lymin=0.4; 
        
    }
    if (cname.Contains("tt"))   { lymin-=0.05; n_ent=5; }
    // if (cname.Contains("vw4q")) lymin = 0.65;
    if (cname.Contains("vvhbb")) tx=0.62;
    if (cname.Contains("cos"))
        { lxmin= 0.22; lxmax=0.5; tx=0.55; }

    lymax=lymin+0.05*n_ent;
    lxmax=lxmin+0.2;
    TLegend *legend = new TLegend(lxmin, lymin, lxmax, lymax);
    //6.09以后可以自动设置位置
    FormatLegend(legend);
    if ( cname.Contains("cos")) 
    {
        legend->AddEntry(proc,  e_proc,   "P");
        legend->AddEntry("ZH",  "ZH bb",  "P");
        legend->AddEntry("bkg", "Background", "P");  
    } 
    else if ( cname.Contains("zhaoh"))
    {   
        if ( cname.Contains("einc")) frame->SetYTitle("A.U / 0.16 GeV"); 
        if ( cname.Contains("minc")) frame->SetYTitle("A.U / 0.1 GeV"); 
        frame->GetYaxis()->SetTitleOffset(1.85);
        legend->AddEntry("data", "CEPC Simulation",   "f"); 
        legend->AddEntry("Fit",  "Fit",   "L");
        // frame->SetMaximum(0.025); 
        // frame->Draw("same");
    }
    else 
    {
        legend->AddEntry("MCdata","CEPC Simulation","P");
        legend->AddEntry("Fit","S+B Fit","L");

        if (cname.Contains("eeqq") ||cname.Contains("mmqq") ||cname.Contains("qqqq") ||cname.Contains("vvqq"))
        {
            legend->AddEntry("bb", "H#rightarrowb#bar{b}", "L");
            legend->AddEntry("cc", "H#rightarrowc#bar{c}", "L");
            legend->AddEntry("gg", "H#rightarrowg#bar{g}", "L");
            // legend->AddEntry("wzt", "other H", "L");
        }
        else if (cname.Contains("w4q"))
        {
            legend->AddEntry("ww", "Signal", "L");
            // legend->AddEntry("bcgz", "other H", "L");
        }
        else                             legend->AddEntry(proc , e_proc,         "L"); 
        if ( cname.Contains("vvhbb"))    legend->AddEntry("ZH" , "ZH#rightarrowb#bar{b}",   "L");   
        // if ( cname.Contains("zhaoh"))    legend->AddEntry("einc","CEPC Simulation",   "f");   
        // if ( istautau || cname.Contains("imp"))                   legend->AddEntry("ww",  "H#rightarrowWW", "L");
        if ( n_bkg != 0)                 legend->AddEntry("bkg", "Background",       "L"); //always be last
    }
    legend->Draw("same");

    TLatex *tex = new TLatex();
    FormatLatex(tex);
    if (!is250) 
    {
      //tex->DrawLatexNDC(tx, ty+0.14, "#bf{CEPC CDR}");  // original code from Z. Kaili
        tex->DrawLatexNDC(tx, ty+0.14, "#bf{CEPC}");  // modified.
        // tex->DrawLatexNDC(tx, ty+0.09, "#scale[0.7]{#int}Ldt=5 ab^{-1}, #sqrt{s}="+ECM+" GeV");
        if ( cname.Contains("zhaoh")) tex->DrawLatexNDC(tx, ty+0.09, "CEPC-v4, "+ECM+" GeV");
        else tex->DrawLatexNDC(tx, ty+0.09, "5.6 ab^{-1}, "+ECM+" GeV");
        tex->DrawLatexNDC(tx, ty+0.04, e_cname);
    }
    else
    {
        tex->DrawLatexNDC(tx, ty+0.14, "#bf{CEPC 2018}");
        // tex->DrawLatexNDC(tx, ty+0.09, "#scale[0.7]{#int}Ldt=5 ab^{-1}, #sqrt{s}="+ECM+" GeV");
        tex->DrawLatexNDC(tx, ty+0.09, "5.6 ab^{-1}, "+ECM+" GeV");
        tex->DrawLatexNDC(tx, ty+0.04, e_cname);
    }
    // if (cname.Contains("inc_mi")) tex->DrawLatexNDC(tx, ty-0.01, "Model independent");
    // if (cname.Contains("inc_md")) tex->DrawLatexNDC(tx, ty-0.01, "Model dependent");

    canvas->SaveAs((TString) "out/plots"+time_str+"/f_" + cname + "_"+proc+"_"+lu_n+".png");
        
    delete canvas;
    delete frame;
    delete legend;
}
    
void plotImport(RooWorkspace *wspace, channel c, TString proc, TString lu_n)
{
    SetCEPCCDRStyle();
    TString cname=c.name;
    TString e_cname=namesetting(cname);
    TString e_m=xnamesetting(cname);
    TString ECM="250"; 
    if (!is250) ECM="240";

    TCanvas *canvas = new TCanvas("c","c", 1200, 1200);   //X, Y
    canvas->cd();
    canvas->SetMargin(0.02, 0.02, 0.02, 0.02); // left, right, bottom, top
    
    TString e_rec=xrecsetting(cname);   
    TString e_proc=proc;
    if (proc=="s") e_proc="Signal";
    if (proc=="b") e_proc="SM background";

    TPad *pad1 = new TPad("pad1", "pad1", 0, 0.3, 1, 1.0); //xlow,ylow,xup,yup
    pad1->SetMargin(0.10, 0.02, 0, 0.02);  // left, right, bottom, top
    // pad1->SetBottomMargin(0); // Upper and lower plot are joined
    pad1->SetGridx();         // Vertical grid
    pad1->Draw();             // Draw the upper pad: pad1
    pad1->cd();               // pad1 becomes the current pad
    RooRealVar *hmass =(RooRealVar *)(wspace->var ("invMass"));
    RooDataSet *d_mass=(RooDataSet *)(wspace->data("d_mass_"+proc));
    // RooAbsPdf  *pdf   =(RooAbsPdf  *)(wspace->pdf ("pdf_"   +proc));
    RooPlot    *frame = hmass->frame(100);

    Float_t Entries=d_mass->sumEntries();
    char ent_str[9];
    sprintf(ent_str, "%6.2f", Entries);
    TString ent=e_proc+", ";
    ent+=ent_str;

    // Float_t dsigma=d_mass->sigma(*hmass);
    // char sigma_str[9];
    // sprintf(sigma_str, "%6.2f", dsigma);
    // TString dsig="#sigma_{data} = ";
    // dsig+=sigma_str;

    // RooAbsMoment *moment=pdf->sigma(*hmass);
    // Float_t psigma=moment->getVal();        //2d以上pdf结果不正确
    // sprintf(sigma_str, "%6.2f", psigma);
    // TString psig="#sigma_{pdf} = ";
    // psig+=sigma_str;
    // TString sig= dsig + ", " + psig;

    d_mass->plotOn(frame, Name(proc+"_hist"), DataError(RooAbsData::SumW2),MarkerColor(kBlack), XErrorSize(0)); 
    // Now use SumW2 to see the error from the bkg stats
    // SumW2/Poisson
    //use smaller marker and more plots to see the difference
    if (proc=="b") (*wspace->pdf("pdf_b")    ).plotOn(frame, Name(proc), LineColor(kGreen));
    else           (*wspace->pdf("pdf_"+proc)).plotOn(frame, Name(proc), LineColor(kBlue));

    // Float_t chi2 = frame->chiSquare();      //和pdf无关！   (要你何用)
    // char chi2_str[9];
    // sprintf(chi2_str, "%6.2f", chi2);
    // TString chisquare2 ="#chi^{2} = ";
    // chisquare2+=chi2_str;

    TLegend *legend = new TLegend(0.7, 0.6, 0.92, 0.88);
    
    FormatLegend(legend);
    legend->SetTextAlign(31);
    legend->SetTextSize(24);
    // legend->AddEntry((TObject *)0, "#bf{#it{CEPC}}, #scale[0.5]{#int}L="+lu_n+" ab^{-1}, #sqrt{s}="+ECM+" GeV",    "");
    legend->AddEntry((TObject *)0, "#bf{#it{CEPC}}, 5.6 ab^{-1}, "+ECM+" GeV",    "");
    legend->AddEntry((TObject *)0, ent,    "");
    // legend->AddEntry((TObject *)0, sig,    "");
     legend->AddEntry((TObject *)0, e_cname + ", " + e_proc,    "");
    // legend->AddEntry((TObject *)0, chisquare2,    "");

    frame->SetTitle(e_cname + ", " + e_proc);
    TString ytitle=frame->GetYaxis()->GetTitle();
    ytitle+="#scale[0.6]{[GeV]}";
    frame->SetYTitle(ytitle);
    frame->SetXTitle("[GeV]");
    frame->Draw();
    legend->Draw("same");

    // frame->GetYaxis()->SetTitleSize(20);
    frame->GetYaxis()->SetTitleFont(43);
    frame->GetYaxis()->SetTitleOffset(1.5);
    frame->GetYaxis()->ChangeLabel(1, -1, 0);
    
    canvas->cd();          // Go back to the main canvas before defining pad2
    TPad *pad2 = new TPad("pad2", "pad2", 0, 0.01, 1, 0.3);
    pad2->SetMargin(0.10, 0.02, 0.22, 0);  // left, right, bottom, top
    pad2->SetGridx(); // vertical grid
    pad2->Draw();
    pad2->cd();
    //  RooHist* resid=frame->residHist(proc+"_hist",proc,true); which is equal to pull distribution
    RooHist* resid=frame->pullHist(proc+"_hist",proc);
    resid->SetMarkerColor(kBlack);
    resid->SetMarkerSize(1);
    resid->SetTitle("");
    
    FormatAxis(resid->GetXaxis(),3);
    FormatAxis(resid->GetYaxis(),1);
    // resid->GetYaxis()->SetLabelSize(24);
    // resid->GetYaxis()->SetTitleOffset(0.5);
    // resid->GetYaxis()->SetTitleSize(24);
    // resid->GetXaxis()->SetTitleSize(36);
    // frame->GetYaxis()->ChangeLabel(1, -1, 0);
    resid->GetYaxis()->ChangeLabel(-1, -1, 0);
    resid->GetYaxis()->SetTitle("Pull");
    resid->SetLineColor(1); 
    resid->SetLineWidth(1.2);
    resid->SetLineStyle(1);


    resid->GetXaxis()->SetLimits(c.mlow,c.mhigh);
    resid->GetXaxis()->SetTitle("M_{"+e_m+"}^{"+e_rec+"}#scale[0.6]{[GeV]}");
    if (cname.Contains("imp")) resid->GetXaxis()->SetTitle("Log_{10}(D^{2}_{0}+Z^{2}_{0})"); 
    RooCurve *s=frame->getCurve(proc);
    RooCurve f("zero","zero",*s,*s,0,0);
    f.SetLineColor(kBlue);
    if (proc=="b") f.SetLineColor(kGreen); //pull Distribution 中间那根 使用s-s来画
    resid->Draw();
    f.Draw("same");
    //
    canvas->Draw();
    canvas->SaveAs((TString) "out/plots"+time_str+"/part/"+cname + "_" + proc + "_"+lu_n+".png");
    // canvas->SaveAs((TString) "out/plots"+time_str+"/part/"+cname + "_" + proc + "_"+lu_n+".C");
    delete canvas;
    delete frame;
    delete legend;
    
    }
    
int main(int argc, char **argv)
{
        TString ECM="250"; 
    if (!is250) ECM="240";
  cerr<<"Begin "<<ECM<<" plotting"<<endl;
  TDatime time;
  int time_i=time.GetTime();
  int date_i=time.GetDate();
  string str="mkdir -vp out/plots";
  time_str=to_string(date_i) + to_string(time_i);

  str+=time_str;
  str+="/part";
  system(str.c_str());

  RooMsgService::instance().setGlobalKillBelow(RooFit::FATAL);

  //for (int i=0; i<ch; i++)   // original code from Z. Kaili. 
for (int i=0; i<Nch; i++)    // modified for easy use. The variable are defined in shapceFIt.h.  09/20/2019 
{
  //TString cname=CN[i];  // original code from Z. Kaili.
  TString cname=m_CN[i];  // modified for easy use.  The variable defined in shapceFIt.h.  09/20/2019
    if(argc>1) 
    {
        cname=argv[1];
        i=ch-1;
    }
    if (cname=="") continue;
    channel c=channelbyname(cname);
    int n_sig=c.nsig;
    // for (int j=0;j<n_sig;j++) {  }
    TString wsname="out/workspace/" + part+ "/ws_"+cname+"_5.root";
    TString wcname="out/workspace/" + part+ "/wchannel_"+cname+"_5.root";
    TFile fs, fchannel;
    RooWorkspace *ws, *wchannel;
    if (cname.Contains("cos"))
    {
        wchannel=(RooWorkspace*)      fchannel.Open(wcname,"READ")->Get("wchannel_"+cname);
        plotFit(wchannel,  c, "s" , "5");
        continue;
    }
    if (cname.Contains("qqzy"))
    {
        wchannel=(RooWorkspace*)      fchannel.Open(wcname,"READ")->Get("wchannel_"+cname);
        ws=      (RooWorkspace*)      fs.Open(wsname,"READ")->Get("wspace");
        plotFit(wchannel,  c, "s" , "5");
        if (import) plotImport(ws, c, "s", "5");
        if (import) plotImport(ws, c, "b", "5");
        continue;
    }
    if (!gSystem->AccessPathName(wsname)) 
    ws=      (RooWorkspace*)      fs.Open(wsname,"READ")->Get("wspace");
    else continue;
    if (!gSystem->AccessPathName(wcname)) 
    wchannel=(RooWorkspace*)      fchannel.Open(wcname,"READ")->Get("wchannel_"+cname);
    else continue;
    // if (fs.IsZombie()) continue;
    // else ws      =(RooWorkspace*) fs.Get("wspace");
    // if (fchannel.IsZombie()) continue;
    // else wchannel=(RooWorkspace*) fchannel.Get("wchannel_"+cname);

    plotFit(wchannel,  c, "s" , "5");
    if (import && !(cname.Contains("vvhbb")) )
    {
        for (int j=0; j<n_sig; j++)
        {
        // proc[j]  =  c.name_sig[j];
            plotImport(ws, c, c.name_sig[j], "5"); 
        }
        if (c.nbkg!=0) plotImport(ws, c, "b", "5"); 
    }
}
    return 0;
}

