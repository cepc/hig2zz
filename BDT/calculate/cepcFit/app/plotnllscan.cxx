#include "frame.h"
#include "CommonFunc.h"

using namespace std;
using namespace CommonFunc;
using namespace RooStats;

bool m_debug=false;
double median(double NLL, double minNLL)
{

  double delta_NLL = 2*fabs( NLL-minNLL ) ;
  double pvalue =  ROOT::Math::chisquared_cdf(delta_NLL,2);

  return pvalue;
}

double BinarySearch(TSpline5 *s, double target, double xmin, double xmax, double tolerance=1e-3){
  bool errlo = false, errhi = false;
  if(xmin<=s->GetXmin()) errlo = true;
  if(xmax>=s->GetXmax()) errhi = true;
  if(xmin<s->GetXmin()) {
    cout<<"Warning: input minimum is too small. Use the input spline min: "<<s->GetXmin()<<endl;
    xmin=s->GetXmin();
  }
  if(xmax>s->GetXmax()){
    cout<<"Warning: input maximu is too large. Use the input spline max: "<<s->GetXmax()<<endl;
    xmax=s->GetXmax();
  }
  if(xmin>xmax){
    cout<<"Wrong input."<<endl;
    abort();
  }
  // start binary search

  double begin = xmin;
  double end = xmax;
  double median=(end-begin)/2;
  double thisUL=s->Eval(begin);
  double endUL=s->Eval(end);

  if(thisUL<target&&endUL<target) {
    if(errlo) return xmin;
    if(errhi) return xmax;
  }

  while(fabs(thisUL-target)>tolerance){
    median=(end+begin)/2;
    if(m_debug){
      cout<<"begin = "<<begin<<" "<<s->Eval(begin)
	  <<" end = "<<end<<" "<<s->Eval(end)
	  <<" median = "<<median<<" "<<s->Eval(median)
	  <<endl;
      getchar();
    }
    thisUL=s->Eval(median);
    if((thisUL-target)*(s->Eval(end)-target)<0) begin=median;
    else if((thisUL-target)*(s->Eval(begin)-target)<0) end=median;
  }
  return median;
}

int main(int argc, char **argv){

  TString CHANNEL=argv[1];
  TString scanName=argv[2];
  Float_t rangelow=atof(argv[3]);
  Float_t rangehigh=atof(argv[4]);
  TString mode=argv[5];

  cout<<"Now working with channel "<<CHANNEL<<", poi "<<scanName<<" in range ["<<rangelow<<", "<<rangehigh<<"]..."<<endl;

  SetAtlasStyle();

  TCanvas* c = CreateCanvas("c","NLL Scan",1024,768);

  Int_t i, j, TotalConts;

  double poi[1000], nll[1000], poi_tmp[1000], nll_tmp[1000];

  int nBin=100;

  TString inputFile_min="outs/singleFit/singleFit_"+CHANNEL+".root";
  double minnll=1.00, minpoi=1.00;
  if(gSystem->AccessPathName(inputFile_min)) {
    std::cout << "File : " << inputFile_min << " does not exist, and minimum will be found in the scan."<< std::endl;
  }
  else {
    TFile *f_min=new TFile(inputFile_min,"read");
    assert(f_min);
    TTree *t_min=(TTree*)f_min->Get("nllscan");
    t_min->SetBranchAddress(scanName,&minpoi);
    t_min->SetBranchAddress("nll",&minnll);
    t_min->GetEntry(0);
    cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;
    cout<<"minimum "<<scanName<<" = "<<minpoi<<endl;
    cout<<Form("minimum NLL = %.10f", minnll)<<endl;
    cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;
    f_min->Close();
    SafeDelete(f_min);
  }

  // Load Histogram Data

  int ntotal = 0, nfail = 0;
  for (Int_t i = 0; i < nBin; i++) {
    TString inputFile=Form("outs/nllScan/"+CHANNEL+"/"+scanName+"/%d.root",i);
    if(gSystem->AccessPathName(inputFile)) {
      std::cout << "File : " << inputFile << " does not exist, and it will be ignored."<< std::endl;
      nfail++;
      continue;
    }

    TFile *f=new TFile(inputFile,"read");
    assert(f);
    TTree *t=(TTree*)f->Get("nllscan");
    double minNLL, poihat;

    t->SetBranchAddress("nll",&minNLL);
    t->SetBranchAddress(scanName,&poihat);

    t->GetEntry(0);

    if(!(minNLL==minNLL)) {
      cout<<"wrong value of minll, or reach the poi limit, this file will be ignored!"<<endl;
      nfail++;
      continue;
    }
    cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;
    cout<<"current "<<scanName<<" = "<<poihat<<endl;
    cout<<Form("current minNLL = %.10f", minNLL)<<endl;
    cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;
    nll_tmp[i-nfail]=minNLL;
    poi_tmp[i-nfail]=poihat;
    if(minNLL<minnll) {
      cout<<endl<<"WARNINING:: NLL scan gives a smaller minNLL than the minimum from single fit!!"<<endl<<endl;
//      minnll = minNLL;
//      minpoi = poihat;
    }
    f->Close();
    SafeDelete(f);
    ntotal++;
  }

  Int_t nfinal = 0;
  for (Int_t i = 0; i <ntotal; i++) {
    nll_tmp[i] =2*(nll_tmp[i]-minnll);
    if(nll_tmp[i]>5) continue;
    if(i<1) {
      poi[nfinal]=poi_tmp[i]; nll[nfinal]=nll_tmp[i];
      cout<<"poi is "<<poi[nfinal]<<", nll is "<<nll[nfinal]<<endl;
      nfinal++;
    }
    else if(poi_tmp[i] == minpoi || (minpoi>poi_tmp[i-1]&&minpoi<poi_tmp[i])) {
      poi[nfinal] = minpoi; nll[nfinal] = 0;
      cout<<"poi is "<<poi[i]<<" "<<poi[i+1]<<", nll is "<<nll[i]<<" "<<nll[i+1]<<endl;
      nfinal++;
    }
    else {
      poi[nfinal]=poi_tmp[i]; nll[nfinal]=nll_tmp[i];
      cout<<"poi is "<<poi[nfinal]<<", nll is "<<nll[nfinal]<<endl;
      nfinal++;
    }
  }

  TGraph *gr=new TGraph(nfinal,poi,nll);


  c->cd();

  TString title_x=scanName;
  if(scanName.BeginsWith("mu_")) { TString scanName2=scanName(2, scanName.Length()); title_x = "#sigma_{#it{ZH"+scanName2+"}}"; }
  if(scanName=="mu_mu") title_x = "#sigma_{#it{ZH_#mu#mu}}";
  if(scanName=="mu_tt") title_x = "#sigma_{#it{ZH_#tau#tau}}";
  if(scanName=="mu_rr") title_x = "#sigma_{#it{ZH_#gamma#gamma}}";

  if(scanName=="mu") title_x = "#mu";
  if(scanName=="k_V") title_x = "#kappa_{V}";
  if(scanName=="k_f") title_x = "#kappa_{f}";
  if(scanName=="k_b") title_x = "#kappa_{b}";
  if(scanName=="k_c") title_x = "#kappa_{c}";
  if(scanName=="k_g") title_x = "#kappa_{g}";
  if(scanName=="k_r") title_x = "#kappa_{r}";
  if(scanName=="k_w") title_x = "#kappa_{w}";
  if(scanName=="k_z") title_x = "#kappa_{z}";
  if(scanName=="k_l") title_x = "#kappa_{l}";

  c->SetLeftMargin(0.1);
  c->SetBottomMargin(0.12);

  gr->SetTitle(" ");
  gr->SetMaximum(8);
  gr->SetMinimum(0.0001);

  gr->GetXaxis()->SetNdivisions(8);
  gr->GetYaxis()->SetNdivisions(8);
  gr->GetXaxis()->SetTitle(title_x);
  gr->GetXaxis()->SetLabelSize(0.04);
  gr->GetXaxis()->SetTitleSize(0.07);
  gr->GetXaxis()->SetTitleOffset(0.7);
  gr->GetXaxis()->SetRangeUser(rangelow+0.0001,rangehigh);

  gr->GetYaxis()->SetLabelSize(0.04);
  gr->GetYaxis()->SetTitle("-2ln(#Lambda)");
  gr->GetYaxis()->SetTitleSize(0.05);
  gr->GetYaxis()->SetTitleOffset(0.8);

  gr->Draw("CA");
  TSpline5 *s=new TSpline5("grs",gr);
  s->SetLineWidth(3);
  s->SetLineColor(kAzure+7);
  s->Draw("same");

  double x1,y1,x2,y2;
  GetX1Y1X2Y2(c,x1,y1,x2,y2);
  vector<TString> pavetext;
  pavetext.push_back("#bf{#it{CEPC}}");
  pavetext.push_back("#scale[0.6]{#int}Ldt=5 ab^{-1}, #sqrt{s}=250GeV");

  if(!mode.Contains("noerr")) {
  double errLo = 0, errHi = 0;

  errHi=BinarySearch(s,1,minpoi+1e-7,rangehigh,1e-4)-minpoi;
  errLo=minpoi-BinarySearch(s,1,rangelow,minpoi-1e-7,1e-4);
  double err=(errLo+errHi)/2;

  cout<<"poi with minimum NLL: "<<minpoi<<endl;
  cout<<"Error low: "<<errLo<<endl;
  cout<<"Error high: "<<errHi<<endl;
  DrawConstantLine(c,1,rangelow,rangehigh,kRed,3,1);
  DrawConstantLine(c,2,rangelow,rangehigh,kRed,3,1);
  TLine *ErrLo=new TLine(minpoi-errLo,0,minpoi-errLo,2);
  TLine *ErrHi=new TLine(minpoi+errHi,0,minpoi+errHi,2);
  ErrLo->SetLineColor(2);ErrLo->SetLineWidth(1); ErrLo->SetLineStyle(1);
  ErrHi->SetLineColor(2);ErrHi->SetLineWidth(1); ;ErrHi->SetLineStyle(1);
 ErrLo->Draw("same");
 ErrHi->Draw("same");

  TString title_x=scanName;
  if(scanName.BeginsWith("mu_")) { TString scanName2=scanName(2, scanName.Length()); title_x = "#sigma_{#it{ZH"+scanName2+"}}"; }
  if(scanName=="mu_mu") title_x = "#sigma_{#it{ZH_#mu#mu}}";
  if(scanName=="mu_tt") title_x = "#sigma_{#it{ZH_#tau#tau}}";
  if(scanName=="mu_rr") title_x = "#sigma_{#it{ZH_#gamma#gamma}}";

  if(scanName=="mu") title_x = "#mu";
  if(scanName=="k_V") title_x = "#kappa_{V}";
  if(scanName=="k_f") title_x = "#kappa_{f}";
  if(scanName=="k_b") title_x = "#kappa_{b}";
  if(scanName=="k_c") title_x = "#kappa_{c}";
  if(scanName=="k_g") title_x = "#kappa_{g}";
  if(scanName=="k_r") title_x = "#kappa_{#gamma}";
  if(scanName=="k_w") title_x = "#kappa_{w}";
  if(scanName=="k_z") title_x = "#kappa_{z}";
  if(scanName=="k_l") title_x = "#kappa_{l}";

  pavetext.push_back(Form(title_x+"=%.4f^{+%.5f}_{-%.5f}",minpoi,errHi,errLo));

  TString errout = "outs/plots/nllScan/"+CHANNEL+"/nllScan_"+scanName+".txt";
  ofstream fout(errout,ios::out);
  fout<<minpoi<<" "<<errLo<<" "<<errHi<<endl;
  fout.close();
  cout<<"Print central value and errors in "<<errout<<endl;
  }

  TPaveText* text=CreatePaveText(x1+0.1,y1+0.5,x1+0.48,y1+0.76,pavetext,0.04);

  c->cd();
  text->Draw("same");

  c->Update();
  system("mkdir -vp outs/plots/nllScan/"+CHANNEL);
  PrintCanvas(c,"outs/plots/nllScan/"+CHANNEL+"/nllScan_"+scanName);
}
