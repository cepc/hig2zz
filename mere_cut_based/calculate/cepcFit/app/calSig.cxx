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

  TString inputFile_null="outs/nllScan/"+CHANNEL+"/"+scanName+"/"+CHANNEL+"_"+scanName+"_nullFit.root";
  double nullnll=1.00, nullpoi=1.00;
  if(gSystem->AccessPathName(inputFile_null)) {
    std::cout << "null File : " << inputFile_null << " does not exist, and minimum will be found in the scan."<< std::endl;
  }
  else {
    TFile *f_null=new TFile(inputFile_null,"read");
    assert(f_null);
    TTree *t_null=(TTree*)f_null->Get("nllscan");
    t_null->SetBranchAddress(scanName,&nullpoi);
    t_null->SetBranchAddress("nll",&nullnll);
    t_null->GetEntry(0);
    cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;
    cout<<"null "<<scanName<<" = "<<nullpoi<<endl;
    cout<<Form("null minimum NLL = %.10f", nullnll)<<endl;
    cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;
    f_null->Close();
    SafeDelete(f_null);
  }


  TString inputFile_one="outs/nllScan/"+CHANNEL+"/"+scanName+"/"+CHANNEL+"_"+scanName+"_oneFit.root";
  double onenll=1.00, onepoi=1.00;
  if(gSystem->AccessPathName(inputFile_one)) {
    std::cout << "one File : " << inputFile_one << " does not exist, and minimum will be found in the scan."<< std::endl;
  }
  else {
    TFile *f_one=new TFile(inputFile_one,"read");
    assert(f_one);
    TTree *t_one=(TTree*)f_one->Get("nllscan");
    t_one->SetBranchAddress(scanName,&onepoi);
    t_one->SetBranchAddress("nll",&onenll);
    t_one->GetEntry(0);
    cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;
    cout<<"one "<<scanName<<" = "<<onepoi<<endl;
    cout<<Form("one minimum NLL = %.10f", onenll)<<endl;
    cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;
    f_one->Close();
    SafeDelete(f_one);
  }

  double dnll_null=2*(nullnll-minnll);
  cout<<"Test value is "<<sqrt(fabs(dnll_null))<<endl;
  double pvalue_null = UncapP0(dnll_null,minpoi);
  double sig_null=PValueToSignificance(pvalue_null);

//  double pvalue1_null = ROOT::Math::chisquared_cdf_c(dnll_null,1);
//  cout<<"null 1d  value is "<<PValueToSignificance(pvalue1_null)<<", squred is "<<pvalues_null<<endl;

  double dnll_one=2*(onenll-minnll);
  cout<<"Test value is "<<sqrt(fabs(dnll_one))<<endl;
  double pvalue_one = UncapP0(dnll_one,minpoi);
  double sig_one=PValueToSignificance(pvalue_one);

//  double pvalue1_one = ROOT::Math::chisquared_cdf_c(dnll_one,1);
//  cout<<"one 1d  value is "<<PValueToSignificance(pvalue1_one)<<", squred is "<<pvalues_one<<endl;

  system("mkdir -vp outs/significance");
  TString errout = "outs/significance/significance_"+CHANNEL+"_"+scanName+".txt";
  ofstream fout(errout,ios::out);
  fout<<"## Channel "<<CHANNEL<<": "<<scanName<<" significance and 1D compatibility with SM"<<endl<<endl;
  fout<<"pvalue for null test "<<pvalue_null<<", significance is "<<sqrt(fabs(dnll_null))<<endl<<endl;
  fout<<"pvalue for one test "<<pvalue_one<<", 1D compatibility is "<<sig_one<<endl;
  fout.close();
  cout<<"Print significance in "<<errout<<endl;

//  system("mkdir -vp outs/plots/nllScan/"+CHANNEL);
}
