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

void qq_ntuple(TString a,TString b);
void qzvm()
{
    qq_ntuple("qzvm_bb.root"  ,   "new_qzvm_bb.root");
    qq_ntuple("qzvm_cc.root"  ,   "new_qzvm_cc.root");
    qq_ntuple("qzvm_gg.root"  ,   "new_qzvm_gg.root");
    qq_ntuple("qzvm_az.root"  ,   "new_qzvm_az.root");
    qq_ntuple("qzvm_sm.root"  ,   "new_qzvm_sm.root");
    qq_ntuple("qzvm_tt.root"  ,   "new_qzvm_tt.root");
    qq_ntuple("qzvm_ww.root"  ,   "new_qzvm_ww.root");
    qq_ntuple("qzvm_sig_other.root"  ,   "new_qzvm_sig_other.root");
    qq_ntuple("qzvm_sig.root"  ,  "new_qzvm_sig.root");
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

  Long64_t nentries = Ts->GetEntries();

  cout<<nentries<<endl;
   Double_t BDTs, BDTb, recoEs, recoEb, invmass, recmass, type;
   Ts->SetBranchAddress("scale",   &weight);
   Ts->SetBranchAddress("dijet_rec_m",  &invmass);

  TTree *output=new TTree("HiggsTree",  "HiggsTree");
  output->Branch("Mass_H", &mH, "Mass_H/F"); 
  output->Branch("weight", &weightf, "weight/F");

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
