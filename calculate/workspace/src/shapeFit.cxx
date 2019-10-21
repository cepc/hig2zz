//2017.7.9 kappa
//7.10 Combined
#include "numberCounting.h"
#include "shapeFit.h"
#include "makespace.cxx"
#include "TDatime.h"
int main(int argc, char **argv)
{
 clock_t start, finish;
 start = clock();

 gROOT -> Reset();
 gROOT -> Time();

 TString filename;
 if(argc>1) filename=argv[1];
 

 
RooWorkspace* w[Nch];

//  Float_t number[4]={0.1,0.4,1,2};
 TString n[4]={"0.5","2","5","10"};

  for( int j = 2 ; j < 3; j ++ )
  // for( int j = 0 ; j < 4; j ++ ) //not stable fix soon
 {

 vector<string> catName;
 vector<TString> CN;
 
 RooCategory* channellist = new RooCategory("channellist","channellist");
 RooSimultaneous CombinedPdf("CombinedPdf","",*channellist) ;

 RooArgSet* nuisanceParameters = new RooArgSet();
 RooArgSet* globalObservables = new RooArgSet();
 RooArgSet* Observables = new RooArgSet();
 RooArgSet* ks = new RooArgSet();

 map<string,RooDataSet*> datasetMap_SBasimov;


 RooRealVar wt("wt","wt",1);
 RooArgSet *args = new RooArgSet();
 args->add(wt);

  for( int i = 0 ; i < Nch; i ++ )
 {
   CN.push_back(m_CN[i]);
   catName.push_back((string)CN[i]);

   w[i] = makespace(CN[i] , i, j);

   channellist -> defineType(CN[i]) ;
   //CombinedPdf.addPdf(*w[i]->pdf("model_"+CN[i]),CN[i]) ;  // original code from Z. Kaili
   CombinedPdf.addPdf(*w[i]->pdf("modelSB_"+CN[i]),CN[i]) ;
   nuisanceParameters->add( *w[i]->set("nuisanceParameters"));
   globalObservables->add(*w[i]->set("globalObservables"));
   Observables->add(*w[i]->set("Observables"));
   ks->add( *w[i]->set("Pois"));
   datasetMap_SBasimov[catName[i]] = (RooDataSet*)w[i]->data("AsimovSB");
}

 RooWorkspace* combination = new RooWorkspace("combination");
 combination -> importClassCode();
 combination -> import(CombinedPdf);
 combination -> defineSet("nuisanceParameters",*nuisanceParameters, true);
 combination -> defineSet("Observables",*Observables, true);
 combination -> defineSet("globalObservables",*globalObservables, true);
 combination -> defineSet("poi", *ks, true);

 args->add(*Observables);
 RooDataSet* AsimovSB = new RooDataSet("AsimovSB","Asimov SB data ",*args, Index(*channellist), Import(datasetMap_SBasimov) ,WeightVar(wt));
 combination->import(*AsimovSB);

//  ks->Print("v");

 ModelConfig *mconfig = new ModelConfig("ModelConfig",combination);
 mconfig -> SetPdf(*combination->pdf("CombinedPdf"));
 mconfig -> SetObservables( *combination->set("Observables"));
 mconfig -> SetParametersOfInterest( (*combination->set("poi")) );
 mconfig -> SetNuisanceParameters( (*combination->set("nuisanceParameters")) );
 mconfig -> SetGlobalObservables( (*combination->set("globalObservables")) );
 combination -> import(*mconfig);

//  combination->var("channellist")->setConstant(true);
 combination->writeToFile("out/workspace/"+filename+"_"+n[j]+".root");
  TDatime time;
  int time_i=time.GetTime();
  string time_str=to_string(time_i);
 combination->writeToFile("out/workspace/"+filename+"_"+time_str+".root");

cout<<"workspace/"+filename+"_"+n[j]+" finished, primez"<<endl;
}
 finish = clock();

 cout<<endl<<"main:: All Done! Used time: "<<(finish - start)/CLOCKS_PER_SEC<<"seconds"<<endl;
 cerr<<endl<<"main:: All Done! Used time: "<<(finish - start)/CLOCKS_PER_SEC<<"seconds"<<endl;
 
 return 0;

}

