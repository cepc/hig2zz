#include "frame.h"
#include <iostream>
#include <ostream>
#include <fstream>
#include <stdio.h>
#include "TLeaf.h"
#include "TString.h"

void Plot2DhistStyle(TH2F *_h) {
  _h->GetYaxis()->SetNdivisions(10511);
  _h->GetXaxis()->SetNdivisions(511);
  _h->GetXaxis()->SetTitleOffset(0.9);
  _h->SetMinimum(0.);
  _h->SetStats(0);
}

void Make2DCorrelationPlot(TString CHANNEL, TString outputPath,TString outputName, TH2F* reco_truth_2d, bool drawText) {

  TString outputFile=outputPath+"/"+outputName;
  TCanvas *c1=new TCanvas("c1","c1",1100,800);

  c1->SetMargin(0.12, 0.18, 0.15, 0.05); // left, right, down, up
  Plot2DhistStyle(reco_truth_2d);
  reco_truth_2d->SetMaximum(1);
  reco_truth_2d->SetMinimum(-1);
  reco_truth_2d->GetZaxis()->SetTitle("#rho(X,Y)");

  int NRGBs = 3, NCont = 512;
  gStyle->SetNumberContours(NCont);
  Double_t stops[NRGBs] = { 0.00, 0.50, 1.00 };
  Double_t red[NRGBs]   = { 0.20, 1.00, 1.00 };
  Double_t green[NRGBs] = { 0.20, 1.00, 0.20 };
  Double_t blue[NRGBs]  = { 1.00, 1.00, 0.20 };
  TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
  reco_truth_2d->Draw("COLZ");
  if(drawText) {
    TLatex *tex = new TLatex();
    tex->SetTextAlign(22);
    tex->SetTextSize(0.03);
    for (int x=1; x<=reco_truth_2d->GetNbinsX(); x++) {
      for (int y=1; y<=reco_truth_2d->GetNbinsY(); y++) 
	{
        if(x<=reco_truth_2d->GetNbinsY()+1-y) 
		{
			Float_t temp=reco_truth_2d->GetBinContent(x,y);	
//			if (100*fabs(temp)<1) tex->DrawLatex(reco_truth_2d->GetXaxis()->GetBinCenter(x),reco_truth_2d->GetYaxis()->GetBinCenter(y),"<1%");
//			else 
//tex->DrawLatex(reco_truth_2d->GetXaxis()->GetBinCenter(x),reco_truth_2d->GetYaxis()->GetBinCenter(y),Form("%.0f%%",100*reco_truth_2d->GetBinContent(x,y)));
tex->DrawLatex(reco_truth_2d->GetXaxis()->GetBinCenter(x),reco_truth_2d->GetYaxis()->GetBinCenter(y),Form("%.3f%%",100*temp));
cout<<setw(10)<<setiosflags(ios::fixed)<<setprecision(3)<<100*temp<<" ";
        } 
    }	
cout<<endl;
}
}
  //PlotLumi(0.6-0.3, 0.7-0.3, 0.90, 1.0, 0.035);
  TLatex *tex = new TLatex();
  tex->SetTextSize(0.05);
  tex->DrawLatexNDC(0.5, 0.85, "#bf{#it{CEPC}}");
  tex->SetTextSize(0.035);
  tex->DrawLatexNDC(0.5, 0.75, "#scale[0.6]{#int}Ldt=5.6 ab^{-1}, #sqrt{s}=240GeV");


  c1->SaveAs(outputFile+".png");
  c1->SaveAs(outputFile+".pdf");
  c1->Print(Form("%s.C",outputFile.Data()));
}

TString translateSTXS(TString varName){
  if(varName=="mu_mu") varName = "#sigma_{#it{ZH_#mu#mu}}";
  if(varName=="mu_tt") varName = "#sigma_{#it{ZH_#tau#tau}}";
  if(varName=="mu_rr") varName = "#sigma_{#it{ZH_#gamma#gamma}}";
  if(varName.BeginsWith("mu_")) { TString varName2=varName(2, varName.Length()); varName = "#sigma_{#it{ZH"+varName2+"}}"; }
  if(varName.BeginsWith("k_")) { TString varName2=varName(2, varName.Length()); varName = "#kappa_{"+varName2+"}"; }

  if(varName.BeginsWith("eeqq_")) { TString varName2=varName(4, varName.Length()); varName = "#sigma_{#it{ee"+varName2+"}}"; }
  if(varName.BeginsWith("mmqq_")) { TString varName2=varName(4, varName.Length()); varName = "#sigma_{#it{#mu#mu"+varName2+"}}"; }
  if(varName.BeginsWith("qqqq_")) { TString varName2=varName(4, varName.Length()); varName = "#sigma_{#it{qq"+varName2+"}}"; }
  if(varName.BeginsWith("vvqq_")) { TString varName2=varName(4, varName.Length()); varName = "#sigma_{#it{#nu#nu"+varName2+"}}"; }

  if(varName=="zhbb") varName = "#sigma_{#it{ZH_bb}}";
  if(varName=="vvbb") varName = "#sigma_{#it{ZH_vvbb}}";
  if(varName=="vvhbb") varName = "#sigma_{#it{vvH->vvbb}}";
  
  return varName;
}

int main (int argc, char **argv) {

  TString CHANNEL=argv[1];
  TString pois;
 
  SetAtlasStyle();

  vector<TString> vPOIs;
 
  if(argc>2) pois=argv[2];
  if (pois != "") {
    vector<TString> poilist = SplitString( pois, ',' );
    for (UInt_t i=0; i<poilist.size(); i++) {
      vector<TString> rangelist = SplitString( poilist[i], '=' );
      if(rangelist.size()>0) vPOIs.push_back(rangelist[0]); 
    }
  }

  cout<<"Now working with channel "<<CHANNEL<<", poi "<<pois<<endl;

  TString inputFileName="outs/singleFit/singleFit_"+CHANNEL+".root";
 
  TFile *inputFile=TFile::Open(inputFileName,"read");
  RooFitResult *result=(RooFitResult*)inputFile->Get("fitResult");

  TH1::SetDefaultSumw2();

  gStyle->SetLabelSize(0.06, "X"); 
  gStyle->SetLabelSize(0.06, "Y"); 

  TH2F* correlationPOI=new TH2F("correlationPOI","correlationPOI",vPOIs.size(), 1, vPOIs.size()+1, vPOIs.size(), 1, vPOIs.size()+1);

  for(unsigned int ivPOIs=1;ivPOIs<vPOIs.size()+1;ivPOIs++) {
    TString xname=vPOIs[vPOIs.size()-ivPOIs];
    xname.ReplaceAll("r_","");
    correlationPOI->GetXaxis()->SetBinLabel(ivPOIs,xname);

    TString xnamelabel=translateSTXS(vPOIs[vPOIs.size()-ivPOIs]);
    correlationPOI->GetXaxis()->SetBinLabel(ivPOIs,xnamelabel);
    correlationPOI->GetXaxis()->SetLabelOffset(0.01);
    correlationPOI->GetXaxis()->LabelsOption("v");
  }

  for(unsigned int ivPOIs=1;ivPOIs<vPOIs.size()+1;ivPOIs++) {
    TString yname=vPOIs[ivPOIs-1];
    yname.ReplaceAll("r_","");
    correlationPOI->GetYaxis()->SetBinLabel(ivPOIs,yname);

    TString ynamelabel=translateSTXS(vPOIs[ivPOIs-1]);
    correlationPOI->GetYaxis()->SetBinLabel(ivPOIs,ynamelabel);
    correlationPOI->GetYaxis()->SetLabelOffset(0.01);
  }

  for(unsigned int ivPOIy=1;ivPOIy<vPOIs.size()+1;ivPOIy++) {
    for(unsigned int ivPOIx=1;ivPOIx<vPOIs.size()+1;ivPOIx++) {
    	correlationPOI->SetBinContent(vPOIs.size()+1-ivPOIx, ivPOIy, result->correlation(vPOIs[ivPOIx-1],vPOIs[ivPOIy-1]));
    	if(ivPOIx<ivPOIy) correlationPOI->SetBinContent(vPOIs.size()+1-ivPOIx, ivPOIy,0.0);
    }
  }
  //correlationPOI->Print("all");
  system("mkdir -vp outs/correlation/");
  TString outputPath="outs/correlation/";

  TString outfname="correlation_"+CHANNEL;
  Make2DCorrelationPlot(CHANNEL,outputPath,outfname,correlationPOI, true);
  std::cout<<"good"<<std::endl;

  return 0;
}
