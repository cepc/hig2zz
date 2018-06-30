// -*- C++ -*- //
//
// Description: Higgs -> ZZ* 
//
//         Author:  Ryuta Kiuchi <kiuchi@ihep.ac.cn>
//         Created:  [2018-06-25 Mon 15:49] 
//         Inspired by JING Maoqiang's code (Higgs->invisible)  
//
// 

//
// system include files
//

// for MCParticle, collection and reconstruction
#include <EVENT/LCCollection.h>
#include <IMPL/LCCollectionVec.h>
#include <EVENT/LCFloatVec.h>
#include <EVENT/MCParticle.h>
#include <marlin/Processor.h>
#include <EVENT/ReconstructedParticle.h>
#include <IMPL/MCParticleImpl.h>
#include <UTIL/PIDHandler.h>
#include <EVENT/LCFloatVec.h>
#include <EVENT/LCParameters.h>

// for general definition
#include <string>
#include <iostream>
#include <iomanip>
#include <TFile.h> 
#include <TTree.h>
#include <TVector3.h>
#include <TRandom.h>
#include <sstream>              
#include <cmath>
#include <vector>
#include <TMath.h>
#include <TLorentzVector.h>


class Higgs2zz : public marlin::Processor {

public:
  Processor*  newProcessor() { return new Higgs2zz ; }
  Higgs2zz();
  ~Higgs2zz() {};

  void init();
  void processEvent( LCEvent * evt );
  void end();

private:

  // output file
  std::string FileName;
  std::string TreeName;
  
  // output rootfile
  TFile *m_file;
  TTree *m_tree;

  // paramter setting
  int    OverWrite;       // tree overwrite option: 1(re-create)=default or 0(update) 
  int    EcmsOption;
  double Ecms;
  double RecoEMax;
  double RecoEMin;

  TLorentzVector P4_Ecms;

  // common info
  unsigned int m_event;  

  // Collection
  LCCollection* Col_FastJet;
  LCCollection* Col_Jets;
  LCCollection* Col_Leps;
  LCCollection* Col_Reco;
  LCCollection* Col_MC;
  MCParticle *a1_MC;
  
  int nMC;

  // neutral tracks 
  int  m_n_neutral;
  int  m_n_photon;
  
  TLorentzVector P4_Neutral_Sum;
  double m_neutral_sum_px;
  double m_neutral_sum_py;
  double m_neutral_sum_pz;
  double m_neutral_sum_e;

  // photon info
  double m_photon_px;
  double m_photon_py;
  double m_photon_pz;
  double m_photon_e;
  double m_photon_pt;

  // charged tracks
  int m_n_charged;

  TLorentzVector P4_Charged_Sum;
  double m_charged_sum_px;
  double m_charged_sum_py;
  double m_charged_sum_pz;
  double m_charged_sum_e;


  // lepton info
  int m_n_lepton;
  int m_n_muon_plus;
  int m_n_muon_minus;

  std::vector<TLorentzVector> P4_MuonPlus;  
  std::vector<TLorentzVector> P4_MuonMinus;

  std::vector<double> m_mup_px;
  std::vector<double> m_mup_py;
  std::vector<double> m_mup_pz;
  std::vector<double> m_mup_e;
  std::vector<double> m_mup_pt;

  std::vector<double> m_mum_px;
  std::vector<double> m_mum_py;
  std::vector<double> m_mum_pz;
  std::vector<double> m_mum_e;
  std::vector<double> m_mum_pt;

  std::vector<double> m_dimuon_m;
  std::vector<double> m_dimuon_p;
  std::vector<double> m_dimuon_pt;
  std::vector<double> m_dimuon_e;
  std::vector<double> m_dimuon_rec_m;
  std::vector<double> m_dimuon_dphi;
  std::vector<double> m_dimuon_dang;


  // jet info
  int m_n_jet;
  std::vector<TLorentzVector> P4_Jet;  
 
  std::vector<double> m_jet_px;
  std::vector<double> m_jet_py;
  std::vector<double> m_jet_pz;
  std::vector<double> m_jet_e;
  std::vector<double> m_jet_pt;

  std::vector<double> m_dijet_m;
  std::vector<double> m_dijet_p;
  std::vector<double> m_dijet_pt;
  std::vector<double> m_dijet_e;
  std::vector<double> m_dijet_rec_m;
  std::vector<double> m_dijet_dphi;
  std::vector<double> m_dijet_dang;

  double m_y12;
  double m_y23;
  double m_y34;
  double m_y45;
  double m_y56;
  double m_y67;

  int nFastJet;

  int m_nfastjet;
  std::vector<double> m_fastjet_px; 
  std::vector<double> m_fastjet_py;
  std::vector<double> m_fastjet_pz;
  std::vector<double> m_fastjet_e;

  double m_dijet_m_fastjet;
  double m_dijet_p_fastjet;
  double m_dijet_e_fastjet;
  double m_dijet_rec_m_fastjet;


  // save variables
  double m_rec_lljj_m;
  double m_rec_lljj_e;
  double m_vis_all_m;
  double m_vis_all_e;
  double m_vis_ex_dimuon_m;
  double m_vis_ex_dimuon_e;
  double m_vis_all_rec_m;
  double m_vis_all_rec_e;


  // MC info 
  std::vector<int> m_mc_pdgid;
  std::vector<int> m_mc_init_pdgid;
  std::vector<TLorentzVector> P4_MCTruth_MuonPlus;  
  std::vector<TLorentzVector> P4_MCTruth_MuonMinus;
  std::vector<TLorentzVector> P4_MCTruth_ISRphoton;
  std::vector<TLorentzVector> P4_MCTruth_Higgs;   

  int m_mc_init_n_muon_plus;
  int m_mc_init_n_muon_minus;
  double m_mc_init_mup_px;
  double m_mc_init_mup_py;
  double m_mc_init_mup_pz;
  double m_mc_init_mup_e;
  double m_mc_init_mup_pt;

  double m_mc_init_mum_px;
  double m_mc_init_mum_py;
  double m_mc_init_mum_pz;
  double m_mc_init_mum_e;
  double m_mc_init_mum_pt;

  double m_mc_init_dimuon_m;
  double m_mc_init_dimuon_p;
  double m_mc_init_dimuon_pt;
  double m_mc_init_dimuon_e;
  double m_mc_init_dimuon_rec_m;
  double m_mc_init_dimuon_dphi;
  double m_mc_init_dimuon_dang;
  
  double m_mc_higgs_m;
  double m_mc_higgs_e;
  double m_mc_higgs_rec_m;

  int m_mc_n_Zboson;
  std::vector<int> m_mc_z1_daughter_pid;
  std::vector<int> m_mc_z2_daughter_pid;
  std::vector<TLorentzVector> P4_MCTruth_Z1;  
  std::vector<TLorentzVector> P4_MCTruth_Z2;  

  double m_mc_z1_m;
  double m_mc_z1_p;
  double m_mc_z1_pt;
  double m_mc_z1_e;
  double m_mc_z1_rec_m;

  double m_mc_z2_m;
  double m_mc_z2_p;
  double m_mc_z2_pt;
  double m_mc_z2_e;
  double m_mc_z2_rec_m;
   
  double m_mc_z1z2_m;
  double m_mc_z1z2_e;
  double m_mc_z1z2_rec_m;

  int m_mc_zz_flag;


  // functions
  void book_tree();
  void clearVariables();
  void setECMS();
  bool buildHiggsToZZ();

  void saveNeutral( LCCollection* col_PFOs );
  void savePhotons( LCCollection* col_PFOs );
  void selectCharged( LCCollection* col_IsoLeps );

  void selectLeptons( LCCollection* col_IsoLeps );
  void saveLeptonInfo( std::vector<TLorentzVector> p4_muon_plus, std::vector<TLorentzVector> p4_muon_minus );

  void selectJets( LCCollection* col_Jets );
  void saveJetInfo( std::vector<TLorentzVector> p4_jet );
  void saveFastJet( LCCollection* col_Jets );

  void saveVariables();

  void printDecayChain( int trackID, MCParticle *mcp );
  void printMCinfo( int trackID, int flag, MCParticle *mcp, std::vector<MCParticle*> pvec, std::vector<MCParticle*> dvec );
  void saveMCTruthInfo( LCCollection* col_MC );
  void fillMCInfo();

};

// Global constants
const int ELECTRON_PID           = 11;
const int ELECTRON_NEUTRINO_PID  = 12;
const int MUON_PID               = 13;
const int MUON_NEUTRINO_PID      = 14;
const int TAU_PID                = 15;
const int TAU_NEUTRINO_PID       = 16;

const int PHOTON_PID             = 22;
const int Z_PID                  = 23;
const int HIGGS_PID              = 25;

const double Z_MASS              = 91.2;



Higgs2zz a_higgs2zz_instance;



Higgs2zz::Higgs2zz() : Processor("Higgs2zz") {


  registerProcessorParameter( "TreeOutputFile" , "Output Filename" , FileName , std::string("default.root"));

  registerProcessorParameter( "TreeName" , "ROOT tree name" , TreeName , std::string("tree"));

  registerProcessorParameter( "Ecms" , "ECMS value in GeV." , Ecms , 240.0);

  registerProcessorParameter( "EcmsOption" , "Use ECMS (1) or with Gaussian Blur (0)." , EcmsOption , 1);

  registerProcessorParameter( "OverwriteFile" , "Re-create (1) or Update (0)" , OverWrite , 1 );

  registerProcessorParameter( "RecoEMax" , "Maximum energy of reconstructed particles." , RecoEMax , 100.0);

  registerProcessorParameter( "RecoEMin" , "Minimum energy of reconstructed particles." , RecoEMin , 10.0);
}

void Higgs2zz::init() {

  book_tree();
}

void Higgs2zz::processEvent( LCEvent * evt ) {	

  if(evt){
    try{
      
      clearVariables();
      setECMS();
         
      Col_FastJet = evt->getCollection( "FastJets" );
      Col_Jets = evt->getCollection( "RefinedJets" );
      Col_Leps = evt->getCollection( "IsoLeps"     );      
      Col_MC   = evt->getCollection( "MCParticle"  );
      Col_Reco = evt->getCollection( "ArborPFOs"   );
   

      m_event=evt->getEventNumber();

      if( buildHiggsToZZ() ) {

	saveNeutral( Col_Reco );
	savePhotons( Col_Reco );
	selectCharged( Col_Reco );
	
	saveLeptonInfo( P4_MuonPlus, P4_MuonMinus );
	saveJetInfo( P4_Jet );
	saveVariables();

	//******  Original to be replaced *******// 
	saveFastJet( Col_FastJet );
	
	saveMCTruthInfo( Col_MC ); 

	//***************
	

	m_tree->Fill();
      }
    }
    catch (lcio::DataNotAvailableException err) { }
  }
  
}	


bool Higgs2zz::buildHiggsToZZ() {

  // Select Lepton pairs
  selectLeptons( Col_Leps );
  if( m_n_lepton!=2 ) return false;
  if( m_n_muon_plus!=1 || m_n_muon_minus!=1 ) return false;
 
  // Select LCFIplus Jets
  selectJets( Col_Jets ); 
  //selectJets( Col_FastJet ); 
  //if( m_n_jet!=2 ) return false;

  return true;
}


void Higgs2zz::end() {

  if (m_tree) {
    TFile *tree_file = m_tree->GetCurrentFile(); //just in case we switched to a new file
    tree_file->Write();
    delete tree_file;
  }

}

  
void Higgs2zz::book_tree() {

	m_file=new TFile(FileName.c_str(),(OverWrite ? "RECREATE" : "UPDATE"));
	if (!m_file->IsOpen()) {
		delete m_file;
		m_file=new TFile(FileName.c_str(),"NEW");
	}
	m_tree = new TTree(TreeName.c_str(),TreeName.c_str());

	// General Info
	m_tree->Branch("event",&m_event,"event/I");

	// Neutrals
	m_tree->Branch("n_neutral",  &m_n_neutral,  "n_neutral/I");
	m_tree->Branch("neutral_sum_px", &m_neutral_sum_px, "neutral_sum_px/D");
	m_tree->Branch("neutral_sum_py", &m_neutral_sum_py, "neutral_sum_py/D");
	m_tree->Branch("neutral_sum_pz", &m_neutral_sum_pz, "neutral_sum_pz/D");
	m_tree->Branch("neutral_sum_e" , &m_neutral_sum_e , "neutral_sum_e/D");

	m_tree->Branch("n_photon",  &m_n_photon,  "n_photon/I");
	m_tree->Branch("photon_px", &m_photon_px, "photon_px/D");
	m_tree->Branch("photon_py", &m_photon_py, "photon_py/D");
	m_tree->Branch("photon_pz", &m_photon_pz, "photon_pz/D");
	m_tree->Branch("photon_e" , &m_photon_e , "photon_e/D");
	m_tree->Branch("photon_pt", &m_photon_pt, "photon_pt/D");

	// Charged
	m_tree->Branch("n_charged",  &m_n_charged,  "n_charged/I");
	m_tree->Branch("charged_sum_px", &m_charged_sum_px, "charged_sum_px/D");
	m_tree->Branch("charged_sum_py", &m_charged_sum_py, "charged_sum_py/D");
	m_tree->Branch("charged_sum_pz", &m_charged_sum_pz, "charged_sum_pz/D");
	m_tree->Branch("charged_sum_e" , &m_charged_sum_e , "charged_sum_e/D");


	// Leptons
	m_tree->Branch("n_lepton", &m_n_lepton,  "n_lepton/I");
	m_tree->Branch("n_muon_plus", &m_n_muon_plus, "n_muon_plus/I");
	m_tree->Branch("n_muon_minus", &m_n_muon_minus, "n_muon_minus/I");

	m_tree->Branch("mup_px", &m_mup_px);
	m_tree->Branch("mup_py", &m_mup_py);
	m_tree->Branch("mup_pz", &m_mup_pz);
	m_tree->Branch("mup_e", &m_mup_e);
	m_tree->Branch("mup_pt", &m_mup_pt);

	m_tree->Branch("mum_px", &m_mum_px);
	m_tree->Branch("mum_py", &m_mum_py);
	m_tree->Branch("mum_pz", &m_mum_pz);
	m_tree->Branch("mum_e", &m_mum_e);
	m_tree->Branch("mum_pt", &m_mum_pt);

	m_tree->Branch("dimuon_m", &m_dimuon_m);
	m_tree->Branch("dimuon_p", &m_dimuon_p);
	m_tree->Branch("dimuon_pt", &m_dimuon_pt);
	m_tree->Branch("dimuon_e", &m_dimuon_e);
	m_tree->Branch("dimuon_rec_m", &m_dimuon_rec_m);
	m_tree->Branch("dimuon_dphi", &m_dimuon_dphi);
	m_tree->Branch("dimuon_dang", &m_dimuon_dang);

	// Jets
	m_tree->Branch("n_jet",  &m_n_jet,  "m_n_jet/I");

	m_tree->Branch("jet_px", &m_jet_px);
	m_tree->Branch("jet_py", &m_jet_py);
	m_tree->Branch("jet_pz", &m_jet_pz);
	m_tree->Branch("jet_e", &m_jet_e);
	m_tree->Branch("jet_pt", &m_jet_pt);

	m_tree->Branch("dijet_m", &m_dijet_m);
	m_tree->Branch("dijet_e", &m_dijet_e);
	m_tree->Branch("dijet_rec_m", &m_dijet_rec_m);
	m_tree->Branch("dijet_dphi", &m_dijet_dphi);
	m_tree->Branch("dijet_dang", &m_dijet_dang);

	m_tree->Branch("y12", &m_y12, "y12/D");
	m_tree->Branch("y23", &m_y23, "y23/D");
	m_tree->Branch("y34", &m_y34, "y34/D");
	m_tree->Branch("y45", &m_y45, "y45/D");
	m_tree->Branch("y56", &m_y56, "y56/D");
	m_tree->Branch("y67", &m_y67, "y67/D");

	m_tree->Branch("n_fastjet",  &m_nfastjet,  "n_fastjet/I");	
	m_tree->Branch("fastjet_px", &m_fastjet_px);
	m_tree->Branch("fastjet_py", &m_fastjet_py);
	m_tree->Branch("fastjet_pz", &m_fastjet_pz);
	m_tree->Branch("fastjet_e", &m_fastjet_e);

	m_tree->Branch("dijet_m_fastjet", &m_dijet_m_fastjet, "dijet_m_fastjet/D"); 
	m_tree->Branch("dijet_p_fastjet", &m_dijet_p_fastjet, "dijet_p_fastjet/D");
 	m_tree->Branch("dijet_e_fastjet", &m_dijet_e_fastjet, "dijet_e_fastjet/D"); 
	m_tree->Branch("dijet_rec_m_fastjet", &m_dijet_rec_m_fastjet, "dijet_rec_m_fastjet/D");
	

	// other variables to be stored.
	m_tree->Branch("rec_lljj_m", &m_rec_lljj_m, "rec_lljj_m/D");
	m_tree->Branch("rec_lljj_e", &m_rec_lljj_e, "rec_lljj_e/D");

	m_tree->Branch("vis_ex_dimuon_m", &m_vis_ex_dimuon_m, "vis_ex_dimuon_m/D");
	m_tree->Branch("vis_ex_dimuon_e", &m_vis_ex_dimuon_e, "vis_ex_dimuon_e/D");
	m_tree->Branch("vis_all_m", &m_vis_all_m, "vis_all_m/D");
	m_tree->Branch("vis_all_e", &m_vis_all_e, "vis_all_e/D");
	m_tree->Branch("vis_all_rec_m", &m_vis_all_rec_m, "vis_all_rec_m/D");
	m_tree->Branch("vis_all_rec_e", &m_vis_all_rec_e, "vis_all_rec_e/D");


	// MC info 
	m_tree->Branch("mc_pdgid", &m_mc_pdgid);
	m_tree->Branch("mc_init_pdgid", &m_mc_init_pdgid);

	m_tree->Branch("mc_init_n_muon_plus", &m_mc_init_n_muon_plus,  "mc_init_n_muon_plus/I");
	m_tree->Branch("mc_init_n_muon_minus", &m_mc_init_n_muon_minus,  "mc_init_n_muon_minus/I");

	m_tree->Branch("mc_init_mup_px", &m_mc_init_mup_px,  "mc_init_mup_px/D");
	m_tree->Branch("mc_init_mup_py", &m_mc_init_mup_py,  "mc_init_mup_py/D");
	m_tree->Branch("mc_init_mup_pz", &m_mc_init_mup_pz,  "mc_init_mup_pz/D");
	m_tree->Branch("mc_init_mup_e",  &m_mc_init_mup_e,   "mc_init_mup_e/D");
	m_tree->Branch("mc_init_mup_pt", &m_mc_init_mup_pt,  "mc_init_mup_pt/D");

	m_tree->Branch("mc_init_mum_px", &m_mc_init_mum_px,  "mc_init_mum_px/D");
	m_tree->Branch("mc_init_mum_py", &m_mc_init_mum_py,  "mc_init_mum_py/D");
	m_tree->Branch("mc_init_mum_pz", &m_mc_init_mum_pz,  "mc_init_mum_pz/D");
	m_tree->Branch("mc_init_mum_e",  &m_mc_init_mum_e,   "mc_init_mum_e/D");
	m_tree->Branch("mc_init_mum_pt", &m_mc_init_mum_pt,  "mc_init_mum_pt/D");

	m_tree->Branch("mc_init_dimuon_m", &m_mc_init_dimuon_m,  "mc_init_dimuon_m/D");
	m_tree->Branch("mc_init_dimuon_p", &m_mc_init_dimuon_p,  "mc_init_dimuon_p/D");
	m_tree->Branch("mc_init_dimuon_pt", &m_mc_init_dimuon_pt,  "mc_init_dimuon_pt/D");
	m_tree->Branch("mc_init_dimuon_e",  &m_mc_init_dimuon_e,   "mc_init_dimuon_e/D");
	m_tree->Branch("mc_init_dimuon_rec_m", &m_mc_init_dimuon_rec_m,  "mc_init_dimuon_rec_m/D");
	m_tree->Branch("mc_init_dimuon_dphi", &m_mc_init_dimuon_dphi,  "mc_init_dimuon_dphi/D");
	m_tree->Branch("mc_init_dimuon_dang", &m_mc_init_dimuon_dang,  "mc_init_dimuon_dang/D");

	m_tree->Branch("mc_higgs_m", &m_mc_higgs_m);
	m_tree->Branch("mc_higgs_e", &m_mc_higgs_e);
	m_tree->Branch("mc_higgs_rec_m", &m_mc_higgs_rec_m);

	m_tree->Branch("mc_n_Zboson", &m_mc_n_Zboson, "mc_n_Zboson/I");

	m_tree->Branch("mc_z1_daughter_pid", &m_mc_z1_daughter_pid);
	m_tree->Branch("mc_z2_daughter_pid", &m_mc_z2_daughter_pid);

	m_tree->Branch("mc_z1_m", &m_mc_z1_m, "mc_z1_m/D");
	m_tree->Branch("mc_z1_p", &m_mc_z1_p, "mc_z1_p/D");
	m_tree->Branch("mc_z1_pt", &m_mc_z1_pt, "mc_z1_pt/D");
	m_tree->Branch("mc_z1_e", &m_mc_z1_e, "mc_z1_e/D");
	m_tree->Branch("mc_z1_rec_m", &m_mc_z1_rec_m, "mc_z1_rec_m/D");

	m_tree->Branch("mc_z2_m", &m_mc_z2_m, "mc_z2_m/D");
	m_tree->Branch("mc_z2_p", &m_mc_z2_p, "mc_z2_p/D");
	m_tree->Branch("mc_z2_pt", &m_mc_z2_pt, "mc_z2_pt/D");
	m_tree->Branch("mc_z2_e", &m_mc_z2_e, "mc_z2_e/D");
	m_tree->Branch("mc_z2_rec_m", &m_mc_z2_rec_m, "mc_z2_rec_m/D");

	m_tree->Branch("mc_z1z2_m", &m_mc_z1z2_m, "mc_z1z2_m/D");
	m_tree->Branch("mc_z1z2_e", &m_mc_z1z2_e, "mc_z1z2_e/D");
	m_tree->Branch("mc_z1z2_rec_m", &m_mc_z1z2_rec_m, "mc_z1z2_rec_m/D");
	m_tree->Branch("mc_zz_flag", &m_mc_zz_flag, "mc_zz_flag/I");

}

void Higgs2zz::clearVariables() {

  // MC info. 
  m_mc_pdgid.clear();
  m_mc_init_pdgid.clear();
  P4_MCTruth_MuonPlus.clear();
  P4_MCTruth_MuonMinus.clear();
  P4_MCTruth_ISRphoton.clear();
  P4_MCTruth_Higgs.clear();

  m_mc_z1_daughter_pid.clear();
  m_mc_z2_daughter_pid.clear();
  P4_MCTruth_Z1.clear();
  P4_MCTruth_Z2.clear();
  
  // Sum of all neutrals
  for(int i=0;i<4;i++)P4_Neutral_Sum[i]=0.0;
  
  // Sum of all charged 
  for(int i=0;i<4;i++)P4_Charged_Sum[i]=0.0;
  
  // Lepton info.
  P4_MuonPlus.clear();
  P4_MuonMinus.clear();
  
  m_mup_px.clear();
  m_mup_py.clear();
  m_mup_pz.clear();
  m_mup_e.clear();
  m_mup_pt.clear();
  
  m_mum_px.clear();
  m_mum_py.clear();
  m_mum_pz.clear();
  m_mum_e.clear();
  m_mum_pt.clear();
  
  m_dimuon_m.clear();
  m_dimuon_p.clear();
  m_dimuon_pt.clear();
  m_dimuon_e.clear();
  m_dimuon_rec_m.clear();
  m_dimuon_dphi.clear();
  m_dimuon_dang.clear();
  
  
  // Jet info.
  P4_Jet.clear();
  m_jet_px.clear();
  m_jet_py.clear();
  m_jet_pz.clear();
  m_jet_e.clear();
  m_jet_pt.clear();
  
  m_dijet_m.clear();
  m_dijet_p.clear();
  m_dijet_pt.clear();
  m_dijet_e.clear();
  m_dijet_rec_m.clear();
  m_dijet_dphi.clear();
  m_dijet_dang.clear();
  
  // fast jet
  m_fastjet_px.clear();
  m_fastjet_py.clear();
  m_fastjet_pz.clear();
  m_fastjet_e.clear();
 
}

void Higgs2zz::setECMS() {

  if( EcmsOption == 0 ) {

    double ehalf = Ecms*0.5;  // if Ecms=240GeV, ehalf=120GeV
    TLorentzVector beamp(0, 0,  ehalf, ehalf);
    TLorentzVector beamm(0, 0, -ehalf, ehalf);

    double scale1 = (gRandom->Gaus(1, 0.0024));
    double scale2 = (gRandom->Gaus(1, 0.0024));
    
    P4_Ecms=scale1*beamp+scale2*beamm;
  }
  else {
   
    TLorentzVector ecms(0, 0, 0, Ecms);
    P4_Ecms = ecms;
  }
}
  

void Higgs2zz::saveNeutral( LCCollection* col_PFOs ) {

  int ncol = col_PFOs->getNumberOfElements();

  int counter=0;
  for(int i = 0; i < ncol; i++) {
    ReconstructedParticle *a_Reco = dynamic_cast<EVENT::ReconstructedParticle *>(col_PFOs->getElementAt(i));
    if(a_Reco->getCharge()!=0) continue;
    P4_Neutral_Sum[0] += a_Reco->getMomentum()[0];
    P4_Neutral_Sum[1] += a_Reco->getMomentum()[1];
    P4_Neutral_Sum[2] += a_Reco->getMomentum()[2];
    P4_Neutral_Sum[3] += a_Reco->getEnergy();
  }

  m_n_neutral = counter;
  
  m_neutral_sum_px = P4_Neutral_Sum[0];
  m_neutral_sum_py = P4_Neutral_Sum[1];
  m_neutral_sum_pz = P4_Neutral_Sum[2];
  m_neutral_sum_e  = P4_Neutral_Sum[3];
}


void Higgs2zz::savePhotons( LCCollection* col_PFOs ) {

  int ncol = col_PFOs->getNumberOfElements();

  double tmp_emax=-1.0;
  int counter=0;
  for(int i = 0; i < ncol; i++) {
    ReconstructedParticle *a_Reco = dynamic_cast<EVENT::ReconstructedParticle *>(col_PFOs->getElementAt(i));
    if(a_Reco->getCharge()!=0) continue;
    if(a_Reco->getType()!=PHOTON_PID) continue;
    if(fabs(a_Reco->getMomentum()[2]/a_Reco->getEnergy())>0.995) continue; // acceptance of the detector
    counter++;

    if(a_Reco->getEnergy() > tmp_emax) {
      tmp_emax = a_Reco->getEnergy();

      m_photon_px = a_Reco->getMomentum()[0];
      m_photon_py = a_Reco->getMomentum()[1];
      m_photon_pz = a_Reco->getMomentum()[2];
      m_photon_e = a_Reco->getEnergy();
      m_photon_pt = sqrt( m_photon_px*m_photon_px + m_photon_py*m_photon_py );
    }
  }
  m_n_photon = counter;
  
  if( m_n_photon == 0 ) {

    m_photon_px = -9999.0; 
    m_photon_py = -9999.0;
    m_photon_pz = -9999.0;
    m_photon_e = -9999.0;
    m_photon_pt = -9999.0;
  }
  
}

  
void Higgs2zz::selectCharged( LCCollection* col_IsoLeps ) {

  int ncol = col_IsoLeps->getNumberOfElements();

  int counter = 0;
  for(int i = 0; i < ncol; i++) {
    ReconstructedParticle *a_Reco = dynamic_cast<EVENT::ReconstructedParticle *>(col_IsoLeps->getElementAt(i));
    if(a_Reco->getCharge()==0) continue;

    P4_Charged_Sum[0] += a_Reco->getMomentum()[0];
    P4_Charged_Sum[1] += a_Reco->getMomentum()[1];
    P4_Charged_Sum[2] += a_Reco->getMomentum()[2];
    P4_Charged_Sum[3] += a_Reco->getEnergy();
    counter++;
  }
  m_n_charged = counter;

  m_charged_sum_px = P4_Charged_Sum[0];
  m_charged_sum_py = P4_Charged_Sum[1];
  m_charged_sum_pz = P4_Charged_Sum[2];
  m_charged_sum_e  = P4_Charged_Sum[3];
}




void Higgs2zz::selectLeptons( LCCollection* col_Leps ) {
  
  int ncol = col_Leps->getNumberOfElements();

  int nlep=0;
  for(int i = 0; i < ncol; i++) {
    ReconstructedParticle *a_Reco = dynamic_cast<EVENT::ReconstructedParticle *>(col_Leps->getElementAt(i));
    if(a_Reco->getCharge()==0) continue;

    int    lepton_pid    = abs(a_Reco->getType());
    double lepton_charge = a_Reco->getCharge();
    double lepton_px     = a_Reco->getMomentum()[0];
    double lepton_py     = a_Reco->getMomentum()[1];
    double lepton_pz     = a_Reco->getMomentum()[2];
    double lepton_e      = a_Reco->getEnergy();
    
    TLorentzVector p4vec(lepton_px, lepton_py, lepton_pz, lepton_e);

    if( lepton_e > RecoEMin && lepton_e < RecoEMax ) {  //0.4*sqrt(s) 

      if( lepton_pid == MUON_PID || lepton_pid == ELECTRON_PID || lepton_pid == TAU_PID )nlep++;

      if( lepton_pid ==  MUON_PID ) {
	if( lepton_charge <  0.1 )P4_MuonPlus.push_back( p4vec );
	if( lepton_charge > -0.1 )P4_MuonMinus.push_back( p4vec );
      }
    }

  }

  m_n_lepton = nlep;
  m_n_muon_plus  = P4_MuonPlus.size();
  m_n_muon_minus = P4_MuonMinus.size();
  std::cout << "m_n_muon_plus = " << m_n_muon_plus << ", m_n_muon_minus = " << m_n_muon_minus << std::endl;

}


void Higgs2zz::saveLeptonInfo(std::vector<TLorentzVector> p4_muon_plus, std::vector<TLorentzVector> p4_muon_minus) {

  int nlep_p = p4_muon_plus.size();
  int nlep_m = p4_muon_minus.size();

  for(int i = 0; i < nlep_p; i++) {
  
    for(int j = 0; j < nlep_m; j++) {
	
      m_mup_px.push_back(p4_muon_plus[i].Px());
      m_mup_py.push_back(p4_muon_plus[i].Py());
      m_mup_pz.push_back(p4_muon_plus[i].Pz());
      m_mup_e.push_back(p4_muon_plus[i].E());
      
      m_mup_pt.push_back(p4_muon_plus[i].Pt());

      m_mum_px.push_back(p4_muon_minus[j].Px());
      m_mum_py.push_back(p4_muon_minus[j].Py());
      m_mum_pz.push_back(p4_muon_minus[j].Pz());
      m_mum_e.push_back(p4_muon_minus[j].E());
      
      m_mum_pt.push_back(p4_muon_minus[j].Pt());

      double mll     = ( p4_muon_plus[i] + p4_muon_minus[j] ).M();
      double pll     = ( p4_muon_plus[i] + p4_muon_minus[j] ).P();
      double ptll    = ( p4_muon_plus[i] + p4_muon_minus[j] ).Pt();
      double ell     = ( p4_muon_plus[i] + p4_muon_minus[j] ).E();
      double rec_mll = ( P4_Ecms - p4_muon_plus[i] - p4_muon_minus[j] ).M();
      double dphi    = fabs(p4_muon_plus[i].DeltaPhi(p4_muon_minus[j])) *180.0/M_PI;
      double dang    = p4_muon_plus[i].Angle(p4_muon_minus[j].Vect())   *180.0/M_PI;
      
      m_dimuon_m.push_back(mll);
      m_dimuon_p.push_back(pll);
      m_dimuon_pt.push_back(ptll);
      m_dimuon_e.push_back(ell);
      m_dimuon_rec_m.push_back(rec_mll);
      m_dimuon_dphi.push_back(dphi);
      m_dimuon_dang.push_back(dang);
    }
  }

  // fill dummy value in case of N(muon)=0
  if( nlep_p == 0 ) {

    m_mup_px.push_back( -9999.0 );
    m_mup_py.push_back( -9999.0 );
    m_mup_pz.push_back( -9999.0 );
    m_mup_e.push_back( -9999.0 );    
    m_mup_pt.push_back( -9999.0 );
  }

  if( nlep_m == 0 ) {

    m_mum_px.push_back( -9999.0 );
    m_mum_py.push_back( -9999.0 );
    m_mum_pz.push_back( -9999.0 );
    m_mum_e.push_back( -9999.0 );    
    m_mum_pt.push_back( -9999.0 );
  }

  if( nlep_p == 0 || nlep_m == 0 ) {

    m_dimuon_m.push_back( -9999.0 );
    m_dimuon_e.push_back( -9999.0 );
    m_dimuon_rec_m.push_back( -9999.0 );
    m_dimuon_dphi.push_back( -9999.0 );
    m_dimuon_dang.push_back( -9999.0 );
  }

}


void Higgs2zz::saveFastJet( LCCollection* col_Jets ) {

  int ncol = col_Jets->getNumberOfElements();

  std::cout << "nFastJet = " << ncol << std::endl;
  m_nfastjet = ncol;
  for( int i = 0; i < ncol; i++) {

    ReconstructedParticle *reco_jet = dynamic_cast<EVENT::ReconstructedParticle *>(col_Jets->getElementAt(i));
    m_fastjet_px.push_back( reco_jet->getMomentum()[0] );
    m_fastjet_py.push_back( reco_jet->getMomentum()[1] );
    m_fastjet_pz.push_back( reco_jet->getMomentum()[2] );
    m_fastjet_e.push_back( reco_jet->getEnergy() );
  }

  if( m_nfastjet == 2 ) {
    
    TLorentzVector jet1, jet2;
      
    ReconstructedParticle *reco_jet1 = dynamic_cast<EVENT::ReconstructedParticle *>(col_Jets->getElementAt(0));
    ReconstructedParticle *reco_jet2 = dynamic_cast<EVENT::ReconstructedParticle *>(col_Jets->getElementAt(1));
      
    jet1[0] = reco_jet1->getMomentum()[0];
    jet1[1] = reco_jet1->getMomentum()[1];
    jet1[2] = reco_jet1->getMomentum()[2];
    jet1[3] = reco_jet1->getEnergy();

    jet2[0] = reco_jet2->getMomentum()[0];
    jet2[1] = reco_jet2->getMomentum()[1];
    jet2[2] = reco_jet2->getMomentum()[2];
    jet2[3] = reco_jet2->getEnergy();

    m_dijet_e_fastjet = ( jet1 + jet2 ).M();
    m_dijet_p_fastjet = ( jet1 + jet2 ).P();
    m_dijet_e_fastjet = ( jet1 + jet2 ).E();
    m_dijet_rec_m_fastjet = (P4_Ecms - jet1 - jet2).M();
  }
  else {

    m_fastjet_px.push_back( -9999.0 );
    m_fastjet_py.push_back( -9999.0 );
    m_fastjet_pz.push_back( -9999.0 );
    m_fastjet_e.push_back( -9999.0 );

    m_dijet_e_fastjet = -9999.0;
    m_dijet_p_fastjet = -9999.0;
    m_dijet_e_fastjet = -9999.0;
    m_dijet_rec_m_fastjet = -9999.0;
  }
}

void Higgs2zz::selectJets( LCCollection* col_Jets ) {

  int ncol = col_Jets->getNumberOfElements();
  std::cout << "njet = " << ncol << std::endl; 
  
  
  ReconstructedParticle *Jet0 = dynamic_cast<ReconstructedParticle *>(col_Jets->getElementAt(1));
  PIDHandler pidh(col_Jets);
  Int_t algo_y = pidh.getAlgorithmID("yth");
  const ParticleID & ythID = pidh.getParticleID(Jet0, algo_y);
  FloatVec params_y = ythID.getParameters();
  m_y12 = params_y[pidh.getParameterIndex(algo_y, "y12")];
  m_y23 = params_y[pidh.getParameterIndex(algo_y, "y23")];
  m_y34 = params_y[pidh.getParameterIndex(algo_y, "y34")];
  m_y45 = params_y[pidh.getParameterIndex(algo_y, "y45")];
  m_y56 = params_y[pidh.getParameterIndex(algo_y, "y56")];
  m_y67 = params_y[pidh.getParameterIndex(algo_y, "y67")];


  for( int i = 0; i < ncol; i++) {

    ReconstructedParticle *reco_jet = dynamic_cast<EVENT::ReconstructedParticle *>(col_Jets->getElementAt(i));

    double jet_px     = reco_jet->getMomentum()[0];
    double jet_py     = reco_jet->getMomentum()[1];
    double jet_pz     = reco_jet->getMomentum()[2];
    double jet_e      = reco_jet->getEnergy();
    
    TLorentzVector p4vec(jet_px, jet_py, jet_pz, jet_e);

    P4_Jet.push_back( p4vec );
  }

  m_n_jet = P4_Jet.size();

}

void Higgs2zz::saveJetInfo( std::vector<TLorentzVector> p4_jet ) {

  int njet = p4_jet.size();

  for( int i=0; i < njet-1; i++ ) {
    
    m_jet_px.push_back(p4_jet[i].Px());
    m_jet_py.push_back(p4_jet[i].Py());
    m_jet_pz.push_back(p4_jet[i].Pz());
    m_jet_e.push_back(p4_jet[i].E());

    m_jet_pt.push_back(p4_jet[i].Pt());

    for( int j=i+1; j < njet; j++) {

      double mjj     = ( p4_jet[i] + p4_jet[j] ).M();
      double pjj     = ( p4_jet[i] + p4_jet[j] ).P();
      double ptjj    = ( p4_jet[i] + p4_jet[j] ).Pt();
      double ejj     = ( p4_jet[i] + p4_jet[j] ).E();
      double rec_mjj = ( P4_Ecms - p4_jet[i] - p4_jet[j] ).M();
      double dphi    = fabs(p4_jet[i].DeltaPhi(p4_jet[j])) *180.0/M_PI;
      double dang    = p4_jet[i].Angle(p4_jet[j].Vect())   *180.0/M_PI;

      m_dijet_m.push_back( mjj );
      m_dijet_p.push_back( pjj );
      m_dijet_pt.push_back( ptjj );
      m_dijet_e.push_back( ejj );
      m_dijet_rec_m.push_back( rec_mjj );
      m_dijet_dphi.push_back( dphi );
      m_dijet_dang.push_back( dang );
    }
  }
      
  if( njet <= 1 ) {  // Can not calculate dijet variables

    m_dijet_m.push_back( -9999.0 );
    m_dijet_e.push_back( -9999.0 );
    m_dijet_rec_m.push_back( -9999.0 );
    m_dijet_dphi.push_back( -9999.0 );
    m_dijet_dang.push_back( -9999.0 );

    if( njet == 0 ) {
      
      m_jet_px.push_back( -9999.0 );
      m_jet_py.push_back( -9999.0 );
      m_jet_pz.push_back( -9999.0 );
      m_jet_e.push_back( -9999.0 );
      m_jet_pt.push_back( -9999.0 );
    }
  }
    
}


void Higgs2zz::saveVariables() {

  // Variables to be stored -- temporal form !!
  if( m_n_jet == 2 ) {

    m_rec_lljj_m = ( P4_Ecms - P4_MuonPlus[0] - P4_MuonMinus[0] - P4_Jet[0] - P4_Jet[1] ).M(); 
    m_rec_lljj_e = ( P4_Ecms - P4_MuonPlus[0] - P4_MuonMinus[0] - P4_Jet[0] - P4_Jet[1] ).E();
  }
  else {

    m_rec_lljj_m = -9999.0;
    m_rec_lljj_e = -9999.0;
  }

  m_vis_ex_dimuon_m = ( P4_Charged_Sum + P4_Neutral_Sum - P4_MuonPlus[0] - P4_MuonMinus[0] ).M();
  m_vis_ex_dimuon_e = ( P4_Charged_Sum + P4_Neutral_Sum - P4_MuonPlus[0] - P4_MuonMinus[0] ).E();

  m_vis_all_m = ( P4_Charged_Sum + P4_Neutral_Sum ).M();
  m_vis_all_e = ( P4_Charged_Sum + P4_Neutral_Sum ).E();
  m_vis_all_rec_m = ( P4_Ecms - P4_Charged_Sum - P4_Neutral_Sum ).M();
  m_vis_all_rec_e = ( P4_Ecms - P4_Charged_Sum - P4_Neutral_Sum ).E();

}


void Higgs2zz::printDecayChain( int trackID, MCParticle *mcp ) {
  
  std::vector<MCParticle*> pvec, dvec;
  pvec = mcp->getParents();
  dvec = mcp->getDaughters();
  
  // Display PID info. 
  printMCinfo( trackID, 1, mcp, pvec, dvec );
  
  // Follow daughter's information as well
  if( 1 )
  {
    for( std::vector<MCParticle*>::iterator itr = dvec.begin(); itr != dvec.end(); ++itr ) {
      
      std::vector<MCParticle*> p_dvec, d_dvec;
      p_dvec = (*itr)->getParents();
      d_dvec = (*itr)->getDaughters();
    
      int dummy_trackID = -1;
      printMCinfo( dummy_trackID, 2, *itr, p_dvec, d_dvec );    
    }
  }
}

void Higgs2zz::printMCinfo( int trackID, int flag, MCParticle *mcp, std::vector<MCParticle*> pvec, std::vector<MCParticle*> dvec ) {

  int status      =  mcp->getGeneratorStatus(); 
  int pdgid       =  mcp->getPDG();
  //int mass        =  mcp->getMass();
  int nparents    =  pvec.size();
  int ndaughters  =  dvec.size();

  std::vector<int> p_pid;
  std::vector<int> d_pid;

  for( std::vector<MCParticle*>::iterator itr = pvec.begin(); itr != pvec.end(); ++itr ) p_pid.push_back( (*itr)->getPDG() );
  for( std::vector<MCParticle*>::iterator itr = dvec.begin(); itr != dvec.end(); ++itr ) d_pid.push_back( (*itr)->getPDG() );

  if( flag == 1 )std::cout << " trackID = " << std::setw(4) <<  trackID ;
  if( flag == 2 )std::cout << "           " << "    " ;                    // daughther info.

  std::cout << ", status=" << status << " : nParents = " << nparents << " : " ;    
  for( std::vector<int>::iterator itr = p_pid.begin(); itr != p_pid.end(); ++itr ) std::cout << std::setw(5) << *itr << " " ;
  if( p_pid.size() == 0 ) {
    std::cout << "     " << " " ;
    std::cout << "     " << " " ;
  }
  if( p_pid.size() == 1 ) {
    std::cout << "     " << " " ;
  }  
  std::cout << " : pdgid = " << std::setw(5) << pdgid << " : nDaughters = " << ndaughters << " : " ;
  for( std::vector<int>::iterator itr = d_pid.begin(); itr != d_pid.end(); ++itr ) std::cout << std::setw(5) << *itr << ", " ;
  std::cout << std::endl; 

}



void Higgs2zz::saveMCTruthInfo( LCCollection* col_MC ) {

  int ncol = col_MC->getNumberOfElements();
  
  int Zcount=0;
  for( int i = 0; i < ncol; i++) {

    MCParticle *mcp = dynamic_cast<EVENT::MCParticle *>(col_MC->getElementAt(i));

    std::vector<MCParticle*> pvec, dvec;
    pvec = mcp->getParents();
    dvec = mcp->getDaughters();

    int status      =  mcp->getGeneratorStatus(); 
    int pdgid       =  mcp->getPDG();
    //int mass        =  mcp->getMass();
    int nparents    =  pvec.size();
    int ndaughters  =  dvec.size();

    // Print decay chain info, if need them.
    if( 0 ) printDecayChain( i , mcp );


    int mother_pid=-9999;
    if( nparents > 0 )mother_pid=pvec[0]->getPDG();

    if( nparents == 0 ) { 
	
      double px = mcp->getMomentum()[0];
      double py = mcp->getMomentum()[1];
      double pz = mcp->getMomentum()[2];
      double e = mcp->getEnergy();
      
      TLorentzVector p4vec(px, py, pz, e);
      
      if( pdgid == MUON_PID )P4_MCTruth_MuonMinus.push_back( p4vec );
      if( pdgid == -MUON_PID )P4_MCTruth_MuonPlus.push_back( p4vec );
      
      if( pdgid == PHOTON_PID )P4_MCTruth_ISRphoton.push_back( p4vec );
      if( pdgid == HIGGS_PID )P4_MCTruth_Higgs.push_back( p4vec );

      m_mc_init_pdgid.push_back( pdgid );
    }

    // Find Z daughters
    if( nparents == 1 && mother_pid == HIGGS_PID ) { // mother is Higgs

      if( pdgid == Z_PID ) {  // Z boson
	
	//for( int j = 0; j < ndaughters; j++ ) 
	for( int j = 0; j < 2; j++ )  { // fill daughter's info
	  
	  int d_pid  = dvec[j]->getPDG();
	  
	  double px = dvec[j]->getMomentum()[0];
	  double py = dvec[j]->getMomentum()[1];
	  double pz = dvec[j]->getMomentum()[2];
	  double e = dvec[j]->getEnergy();
      
	  TLorentzVector p4vec(px, py, pz, e);

	  if( Zcount == 0 ) {
	    //std::cout << "Zcount = 0 : daughter pid = " << d_pid << std::endl; 
	    //std::cout << "px = " << px << ", py = " << py << ", e = " << e << std::endl;
	    m_mc_z1_daughter_pid.push_back( d_pid );
	    P4_MCTruth_Z1.push_back( p4vec );	    
	  }
	  else if( Zcount == 1 ) {
	    //std::cout << "Zcount = 1 : daughter pid = " << d_pid << std::endl; 
	    //std::cout << "px = " << px << ", py = " << py << ", e = " << e << std::endl;
	    m_mc_z2_daughter_pid.push_back( d_pid );
	    P4_MCTruth_Z2.push_back( p4vec );
	  }
	}
	
	Zcount++;
      }
    }

    if(status==1 || status==2)m_mc_pdgid.push_back(pdgid);
  }

  m_mc_n_Zboson = Zcount;

  fillMCInfo();

}

void Higgs2zz::fillMCInfo() {

  int n_init_mup = P4_MCTruth_MuonPlus.size();
  int n_init_mum = P4_MCTruth_MuonMinus.size();
  
  // Initial two muons
  m_mc_init_n_muon_plus  = n_init_mup;
  m_mc_init_n_muon_minus = n_init_mum;

  m_mc_init_mup_px = P4_MCTruth_MuonPlus[0].Px();
  m_mc_init_mup_py = P4_MCTruth_MuonPlus[0].Py();
  m_mc_init_mup_pz = P4_MCTruth_MuonPlus[0].Pz();
  m_mc_init_mup_e = P4_MCTruth_MuonPlus[0].E();
  
  m_mc_init_mup_pt = P4_MCTruth_MuonPlus[0].Pt();
  
  m_mc_init_mum_px = P4_MCTruth_MuonMinus[0].Px();
  m_mc_init_mum_py = P4_MCTruth_MuonMinus[0].Py();
  m_mc_init_mum_pz = P4_MCTruth_MuonMinus[0].Pz();
  m_mc_init_mum_e  = P4_MCTruth_MuonMinus[0].E();
  
  m_mc_init_mum_pt = P4_MCTruth_MuonMinus[0].Pt();
  
  double mll     = ( P4_MCTruth_MuonPlus[0] + P4_MCTruth_MuonMinus[0] ).M();
  double pll     = ( P4_MCTruth_MuonPlus[0] + P4_MCTruth_MuonMinus[0] ).P();
  double ptll    = ( P4_MCTruth_MuonPlus[0] + P4_MCTruth_MuonMinus[0] ).Pt();
  double ell     = ( P4_MCTruth_MuonPlus[0] + P4_MCTruth_MuonMinus[0] ).E();
  double rec_mll = ( P4_Ecms - P4_MCTruth_MuonPlus[0] - P4_MCTruth_MuonMinus[0] ).M();
  double dphi    = fabs(P4_MCTruth_MuonPlus[0].DeltaPhi(P4_MCTruth_MuonMinus[0])) *180.0/M_PI;
  double dang    = P4_MCTruth_MuonPlus[0].Angle(P4_MCTruth_MuonMinus[0].Vect())   *180.0/M_PI;
  
  m_mc_init_dimuon_m = mll;
  m_mc_init_dimuon_p = pll;
  m_mc_init_dimuon_pt = ptll;
  m_mc_init_dimuon_e = ell;
  m_mc_init_dimuon_rec_m = rec_mll;
  m_mc_init_dimuon_dphi = dphi;
  m_mc_init_dimuon_dang = dang;

  // Initial Higgs
  m_mc_higgs_m = P4_MCTruth_Higgs[0].M();
  m_mc_higgs_e = P4_MCTruth_Higgs[0].E();
  m_mc_higgs_rec_m = ( P4_Ecms - P4_MCTruth_Higgs[0] ).M();

  // Zboson
  int flag1=0;
  int flag2=0;
  //*******  Z1 decay combination   *******//
  // Z1->qq
  if( abs(m_mc_z1_daughter_pid[0]) >= 1 && abs(m_mc_z1_daughter_pid[0]) <= 6 ) { flag1 = 1; }

  // Z1->nunu
  if( abs(m_mc_z1_daughter_pid[0]) == ELECTRON_NEUTRINO_PID ||
      abs(m_mc_z1_daughter_pid[0]) == MUON_NEUTRINO_PID     ||
      abs(m_mc_z1_daughter_pid[0]) == TAU_NEUTRINO_PID         ) { flag1 = 2; }

  // Z1->ll
  if( abs(m_mc_z1_daughter_pid[0]) == ELECTRON_PID ||
      abs(m_mc_z1_daughter_pid[0]) == MUON_PID     ||
      abs(m_mc_z1_daughter_pid[0]) == TAU_PID         ) { flag1 = 3; }

  // Strange !
  if( (m_mc_z1_daughter_pid[0] + m_mc_z1_daughter_pid[1]) != 0 ) { flag1 = 4; }
  
  //*******  Z2 decay combination   *******//
  // Z2->qq
  if( abs(m_mc_z2_daughter_pid[0]) >= 1 && abs(m_mc_z2_daughter_pid[0]) <= 6 ) { flag2 = 1; }

  // Z2->nunu
  if( abs(m_mc_z2_daughter_pid[0]) == ELECTRON_NEUTRINO_PID ||
      abs(m_mc_z2_daughter_pid[0]) == MUON_NEUTRINO_PID     ||
      abs(m_mc_z2_daughter_pid[0]) == TAU_NEUTRINO_PID         ) { flag2 = 2; }

  // Z2->ll
  if( abs(m_mc_z2_daughter_pid[0]) == ELECTRON_PID ||
      abs(m_mc_z2_daughter_pid[0]) == MUON_PID     ||
      abs(m_mc_z2_daughter_pid[0]) == TAU_PID         ) { flag2 = 3; }

  // Strange !
  if( (m_mc_z2_daughter_pid[0] + m_mc_z2_daughter_pid[1]) != 0 ) { flag2 = 4; }

  m_mc_zz_flag = flag2*10 + flag1;

  if( flag1==1 && flag2==1 )std::cout << "Event is ZZ*->qqqq" << std::endl;

  // Remove Neutrino Component
  
  TLorentzVector p4_z1_1, p4_z1_2;
  TLorentzVector p4_z2_1, p4_z2_2;

  TLorentzVector p4_null(0,0,0,0);

  p4_z1_1 = P4_MCTruth_Z1[0];
  p4_z1_2 = P4_MCTruth_Z1[1];
  p4_z2_1 = P4_MCTruth_Z2[0];
  p4_z2_2 = P4_MCTruth_Z2[1];
  
  if( flag1 == 2 ) { // neutrino
    
    p4_z1_1 = p4_null;
    p4_z1_2 = p4_null;
  }
  if( flag2 == 2 ) { // neutrino
    
    p4_z2_1 = p4_null;
    p4_z2_2 = p4_null;
  }

  double z1_m  = ( p4_z1_1 + p4_z1_2 ).M();
  double z1_p  = ( p4_z1_1 + p4_z1_2 ).P();
  double z1_pt = ( p4_z1_1 + p4_z1_2 ).Pt();
  double z1_e  = ( p4_z1_1 + p4_z1_2 ).E();
  double z1_rec_m  = ( P4_Ecms - p4_z1_1 - p4_z1_2 ).M();

  double z2_m  = ( p4_z2_1 + p4_z2_2 ).M();
  double z2_p  = ( p4_z2_1 + p4_z2_2 ).P();
  double z2_pt = ( p4_z2_1 + p4_z2_2 ).Pt();
  double z2_e  = ( p4_z2_1 + p4_z2_2 ).E();
  double z2_rec_m  = ( P4_Ecms - p4_z2_1 - p4_z2_2 ).M();

  double z1z2_m = ( p4_z1_1 + p4_z1_2 + p4_z2_1 + p4_z2_2 ).M();
  double z1z2_e = ( p4_z1_1 + p4_z1_2 + p4_z2_1 + p4_z2_2 ).E();
  double z1z2_rec_m = ( P4_Ecms - p4_z1_1 - p4_z1_2 - p4_z2_1 - p4_z2_2 ).M();

  m_mc_z1_m  = z1_m;
  m_mc_z1_p  = z1_p;
  m_mc_z1_pt = z1_pt;
  m_mc_z1_e  = z1_e;
  m_mc_z1_rec_m = z1_rec_m;

  m_mc_z2_m  = z2_m;
  m_mc_z2_p  = z2_p;
  m_mc_z2_pt = z2_pt;
  m_mc_z2_e  = z2_e;
  m_mc_z2_rec_m = z2_rec_m;

  m_mc_z1z2_m = z1z2_m;
  m_mc_z1z2_e = z1z2_e;
  m_mc_z1z2_rec_m = z1z2_rec_m;
  
  
}

