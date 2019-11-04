#include <cstdlib>
#include <vector>
#include <iostream>
#include <map>
#include <string>

#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TStopwatch.h"

// #if not defined(__CINT__) || defined(__MAKECINT__)
// #include "TMVA/Tools.h"
// #include "TMVA/Reader.h"
// #include "TMVA/MethodCuts.h"
// #endif

void qq_ntuple(TString a,TString b);
void qzmv()
{


    qq_ntuple("qzmv_az.root"  ,   "new_qzmv_az.root");
    qq_ntuple("qzmv_sm.root"  ,   "new_qzmv_sm.root");
    qq_ntuple("qzmv_tt.root"  ,   "new_qzmv_tt.root");
    qq_ntuple("qzmv_ww.root"  ,   "new_qzmv_ww.root");
    qq_ntuple("qzmv_zz.root"  , "new_qzmv_zz.root");
    qq_ntuple("qzmv_sig.root"  ,  "new_qzmv_sig.root");

}

void qq_ntuple(TString a,TString b)
{

  TFile *f       = new TFile(a);
  TFile *target  = new TFile(b,"RECREATE");
  TTree *Ts = (TTree *)f->Get("Higgs Tree");
 
  Double_t VisMass,  MisMass;
  Float_t  VisMassf, MisMassf, VisMassf2, MisMassf2, mZ, mH, mjj, rjj;
  Double_t      weight;

  Int_t   MCtau=0;
  Int_t   Tau,nTauP,nTauM;
  weight=1;

  Float_t g1CosPolar,g2CosPolar, g1E, g2E, g1rcCos, g2rcCos, ggE, ggM, rcM, g1PTrans, g2PTrans, ggPTrans, rcCosPolar, g1g2cos;
  Float_t LD0, LZ0, NLD0, NLZ0, weightf;

//    data->SetBranchAddress("ggM",          &ggM); // For recoil M, recoilM is MCtruth.
  //  data->SetBranchAddress("KMass34",   &mH);
  //  data->SetBranchAddress("KReco34",   &mZ);
  //  data->SetBranchAddress("KMass12",   &mjj);
  //  data->SetBranchAddress("KReco12",   &rjj);

  Long64_t nentries = Ts->GetEntries();

  cout<<nentries<<endl;
   Double_t BDTs, BDTb, recoEs, recoEb, invmass, recmass, type;
   Ts->SetBranchAddress("scale",   &weight);
  //  Tb->SetBranchAddress("BDT",   &BDTb);
   Ts->SetBranchAddress("dijet_rec_m",  &invmass);

  TTree *output=new TTree("HiggsTree",  "HiggsTree");
  output->Branch("Mass_H", &mH, "Mass_H/F"); 
  output->Branch("weight", &weightf, "weight/F");
//   output->Branch("BDT"      ,&BDTs,    "BDT/F");

     for (Long64_t i=0; i<nentries;i++)
    {
      Ts->GetEntry(i);
      mH=(Float_t)invmass;
      weightf=(Float_t)weight;
      output->Fill();;
    }
 cout<<a<<"->begin:"<<nentries<<endl;
 cout<<a<<"->after:"<<output->GetEntries()<<endl;
 output->Write("",TObject::kOverwrite);
 target->Close();
 f->Close();

}
