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

void mm_ntuple(TString a,TString b);
void mzjv()
{
    mm_ntuple("mzjv_cc.root"  ,   "new_mzjv_cc.root");
    mm_ntuple("mzjv_gg.root"  ,   "new_mzjv_gg.root");
    mm_ntuple("mzjv_bb.root"  ,   "new_mzjv_bb.root");
    mm_ntuple("mzjv_sm.root"  ,   "new_mzjv_sm.root");
    mm_ntuple("mzjv_tt.root"  ,   "new_mzjv_tt.root");
    mm_ntuple("mzjv_ww.root"  ,   "new_mzjv_ww.root");
    mm_ntuple("mzjv_mu.root"  ,   "new_mzjv_mu.root");
    mm_ntuple("mzjv_az.root"  ,   "new_mzjv_az.root");
    mm_ntuple("mzjv_sig.root"  ,  "new_mzjv_sig.root");
    mm_ntuple("mzjv_sig_other.root"  ,  "new_mzjv_sig_other.root");
}

void mm_ntuple(TString a,TString b)
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

  Long64_t nentries = Ts->GetEntries();

  cout<<nentries<<endl;
   Double_t BDTs, BDTb, recoEs, recoEb, invmass, recmass, type;
   Ts->SetBranchAddress("scale",   &weight);
   Ts->SetBranchAddress("dimuon_rec_m",  &invmass);

  TTree *output=new TTree("HiggsTree","HiggsTree");
  output->Branch("Mass_H"     ,&mH,    "Mass_H/F");                          
  output->Branch("weight"        ,&weightf,      "weight/F");

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
