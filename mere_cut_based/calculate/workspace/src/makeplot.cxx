#include "head.h"
#include "TDatime.h"
using namespace std;
using namespace RooFit;
#include "shapeFit.h"
#include "CEPCCDRstyle.h"
string time_str;
  
TString part="part";
bool import=true;
const int ch = 6;
const TString CN[ch] = {"mzvj","mzjv","vzmj","vzjm","qzvm","qzmv"};

void plotFit(RooWorkspace *wchannel,  channel c, TString proc, TString lu_n) 
{
    SetCEPCCDRStyle();
    TString cname=c.name;
    TString e_cname= namesetting(cname);
    TString e_m    =xnamesetting(cname);
    TString e_rec  = xrecsetting(cname);
    
    checkcname(cname);

    TString ECM="240"; 
    cout<<"begin to plot "<<cname<<" "<<endl;
    TString e_proc=proc;
    if (proc=="s") e_proc="Signal";
    //if (proc=="b") e_proc="SM Background";
    if (proc=="b") e_proc="SM Background";
    
    TCanvas *canvas = new TCanvas("c1", "c1", 800, 800);
    canvas->SetMargin(0.16, 0.04, 0.11, 0.02); // left, right, bottom, top
    gPad->SetTicks(1,1);
    RooPlot *frame;

    frame = (*wchannel->var("invMass_" + cname)).frame(25);
   
    wchannel->data("AsimovSB")->plotOn(frame,DataError(RooAbsData::Poisson),XErrorSize(0),MarkerSize(2));          
    wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("Fit"), LineColor(4));
    wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name(proc),  Components((*wchannel->pdf("pdf_"+proc+"_" + cname))), LineColor(kRed), LineStyle(2));//s
/*    wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"), Components((*wchannel->pdf("pdf_b_" + cname))), LineColor(kGreen), LineStyle(2));//sm bkg
    if (cname.Contains("mzvj"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("zh"), Components((RooArgSet(*wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_tt_" + cname), *wchannel->pdf("pdf_ww_" + cname)))), LineColor(kOrange), LineStyle(2));//zh bkg
    if (cname.Contains("mzjv"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("zh"), Components((RooArgSet(*wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_tt_" + cname), *wchannel->pdf("pdf_ww_" + cname), *wchannel->pdf("pdf_bb_" + cname), *wchannel->pdf("pdf_cc_" + cname), *wchannel->pdf("pdf_gg_" + cname)))), LineColor(kOrange), LineStyle(2));    
    if (cname.Contains("vzmj"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("zh"), Components((RooArgSet(*wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_ww_" + cname)))), LineColor(kOrange), LineStyle(2));
    if (cname.Contains("vzjm"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("zh"), Components((RooArgSet(*wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_tt_" + cname), *wchannel->pdf("pdf_ww_" + cname), *wchannel->pdf("pdf_bb_" + cname)))), LineColor(kOrange), LineStyle(2));
    if (cname.Contains("qzvm"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("zh"), Components((RooArgSet(*wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_tt_" + cname), *wchannel->pdf("pdf_ww_" + cname), *wchannel->pdf("pdf_bb_" + cname)))), LineColor(kOrange), LineStyle(2));
    if (cname.Contains("qzmv"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("zh"), Components((RooArgSet(*wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_tt_" + cname), *wchannel->pdf("pdf_ww_" + cname), *wchannel->pdf("pdf_bb_" + cname), *wchannel->pdf("pdf_cc_" + cname), *wchannel->pdf("pdf_gg_" + cname)))), LineColor(kOrange), LineStyle(2));
*/

    if (cname.Contains("mzvj"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"), Components((RooArgSet(*wchannel->pdf("pdf_b_" + cname), *wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_tt_" + cname), *wchannel->pdf("pdf_ww_" + cname)))), LineColor(kGreen), LineStyle(2));// bkg
    if (cname.Contains("mzjv"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"), Components((RooArgSet(*wchannel->pdf("pdf_b_" + cname), *wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_tt_" + cname), *wchannel->pdf("pdf_ww_" + cname), *wchannel->pdf("pdf_bb_" + cname), *wchannel->pdf("pdf_cc_" + cname), *wchannel->pdf("pdf_gg_" + cname)))), LineColor(kGreen), LineStyle(2));
    if (cname.Contains("vzmj"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"), Components((RooArgSet(*wchannel->pdf("pdf_b_" + cname), *wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_ww_" + cname)))), LineColor(kGreen), LineStyle(2));
    if (cname.Contains("vzjm"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"), Components((RooArgSet(*wchannel->pdf("pdf_b_" + cname), *wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_tt_" + cname), *wchannel->pdf("pdf_ww_" + cname), *wchannel->pdf("pdf_bb_" + cname)))), LineColor(kGreen), LineStyle(2));
    if (cname.Contains("qzvm"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"), Components((RooArgSet(*wchannel->pdf("pdf_b_" + cname), *wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_tt_" + cname), *wchannel->pdf("pdf_ww_" + cname), *wchannel->pdf("pdf_bb_" + cname)))), LineColor(kGreen), LineStyle(2));
    if (cname.Contains("qzmv"))
        wchannel->pdf("modelSB_" + cname)->plotOn(frame, Name("bkg"), Components((RooArgSet(*wchannel->pdf("pdf_b_" + cname), *wchannel->pdf("pdf_zz_" + cname), *wchannel->pdf("pdf_tt_" + cname), *wchannel->pdf("pdf_ww_" + cname), *wchannel->pdf("pdf_bb_" + cname), *wchannel->pdf("pdf_cc_" + cname), *wchannel->pdf("pdf_gg_" + cname)))), LineColor(kGreen), LineStyle(2));

    frame->SetTitle(""); 

    TString ytitle=frame->GetYaxis()->GetTitle();
    ytitle.Remove(8,2);
    ytitle.Remove(ytitle.Length()-1,1);
    if (!cname.Contains("imp")) ytitle+=" GeV";
    cout<<"Prime:"<<ytitle<<endl;
    frame->SetYTitle(ytitle);
    frame->SetXTitle("M_{#kern[-0.8]{ }"+e_m+"}^{#kern[-0.8]{ }"+e_rec+"}#kern[-0.5]{ }[GeV]");   

    FormatAxis(frame->GetYaxis(), 1.0);
    FormatAxis(frame->GetXaxis(), 0.9);
    
    frame->GetXaxis()->SetTitleSize(40);
    frame->SetMinimum(0.);
    frame->SetStats(0);

    if ( SetPlotMaximum(cname) )  frame->SetMaximum(PlotMaximum); 

    if ( frame->GetMaximum()<=1)   frame->GetYaxis()->SetTitleOffset(1.55);
    if ( frame->GetMaximum()>=1e2) frame->GetYaxis()->SetTitleOffset(1.25);
    if ( frame->GetMaximum()>=1e3) frame->GetYaxis()->SetTitleOffset(1.55);
    if ( frame->GetMaximum()>=1e4) frame->GetYaxis()->SetTitleOffset(1.85);
    
    frame->GetYaxis()->ChangeLabel(1, -1, 0); //after ROOT version 6.07/07: 去掉最下方0
    frame->Draw();

    Float_t lxmin,lxmax,lymin,lymax, tx,ty;
    tx=0.6;      ty=0.78;
    lxmin=0.2;   lymin=0.76; 
    int n_ent=4;
    if (cname.Contains("mzvj"))
    {
        lxmin= 0.6; lymin=0.4; 
    }

    lymax=lymin+0.05*n_ent;
    lxmax=lxmin+0.2;
    TLegend *legend = new TLegend(lxmin, lymin, lxmax, lymax);
    FormatLegend(legend);
        legend->AddEntry("MCdata","CEPC Simulation","P");
        legend->AddEntry("Fit","S+B Fit","L");

        legend->AddEntry(proc , e_proc,          "L"); 
        //legend->AddEntry("bkg", "SM Background", "L"); //always be last
        legend->AddEntry("bkg", "Background", "L");
	//legend->AddEntry("zh",  "ZH Background", "L");
    legend->Draw("same");

    TLatex *tex = new TLatex();
    FormatLatex(tex);
        tex->DrawLatexNDC(tx, ty+0.14, "#bf{CEPC Preliminary}");
        if ( cname.Contains("zhaoh")) tex->DrawLatexNDC(tx, ty+0.09, "CEPC-v4, "+ECM+" GeV");
        else tex->DrawLatexNDC(tx, ty+0.09, "5.6 ab^{-1}, "+ECM+" GeV");
        tex->DrawLatexNDC(tx, ty+0.04, e_cname);

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
    TString ECM="240"; 

    TCanvas *canvas = new TCanvas("c","c", 1200, 1200);   //X, Y
    canvas->cd();
    canvas->SetMargin(0.02, 0.02, 0.02, 0.02); // left, right, bottom, top
    
    TString e_rec=xrecsetting(cname);   
    TString e_proc=proc;
    if (proc=="s") e_proc="Signal";
    if (proc=="b") e_proc="SM background";

    TPad *pad1 = new TPad("pad1", "pad1", 0, 0.3, 1, 1.0); //xlow,ylow,xup,yup
    pad1->SetMargin(0.10, 0.02, 0, 0.02);  // left, right, bottom, top
    pad1->SetGridx();         // Vertical grid
    pad1->Draw();             // Draw the upper pad: pad1
    pad1->cd();               // pad1 becomes the current pad
    RooRealVar *hmass =(RooRealVar *)(wspace->var ("invMass"));
    RooDataSet *d_mass=(RooDataSet *)(wspace->data("d_mass_"+proc));
    RooPlot    *frame = hmass->frame(100);

    Float_t Entries=d_mass->sumEntries();
    char ent_str[9];
    sprintf(ent_str, "%6.2f", Entries);
    TString ent=e_proc+", ";
    ent+=ent_str;

    d_mass->plotOn(frame, Name(proc+"_hist"), DataError(RooAbsData::SumW2),MarkerColor(kBlack), XErrorSize(0)); 
    if (proc=="b")  (*wspace->pdf("pdf_b")    ).plotOn(frame, Name(proc), LineColor(kGreen));
    else            (*wspace->pdf("pdf_"+proc)).plotOn(frame, Name(proc), LineColor(kBlue));
    TLegend *legend = new TLegend(0.7, 0.6, 0.92, 0.88);
    
    FormatLegend(legend);
    legend->SetTextAlign(31);
    legend->SetTextSize(24);
    legend->AddEntry((TObject *)0, "#bf{#it{CEPC}}, 5.6 ab^{-1}, "+ECM+" GeV",    "");
    legend->AddEntry((TObject *)0, ent,    "");
    legend->AddEntry((TObject *)0, e_cname + ", " + e_proc,    "");

    frame->SetTitle(e_cname + ", " + e_proc);
    TString ytitle=frame->GetYaxis()->GetTitle();
    ytitle+="#scale[0.6]{[GeV]}";
    frame->SetYTitle(ytitle);
    frame->SetXTitle("[GeV]");
    frame->Draw();
    legend->Draw("same");

    frame->GetYaxis()->SetTitleFont(43);
    frame->GetYaxis()->SetTitleOffset(1.5);
    frame->GetYaxis()->ChangeLabel(1, -1, 0);
    
    canvas->cd();          // Go back to the main canvas before defining pad2
    TPad *pad2 = new TPad("pad2", "pad2", 0, 0.01, 1, 0.3);
    pad2->SetMargin(0.10, 0.02, 0.22, 0);  // left, right, bottom, top
    pad2->SetGridx(); // vertical grid
    pad2->Draw();
    pad2->cd();
    RooHist* resid=frame->pullHist(proc+"_hist",proc);
    resid->SetMarkerColor(kBlack);
    resid->SetMarkerSize(1);
    resid->SetTitle("");
    
    FormatAxis(resid->GetXaxis(),3);
    FormatAxis(resid->GetYaxis(),1);
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
    canvas->Draw();
    canvas->SaveAs((TString) "out/plots"+time_str+"/part/"+cname + "_" + proc + "_"+lu_n+".png");
    delete canvas;
    delete frame;
    delete legend;
    }
    
int main(int argc, char **argv)
{
  TString ECM="240"; 
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

for (int i=0; i<ch; i++)
//for (int i = 0; i<4; i++)
{
    //if (i==2) continue;
    TString cname=CN[i];
    cerr<<"cname: " << cname<< endl;
    if(argc>1) 
    {
        cname=argv[1];
        i=ch-1;
    }
    if (cname=="") continue;
    channel c=channelbyname(cname);
    int n_sig=c.nsig;
    TString wsname="out/workspace/" + part+ "/ws_"+cname+"_5.root";
    TString wcname="out/workspace/" + part+ "/wchannel_"+cname+"_5.root";
    TFile fs, fchannel;
    RooWorkspace *ws, *wchannel;
    if (!gSystem->AccessPathName(wsname)) 
    ws=      (RooWorkspace*)      fs.Open(wsname,"READ")->Get("wspace");
    else continue;
    if (!gSystem->AccessPathName(wcname))
    wchannel=(RooWorkspace*)      fchannel.Open(wcname,"READ")->Get("wchannel_"+cname);
    else continue;

    plotFit(wchannel,  c, "s" , "5");
    if (import)
    {
        for (int j=0; j<n_sig; j++)
        {
            plotImport(ws, c, c.name_sig[j], "5"); 
        }
        if (c.nbkg!=0) plotImport(ws, c, "b", "5"); 
    }
}
    return 0;
}

