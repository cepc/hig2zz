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
#include <TH1.h>
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

  TH1F* h_evtflw; 
  TH1F* h_mc_init_plist;
  TH1F* h_mc_higgs_dlist;

  // paramter setting
  int    OverWrite;       // tree overwrite option: 1(re-create)=default or 0(update) 
  int    EcmsOption;
  int    JetAlgorithm;
  int    TagLeptonID;
  double Ecms;
  double LeptonEMax;
  double LeptonEMin;
  double LeptonPtMin;
  double EjetMin;
  int JetNpfoMin;

  TLorentzVector P4_Ecms;

  // common info
  unsigned int m_event;  

  // Collection
  LCCollection* Col_WoLeps;
  LCCollection* Col_FastJet;
  LCCollection* Col_FJPList1;
  LCCollection* Col_FJPList2;
  LCCollection* Col_Jets;
  LCCollection* Col_Leps;
  LCCollection* Col_Reco;
  LCCollection* Col_MC;
  MCParticle *a1_MC;

  // pfo 
  int m_n_col_reco;

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
  std::vector<double> m_mu_charge;

  double m_lepton_pt_sum;

  TLorentzVector P4_Z_MuonPlus;  
  TLorentzVector P4_Z_MuonMinus;  
  std::vector<TLorentzVector> P4_MuonPlus;  
  std::vector<TLorentzVector> P4_MuonMinus;

  std::vector<double> m_mup_e;
  std::vector<double> m_mup_p;
  std::vector<double> m_mup_pt;
  std::vector<double> m_mup_px;
  std::vector<double> m_mup_py;
  std::vector<double> m_mup_pz;

  std::vector<double> m_mum_e;
  std::vector<double> m_mum_p;
  std::vector<double> m_mum_pt;
  std::vector<double> m_mum_px;
  std::vector<double> m_mum_py;
  std::vector<double> m_mum_pz;

  std::vector<double> m_dimuon_m;
  std::vector<double> m_dimuon_p;
  std::vector<double> m_dimuon_pt;
  std::vector<double> m_dimuon_px;
  std::vector<double> m_dimuon_py;
  std::vector<double> m_dimuon_pz;
  std::vector<double> m_dimuon_e;
  std::vector<double> m_dimuon_rec_m;
  std::vector<double> m_dimuon_dphi;
  std::vector<double> m_dimuon_dang;

  // lepton cone info
  std::vector<int> m_cone_lp_npfo;
  std::vector<double> m_cone_lp_track_energy;
  std::vector<double> m_cone_lp_cone_energy;
  std::vector<double> m_cone_lp_energy_ratio;
  std::vector<double> m_cone_lp_simple_averaged_angle;
  std::vector<double> m_cone_lp_weight_averaged_angle;

  std::vector<int> m_cone_lm_npfo;
  std::vector<double> m_cone_lm_track_energy;
  std::vector<double> m_cone_lm_cone_energy;
  std::vector<double> m_cone_lm_energy_ratio;
  std::vector<double> m_cone_lm_simple_averaged_angle;
  std::vector<double> m_cone_lm_weight_averaged_angle;

  // jet info
  int m_fastjet_flag;
  int m_n_jet;
  std::vector<TLorentzVector> P4_Jet;  

  std::vector<double> m_jet_m;
  std::vector<double> m_jet_p;
  std::vector<double> m_jet_pt;
  std::vector<double> m_jet_px;
  std::vector<double> m_jet_py;
  std::vector<double> m_jet_pz;
  std::vector<double> m_jet_e;

  std::vector<double> m_jet_lead_e;
  std::vector<double> m_jet_sub_e;

  std::vector<double> m_jet_phi;
  std::vector<double> m_jet_theta;

  std::vector<double> m_dijet_m;
  std::vector<double> m_dijet_p;
  std::vector<double> m_dijet_pt;
  std::vector<double> m_dijet_px;
  std::vector<double> m_dijet_py;
  std::vector<double> m_dijet_pz;
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

  std::vector<double> m_btag;
  std::vector<double> m_ctag;
  std::vector<double> m_bctag;
  std::vector<double> m_category;

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

  int m_fastjet_npfo1;
  int m_fastjet_npfo2;

  // save variables
  double m_lljj_m;
  double m_lljj_cos;
  double m_rec_lljj_m;
  double m_rec_lljj_e;
  double m_lj_angle;
  double m_lj_minangle;
  double m_vis_all_m;
  double m_vis_all_e;
  double m_vis_all_p;
  double m_vis_all_pt;
  double m_vis_all_px;
  double m_vis_all_py;
  double m_vis_all_pz;
  double m_vis_all_cos;
  double m_cos;
  double m_vis_ex_dimuon_m;
  double m_vis_ex_dimuon_e;
  double m_vis_all_rec_m;
  double m_vis_all_rec_e;
  double m_vis_all_rec_px;
  double m_vis_all_rec_py;
  double m_vis_all_rec_pz;

  // MC info 
  std::vector<int> m_mc_pdgid;
  std::vector<int> m_mc_init_pdgid;
  std::vector<TLorentzVector> P4_MCTruth_LeptonPlus;  
  std::vector<TLorentzVector> P4_MCTruth_LeptonMinus;
  std::vector<TLorentzVector> P4_MCTruth_photon;
  std::vector<TLorentzVector> P4_MCTruth_Higgs;   

  int m_mc_lepton_minus_id;
  int m_mc_lepton_plus_id;
  int m_mc_neutrino_minus_id;
  int m_mc_neutrino_plus_id;
  int m_mc_quark_minus_id;
  int m_mc_quark_plus_id;

  int m_mc_init_n_lepton_plus;
  int m_mc_init_n_lepton_minus;

  double m_mc_init_leptonp_e;
  double m_mc_init_leptonp_p;
  double m_mc_init_leptonp_pt;
  double m_mc_init_leptonp_px;
  double m_mc_init_leptonp_py;
  double m_mc_init_leptonp_pz;

  double m_mc_init_leptonp_phi;
  double m_mc_init_leptonp_theta;

  double m_mc_init_leptonm_e;
  double m_mc_init_leptonm_p;
  double m_mc_init_leptonm_pt;
  double m_mc_init_leptonm_px;
  double m_mc_init_leptonm_py;
  double m_mc_init_leptonm_pz;

  double m_mc_init_leptonm_phi;
  double m_mc_init_leptonm_theta;

  double m_mc_init_dilepton_m;
  double m_mc_init_dilepton_e;
  double m_mc_init_dilepton_p;
  double m_mc_init_dilepton_pt;
  double m_mc_init_dilepton_pz;

  double m_mc_init_dilepton_rec_m;
  double m_mc_init_dilepton_dphi;
  double m_mc_init_dilepton_dang;

  int m_mc_init_n_photon;
  std::vector<double> m_mc_init_photon_e;
  std::vector<double> m_mc_init_photon_p;
  std::vector<double> m_mc_init_photon_pt;
  std::vector<double> m_mc_init_photon_pz;
  std::vector<double> m_mc_init_photon_phi;  
  std::vector<double> m_mc_init_photon_theta;

  double m_mc_higgs_m;
  double m_mc_higgs_e;
  double m_mc_higgs_rec_m;

  int m_mc_n_Zboson;
  int m_mc_higgs_decay_type;
  std::vector<int> m_mc_higgs_daughter_pdgid;
  std::vector<int> m_mc_z1_daughter_pid;
  std::vector<int> m_mc_z2_daughter_pid;
  std::vector<TLorentzVector> P4_MCTruth_Z1;  
  std::vector<TLorentzVector> P4_MCTruth_Z2;  
  std::vector<int> m_mc_w1_daughter_pid;
  std::vector<int> m_mc_w2_daughter_pid;
  std::vector<TLorentzVector> P4_MCTruth_W1;  
  std::vector<TLorentzVector> P4_MCTruth_W2;  

  double m_mc_zw1_m;
  double m_mc_zw1_p;
  double m_mc_zw1_pt;
  double m_mc_zw1_e;
  double m_mc_zw1_rec_m;

  double m_mc_zw2_m;
  double m_mc_zw2_p;
  double m_mc_zw2_pt;
  double m_mc_zw2_e;
  double m_mc_zw2_rec_m;
   
  double m_mc_zw1zw2_m;
  double m_mc_zw1zw2_e;
  double m_mc_zw1zw2_rec_m;

  int m_mc_zz_flag;
  int m_mc_ww_flag;
  int m_mc_h2gaugeboson_flag;


  // functions
  void book_histogram();
  void book_tree();
  void clearVariables();
  void setECMS();
  bool buildHiggsToZZ();

  void saveNeutral( LCCollection* col_PFOs );
  void savePhotons( LCCollection* col_PFOs );
  void selectCharged( LCCollection* col_IsoLeps );

  void selectLeptons( LCCollection* col_IsoLeps );
  void saveLeptonInfo( std::vector<TLorentzVector> p4_muon_plus, std::vector<TLorentzVector> p4_muon_minus );

  void saveLeptonConeInfo( std::vector<TLorentzVector> p4_muon_plus, std::vector<TLorentzVector> p4_muon_minus,
			   LCCollection* col_PFOs );

  void selectJets( LCCollection* col_Jets, LCCollection* col_rec1 , LCCollection* col_rec2 );
  void saveJetInfo( std::vector<TLorentzVector> p4_jet );
  void saveFastJet( LCCollection* col_Jets , LCCollection* col_rec1 , LCCollection* col_rec2 );
  void saveFlavorTag_and_Distance( LCCollection* col_Jets, std::string jet_processor_name );
  void saveVariables();

  void checkGenMCInfo( LCCollection* col_MC );
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
const int W_PID                  = 24;
const int HIGGS_PID              = 25;

const double Z_MASS              = 91.2;



Higgs2zz a_higgs2zz_instance;



Higgs2zz::Higgs2zz() : Processor("Higgs2zz") {

  registerProcessorParameter( "TreeOutputFile" , "Output Filename" , FileName , std::string("default.root"));

  registerProcessorParameter( "TreeName" , "ROOT tree name" , TreeName , std::string("tree"));

  registerProcessorParameter( "Ecms" , "ECMS value in GeV." , Ecms , 240.0);

  registerProcessorParameter( "EcmsOption" , "Use ECMS (1) or with Gaussian Blur (0)." , EcmsOption , 1);

  registerProcessorParameter( "OverwriteFile" , "Re-create (1) or Update (0)" , OverWrite , 1 );

  registerProcessorParameter( "LeptonFlavorID" , "Tagging lepton flavor ID" , TagLeptonID, 13);

  registerProcessorParameter( "LeptonEMax" , "Maximum energy of leptons in GeV" , LeptonEMax , 1e+20);

  registerProcessorParameter( "LeptonEMin" , "Minimum energy of leptons in GeV" , LeptonEMin , 3.0);

  registerProcessorParameter( "LeptonPtMin" , "Minimum Pt of leptons in GeV" , LeptonPtMin , 0.0);

  registerProcessorParameter( "EjetMin" , "Minimum Energy of jet in GeV" , EjetMin , 1.0);

  registerProcessorParameter( "JetNpfoMin" , "Minimum npfo in a jet" , JetNpfoMin , 5);

  registerProcessorParameter( "JetAlgorithm" , "Jet Processor Flag. LCFIplus is ON (1) or not (0)" , JetAlgorithm , 0);

}

void Higgs2zz::init() {

  book_histogram();
  book_tree();
}

void Higgs2zz::processEvent( LCEvent * evt ) {	

  if(evt){
    try{
      
      clearVariables();
      setECMS();

      m_event=evt->getEventNumber();

      h_evtflw->Fill(0); // raw event 
      
      // Read MC info. 
      Col_MC      = evt->getCollection( "MCParticle"     );
      checkGenMCInfo( Col_MC );
      
      if( JetAlgorithm == 1 )  // if LCFIplus processor is turned on. 
	Col_Jets   = evt->getCollection( "RefinedJets"    );   

      Col_FastJet  = evt->getCollection( "FastJets"       );   // FastJet
      Col_FJPList1 = evt->getCollection( "FJPList1"       );   // FastJet, List of rec. particle list for jet1
      Col_FJPList2 = evt->getCollection( "FJPList2"       );   // FastJet, List of rec. particle list for jet2
      Col_Leps     = evt->getCollection( "IsoLeps"        );    
      Col_WoLeps   = evt->getCollection( "WithoutIsoLeps" ); 
      Col_Reco     = evt->getCollection( "ArborPFOs"      );

      h_evtflw->Fill(1); // Does collection exist or not                         

      if( buildHiggsToZZ() ) {

	m_n_col_reco = Col_Reco->getNumberOfElements();

	// Save variables
	saveNeutral( Col_Reco );
	savePhotons( Col_Reco );
	selectCharged( Col_Reco );
	
	// Save information related to its "cone" for selected leptons
	saveLeptonConeInfo( P4_MuonPlus, P4_MuonMinus, Col_Reco );

	saveLeptonInfo( P4_MuonPlus, P4_MuonMinus );
	saveJetInfo( P4_Jet );
	saveVariables();

	saveFastJet( Col_FastJet , Col_FJPList1, Col_FJPList2 ); // save FastJet info.

	if( JetAlgorithm == 0 )  // Info from Fastjet
	  saveFlavorTag_and_Distance( Col_FastJet, "fastjet" );
	else                     // Inro from LCFIplus
	  saveFlavorTag_and_Distance( Col_Jets, "lcfiplus" );

	// Save MC Truth info.
	saveMCTruthInfo( Col_MC ); 

	// Fill to the tree
	m_tree->Fill();
      }
    }
    catch (lcio::DataNotAvailableException err) { }
  }
  
}	


bool Higgs2zz::buildHiggsToZZ() {

  // Select Lepton pairs
  selectLeptons( Col_Leps );
  if( m_n_muon_plus==0 || m_n_muon_minus==0 || m_n_lepton!=2 ) return false;

  h_evtflw->Fill(2); // N_{MuonP} > 0 && N_{MuonM} > 0

  // Select Jet pairs
  selectJets( Col_FastJet, Col_FJPList1, Col_FJPList2 ); 

  if( m_n_jet!=2 ) return false;

  h_evtflw->Fill(3); // N_{Jet} == 2

  return true;
}


void Higgs2zz::end() {

  if (m_tree) {
    TFile *tree_file = m_tree->GetCurrentFile(); //just in case we switched to a new file
    tree_file->Write();
    h_evtflw->Write();
    h_mc_init_plist->Write();
    h_mc_higgs_dlist->Write();
    delete tree_file;
  }
}


void Higgs2zz::book_histogram() {

  h_evtflw = new TH1F("hevtflw", "eventflow", 10, 0, 10);

  h_evtflw->GetXaxis()->SetBinLabel(1, "raw");
  h_evtflw->GetXaxis()->SetBinLabel(2, "Collection exist ?");
  h_evtflw->GetXaxis()->SetBinLabel(3, "NmuonP>0 & NmuonM>0");
  h_evtflw->GetXaxis()->SetBinLabel(4, "NJet=2");
  h_evtflw->GetXaxis()->SetBinLabel(5, ""); 
  h_evtflw->GetXaxis()->SetBinLabel(6, "");
  h_evtflw->GetXaxis()->SetBinLabel(7, "");
  h_evtflw->GetXaxis()->SetBinLabel(8, "");
  h_evtflw->GetXaxis()->SetBinLabel(9, "");
  h_evtflw->GetXaxis()->SetBinLabel(10, "");

  h_mc_init_plist = new TH1F("h_mc_init_plist", "mc_init_plist", 80, -40, 40 );
  h_mc_higgs_dlist = new TH1F("h_mc_higgs_dlist", "mc_higgs_dlist", 80, -40, 40 );
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
  m_tree->Branch("n_col_reco", &m_n_col_reco,"n_col_reco/I");
  
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
  
  m_tree->Branch("mu_charge", &m_mu_charge);
  m_tree->Branch("lepton_pt_sum", &m_lepton_pt_sum,  "lepton_pt_sum/D");
  
  m_tree->Branch("mup_e", &m_mup_e);
  m_tree->Branch("mup_p", &m_mup_p);
  m_tree->Branch("mup_pt", &m_mup_pt);
  m_tree->Branch("mup_px",&m_mup_px);
  m_tree->Branch("mup_py",&m_mup_py);
  m_tree->Branch("mup_pz", &m_mup_pz);
  
  m_tree->Branch("mum_e", &m_mum_e);
  m_tree->Branch("mum_p", &m_mum_p);
  m_tree->Branch("mum_pt", &m_mum_pt);
  m_tree->Branch("mum_px", &m_mum_px);
  m_tree->Branch("mum_py", &m_mum_py);
  m_tree->Branch("mum_pz", &m_mum_pz);

  m_tree->Branch("dimuon_e", &m_dimuon_e);  
  m_tree->Branch("dimuon_p", &m_dimuon_p);
  m_tree->Branch("dimuon_pt", &m_dimuon_pt);
  m_tree->Branch("dimuon_px", &m_dimuon_px);
  m_tree->Branch("dimuon_py", &m_dimuon_py);
  m_tree->Branch("dimuon_pz", &m_dimuon_pz);
  m_tree->Branch("dimuon_m", &m_dimuon_m);

  m_tree->Branch("dimuon_rec_m", &m_dimuon_rec_m);
  m_tree->Branch("dimuon_dphi", &m_dimuon_dphi);
  m_tree->Branch("dimuon_dang", &m_dimuon_dang);
  

  // Lepton Cone Info.
  m_tree->Branch("cone_lp_npfo", &m_cone_lp_npfo);
  m_tree->Branch("cone_lp_track_energy", &m_cone_lp_track_energy);
  m_tree->Branch("cone_lp_cone_energy", &m_cone_lp_cone_energy);
  m_tree->Branch("cone_lp_energy_ratio", &m_cone_lp_energy_ratio);
  m_tree->Branch("cone_lp_simple_averaged_angle", &m_cone_lp_simple_averaged_angle);
  m_tree->Branch("cone_lp_weight_averaged_angle", &m_cone_lp_weight_averaged_angle);

  m_tree->Branch("cone_lm_npfo", &m_cone_lm_npfo);
  m_tree->Branch("cone_lm_track_energy", &m_cone_lm_track_energy);
  m_tree->Branch("cone_lm_cone_energy", &m_cone_lm_cone_energy);
  m_tree->Branch("cone_lm_energy_ratio", &m_cone_lm_energy_ratio);
  m_tree->Branch("cone_lm_simple_averaged_angle", &m_cone_lm_simple_averaged_angle);
  m_tree->Branch("cone_lm_weight_averaged_angle", &m_cone_lm_weight_averaged_angle);


  // Jets
  m_tree->Branch("n_jet",  &m_n_jet,  "m_n_jet/I");
  m_tree->Branch("fastjet_flag", &m_fastjet_flag, "m_fastjet_flag/I");

  m_tree->Branch("jet_m", &m_jet_m);
  m_tree->Branch("jet_p", &m_jet_p);
  m_tree->Branch("jet_pt", &m_jet_pt);
  m_tree->Branch("jet_px", &m_jet_px);
  m_tree->Branch("jet_py", &m_jet_py);
  m_tree->Branch("jet_pz", &m_jet_pz);
  m_tree->Branch("jet_e", &m_jet_e);
  m_tree->Branch("jet_lead_e", &m_jet_lead_e);
  m_tree->Branch("jet_sub_e", &m_jet_sub_e);

  m_tree->Branch("jet_phi", &m_jet_phi);
  m_tree->Branch("jet_theta", &m_jet_theta);
  
  m_tree->Branch("dijet_e", &m_dijet_e);
  m_tree->Branch("dijet_p", &m_dijet_p);
  m_tree->Branch("dijet_pt", &m_dijet_pt);
  m_tree->Branch("dijet_px", &m_dijet_px);
  m_tree->Branch("dijet_py", &m_dijet_py);
  m_tree->Branch("dijet_pz", &m_dijet_pz);
  m_tree->Branch("dijet_m", &m_dijet_m);
  m_tree->Branch("dijet_rec_m", &m_dijet_rec_m);
  m_tree->Branch("dijet_dphi", &m_dijet_dphi);
  m_tree->Branch("dijet_dang", &m_dijet_dang);
  
  m_tree->Branch("y12", &m_y12, "y12/D");
  m_tree->Branch("y23", &m_y23, "y23/D");
  m_tree->Branch("y34", &m_y34, "y34/D");
  m_tree->Branch("y45", &m_y45, "y45/D");
  m_tree->Branch("y56", &m_y56, "y56/D");
  m_tree->Branch("y67", &m_y67, "y67/D");

  m_tree->Branch("btag", &m_btag);
  m_tree->Branch("ctag", &m_ctag);
  m_tree->Branch("bctag", &m_bctag);
  m_tree->Branch("category", &m_category);
  
  m_tree->Branch("n_fastjet",  &m_nfastjet,  "n_fastjet/I");	
  m_tree->Branch("fastjet_px", &m_fastjet_px);
  m_tree->Branch("fastjet_py", &m_fastjet_py);
  m_tree->Branch("fastjet_pz", &m_fastjet_pz);
  m_tree->Branch("fastjet_e", &m_fastjet_e);
  
  m_tree->Branch("dijet_m_fastjet", &m_dijet_m_fastjet, "dijet_m_fastjet/D"); 
  m_tree->Branch("dijet_p_fastjet", &m_dijet_p_fastjet, "dijet_p_fastjet/D");
  m_tree->Branch("dijet_e_fastjet", &m_dijet_e_fastjet, "dijet_e_fastjet/D"); 
  m_tree->Branch("dijet_rec_m_fastjet", &m_dijet_rec_m_fastjet, "dijet_rec_m_fastjet/D");

  m_tree->Branch("fastjet_npfo1", &m_fastjet_npfo1, "fastjet_npfo1/I");
  m_tree->Branch("fastjet_npfo2", &m_fastjet_npfo2, "fastjet_npfo2/I");
  
  // other variables to be stored.
  m_tree->Branch("lljj_m", &m_lljj_m, "lljj_m/D");
  m_tree->Branch("lljj_cos", &m_lljj_cos, "lljj_cos/D");

  m_tree->Branch("rec_lljj_m", &m_rec_lljj_m, "rec_lljj_m/D");
  m_tree->Branch("rec_lljj_e", &m_rec_lljj_e, "rec_lljj_e/D");
  m_tree->Branch("lj_angle", &m_lj_angle, "lj_angle/D");
  m_tree->Branch("lj_minangle", &m_lj_minangle, "lj_minangle/D");
  
  m_tree->Branch("vis_ex_dimuon_m", &m_vis_ex_dimuon_m, "vis_ex_dimuon_m/D");
  m_tree->Branch("vis_ex_dimuon_e", &m_vis_ex_dimuon_e, "vis_ex_dimuon_e/D");
  m_tree->Branch("vis_all_m", &m_vis_all_m, "vis_all_m/D");
  m_tree->Branch("vis_all_e", &m_vis_all_e, "vis_all_e/D");
  m_tree->Branch("vis_all_p", &m_vis_all_p, "vis_all_p/D");
  m_tree->Branch("vis_all_pt", &m_vis_all_pt, "vis_all_pt/D");
  m_tree->Branch("vis_all_px", &m_vis_all_px, "vis_all_px/D");
  m_tree->Branch("vis_all_py", &m_vis_all_py, "vis_all_py/D");
  m_tree->Branch("vis_all_pz", &m_vis_all_pz, "vis_all_pz/D");
  m_tree->Branch("vis_all_cos", &m_vis_all_cos, "vis_all_cos/D");
  m_tree->Branch("cos", &m_cos, "cos/D");
  m_tree->Branch("vis_all_rec_m", &m_vis_all_rec_m, "vis_all_rec_m/D");
  m_tree->Branch("vis_all_rec_e", &m_vis_all_rec_e, "vis_all_rec_e/D");
  m_tree->Branch("vis_all_rec_px", &m_vis_all_rec_px, "vis_all_rec_px/D");
  m_tree->Branch("vis_all_rec_py", &m_vis_all_rec_py, "vis_all_rec_py/D");
  m_tree->Branch("vis_all_rec_pz", &m_vis_all_rec_pz, "vis_all_rec_pz/D"); 
  
  // MC info 
  m_tree->Branch("mc_pdgid", &m_mc_pdgid);
  m_tree->Branch("mc_init_pdgid", &m_mc_init_pdgid);
  
  m_tree->Branch("mc_lepton_minus_id", &m_mc_lepton_minus_id, "mc_lepton_minus_id/I");
  m_tree->Branch("mc_lepton_plus_id", &m_mc_lepton_plus_id, "mc_lepton_plus_id/I");
  m_tree->Branch("mc_neutrino_minus_id", &m_mc_neutrino_minus_id, "mc_neutrino_minus_id/I");
  m_tree->Branch("mc_neutrino_plus_id", &m_mc_neutrino_plus_id, "mc_neutrino_plus_id/I");
  m_tree->Branch("mc_quark_minus_id", &m_mc_quark_minus_id, "mc_quark_minus_id/I");
  m_tree->Branch("mc_quark_plus_id", &m_mc_quark_plus_id, "mc_quark_plus_id/I");
  m_tree->Branch("mc_init_n_lepton_plus", &m_mc_init_n_lepton_plus,  "mc_init_n_lepton_plus/I");
  m_tree->Branch("mc_init_n_lepton_minus", &m_mc_init_n_lepton_minus,  "mc_init_n_lepton_minus/I");
  
  m_tree->Branch("mc_init_leptonp_e",  &m_mc_init_leptonp_e,   "mc_init_leptonp_e/D");
  m_tree->Branch("mc_init_leptonp_p",  &m_mc_init_leptonp_p,   "mc_init_leptonp_p/D");
  m_tree->Branch("mc_init_leptonp_pt", &m_mc_init_leptonp_pt,  "mc_init_leptonp_pt/D");
  m_tree->Branch("mc_init_leptonp_px", &m_mc_init_leptonp_px,  "mc_init_leptonp_px/D");
  m_tree->Branch("mc_init_leptonp_py", &m_mc_init_leptonp_py,  "mc_init_leptonp_py/D");
  m_tree->Branch("mc_init_leptonp_pz", &m_mc_init_leptonp_pz,  "mc_init_leptonp_pz/D");

  m_tree->Branch("mc_init_leptonp_phi", &m_mc_init_leptonp_phi,  "mc_init_leptonp_phi/D");
  m_tree->Branch("mc_init_leptonp_theta", &m_mc_init_leptonp_theta,  "mc_init_leptonp_theta/D");
  
  m_tree->Branch("mc_init_leptonm_e",  &m_mc_init_leptonm_e,   "mc_init_leptonm_e/D");
  m_tree->Branch("mc_init_leptonm_p",  &m_mc_init_leptonm_p,   "mc_init_leptonm_p/D");
  m_tree->Branch("mc_init_leptonm_pt", &m_mc_init_leptonm_pt,  "mc_init_leptonm_pt/D");
  m_tree->Branch("mc_init_leptonm_px", &m_mc_init_leptonm_px,  "mc_init_leptonm_px/D");
  m_tree->Branch("mc_init_leptonm_py", &m_mc_init_leptonm_py,  "mc_init_leptonm_py/D");
  m_tree->Branch("mc_init_leptonm_pz", &m_mc_init_leptonm_pz,  "mc_init_leptonm_pz/D");

  m_tree->Branch("mc_init_leptonm_phi", &m_mc_init_leptonm_phi,  "mc_init_leptonm_phi/D");
  m_tree->Branch("mc_init_leptonm_theta", &m_mc_init_leptonm_theta,  "mc_init_leptonm_theta/D");
  
  m_tree->Branch("mc_init_dilepton_m",  &m_mc_init_dilepton_m,   "mc_init_dilepton_m/D");
  m_tree->Branch("mc_init_dilepton_e",  &m_mc_init_dilepton_e,   "mc_init_dilepton_e/D");
  m_tree->Branch("mc_init_dilepton_p",  &m_mc_init_dilepton_p,   "mc_init_dilepton_p/D");
  m_tree->Branch("mc_init_dilepton_pt", &m_mc_init_dilepton_pt,  "mc_init_dilepton_pt/D");
  m_tree->Branch("mc_init_dilepton_pz", &m_mc_init_dilepton_pz,  "mc_init_dilepton_pz/D");
  m_tree->Branch("mc_init_dilepton_rec_m", &m_mc_init_dilepton_rec_m,  "mc_init_dilepton_rec_m/D");
  m_tree->Branch("mc_init_dilepton_dphi", &m_mc_init_dilepton_dphi,  "mc_init_dilepton_dphi/D");
  m_tree->Branch("mc_init_dilepton_dang", &m_mc_init_dilepton_dang,  "mc_init_dilepton_dang/D");
  
  m_tree->Branch("mc_init_n_photon", &m_mc_init_n_photon,  "mc_init_n_photon/I");
  m_tree->Branch("mc_init_photon_e",  &m_mc_init_photon_e);
  m_tree->Branch("mc_init_photon_p",  &m_mc_init_photon_p);
  m_tree->Branch("mc_init_photon_pt",  &m_mc_init_photon_pt);
  m_tree->Branch("mc_init_photon_pz",  &m_mc_init_photon_pz);
  m_tree->Branch("mc_init_photon_phi",  &m_mc_init_photon_phi);
  m_tree->Branch("mc_init_photon_theta",  &m_mc_init_photon_theta);

  m_tree->Branch("mc_higgs_m", &m_mc_higgs_m, "mc_higgs_m/D");
  m_tree->Branch("mc_higgs_e", &m_mc_higgs_e, "mc_higgs_e/D");
  m_tree->Branch("mc_higgs_rec_m", &m_mc_higgs_rec_m, "mc_higgs_rec_m/D");
  m_tree->Branch("mc_higgs_decay_type", &m_mc_higgs_decay_type, "mc_higgs_decay_type/I");
  m_tree->Branch("mc_higgs_daughter_pdgid", &m_mc_higgs_daughter_pdgid);
 
  m_tree->Branch("mc_n_Zboson", &m_mc_n_Zboson, "mc_n_Zboson/I");
  
  m_tree->Branch("mc_z1_daughter_pid", &m_mc_z1_daughter_pid);
  m_tree->Branch("mc_z2_daughter_pid", &m_mc_z2_daughter_pid);

  m_tree->Branch("mc_w1_daughter_pid", &m_mc_w1_daughter_pid);
  m_tree->Branch("mc_w2_daughter_pid", &m_mc_w2_daughter_pid);
  
  m_tree->Branch("mc_zw1_m", &m_mc_zw1_m, "mc_zw1_m/D");
  m_tree->Branch("mc_zw1_p", &m_mc_zw1_p, "mc_zw1_p/D");
  m_tree->Branch("mc_zw1_pt", &m_mc_zw1_pt, "mc_zw1_pt/D");
  m_tree->Branch("mc_zw1_e", &m_mc_zw1_e, "mc_zw1_e/D");
  m_tree->Branch("mc_zw1_rec_m", &m_mc_zw1_rec_m, "mc_zw1_rec_m/D");
  
  m_tree->Branch("mc_zw2_m", &m_mc_zw2_m, "mc_zw2_m/D");
  m_tree->Branch("mc_zw2_p", &m_mc_zw2_p, "mc_zw2_p/D");
  m_tree->Branch("mc_zw2_pt", &m_mc_zw2_pt, "mc_zw2_pt/D");
  m_tree->Branch("mc_zw2_e", &m_mc_zw2_e, "mc_zw2_e/D");
  m_tree->Branch("mc_zw2_rec_m", &m_mc_zw2_rec_m, "mc_zw2_rec_m/D");
  
  m_tree->Branch("mc_zw1zw2_m", &m_mc_zw1zw2_m, "mc_zw1zw2_m/D");
  m_tree->Branch("mc_zw1zw2_e", &m_mc_zw1zw2_e, "mc_zw1zw2_e/D");
  m_tree->Branch("mc_zw1zw2_rec_m", &m_mc_zw1zw2_rec_m, "mc_zw1zw2_rec_m/D");
  m_tree->Branch("mc_zz_flag", &m_mc_zz_flag, "mc_zz_flag/I");
  m_tree->Branch("mc_ww_flag", &m_mc_ww_flag, "mc_ww_flag/I");
  m_tree->Branch("mc_h2gaugeboson_flag", &m_mc_h2gaugeboson_flag, "mc_h2gaugeboson_flag/I");

}

void Higgs2zz::clearVariables() {

  // MC info. 
  m_mc_pdgid.clear();
  m_mc_init_pdgid.clear();
  m_mc_higgs_daughter_pdgid.clear();
  P4_MCTruth_LeptonPlus.clear();
  P4_MCTruth_LeptonMinus.clear();
  P4_MCTruth_photon.clear();
  P4_MCTruth_Higgs.clear();

  m_mc_init_photon_e.clear();
  m_mc_init_photon_p.clear();
  m_mc_init_photon_pt.clear();
  m_mc_init_photon_pz.clear();
  m_mc_init_photon_phi.clear();
  m_mc_init_photon_theta.clear();

  m_mc_z1_daughter_pid.clear();
  m_mc_z2_daughter_pid.clear();
  P4_MCTruth_Z1.clear();
  P4_MCTruth_Z2.clear();

  m_mc_w1_daughter_pid.clear();
  m_mc_w2_daughter_pid.clear();
  P4_MCTruth_W1.clear();
  P4_MCTruth_W2.clear();
  
  // Sum of all neutrals
  for(int i=0;i<4;i++)P4_Neutral_Sum[i]=0.0;
  
  // Sum of all charged 
  for(int i=0;i<4;i++)P4_Charged_Sum[i]=0.0;
  
  // Lepton info.
  for(int i=0;i<4;i++){

    P4_Z_MuonPlus[i]=0.0;
    P4_Z_MuonMinus[i]=0.0;
  }
    
  P4_MuonPlus.clear();
  P4_MuonMinus.clear();
  
  m_mu_charge.clear();

  m_mup_e.clear();
  m_mup_p.clear();
  m_mup_pt.clear();
  m_mup_px.clear();
  m_mup_py.clear();
  m_mup_pz.clear();

  m_mum_e.clear();
  m_mum_p.clear();
  m_mum_pt.clear();
  m_mum_px.clear();
  m_mum_py.clear();
  m_mum_pz.clear();
  
  m_dimuon_m.clear();
  m_dimuon_p.clear();
  m_dimuon_pt.clear();
  m_dimuon_px.clear();
  m_dimuon_py.clear();
  m_dimuon_pz.clear();
  m_dimuon_e.clear();
  m_dimuon_rec_m.clear();
  m_dimuon_dphi.clear();
  m_dimuon_dang.clear();
  
  // Lepton Cone Info.
  m_cone_lp_npfo.clear();
  m_cone_lp_track_energy.clear();
  m_cone_lp_cone_energy.clear();
  m_cone_lp_energy_ratio.clear();
  m_cone_lp_simple_averaged_angle.clear();
  m_cone_lp_weight_averaged_angle.clear();

  m_cone_lm_npfo.clear();
  m_cone_lm_track_energy.clear();
  m_cone_lm_cone_energy.clear();
  m_cone_lm_energy_ratio.clear();
  m_cone_lm_simple_averaged_angle.clear();
  m_cone_lm_weight_averaged_angle.clear();
  
  // Jet info.
  P4_Jet.clear();

  m_jet_m.clear();
  m_jet_p.clear();
  m_jet_pt.clear();
  m_jet_px.clear();
  m_jet_py.clear();
  m_jet_pz.clear();
  m_jet_e.clear();
  m_jet_lead_e.clear();
  m_jet_sub_e.clear();
  m_jet_phi.clear();
  m_jet_theta.clear();

  m_dijet_m.clear();
  m_dijet_p.clear();
  m_dijet_pt.clear();
  m_dijet_px.clear();
  m_dijet_py.clear();
  m_dijet_pz.clear();
  m_dijet_e.clear();
  m_dijet_rec_m.clear();
  m_dijet_dphi.clear();
  m_dijet_dang.clear();
  
  // fast jet
  m_fastjet_px.clear();
  m_fastjet_py.clear();
  m_fastjet_pz.clear();
  m_fastjet_e.clear();
 
  // flavor tag info.
  m_btag.clear();
  m_ctag.clear();
  m_bctag.clear();
  m_category.clear();
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

    counter++;
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
  double lepton_pt_sum=0.0;
  for(int i = 0; i < ncol; i++) {
    ReconstructedParticle *a_Reco = dynamic_cast<EVENT::ReconstructedParticle *>(col_Leps->getElementAt(i));
    if(a_Reco->getCharge()==0) continue;

    int    lepton_pid    = abs(a_Reco->getType());
    double lepton_charge = a_Reco->getCharge();
    double lepton_px     = a_Reco->getMomentum()[0];
    double lepton_py     = a_Reco->getMomentum()[1];
    double lepton_pz     = a_Reco->getMomentum()[2];
    double lepton_e      = a_Reco->getEnergy();
    double lepton_pt     = sqrt(lepton_px*lepton_px + lepton_py*lepton_py );
    
    // For test
    if( lepton_pid == MUON_PID )m_mu_charge.push_back( lepton_charge );
    
    TLorentzVector p4vec(lepton_px, lepton_py, lepton_pz, lepton_e);

    if( lepton_e > LeptonEMin && lepton_e < LeptonEMax && lepton_pt > LeptonPtMin) {  //0.4*sqrt(s) 

      if( lepton_pid == MUON_PID || lepton_pid == ELECTRON_PID || lepton_pid == TAU_PID ) {

	lepton_pt_sum += lepton_pt;          
	nlep++;
      }

      if( lepton_pid == TagLeptonID ) { // Either Muon or Electron

	if( lepton_charge >  0.1 )P4_MuonPlus.push_back( p4vec );
	if( lepton_charge < -0.1 )P4_MuonMinus.push_back( p4vec );
      }
    }

  }
  
  m_n_lepton = nlep;
  m_n_muon_plus  = P4_MuonPlus.size();
  m_n_muon_minus = P4_MuonMinus.size();
  //std::cout << "m_n_muon_plus = " << m_n_muon_plus << ", m_n_muon_minus = " << m_n_muon_minus << std::endl;
  m_lepton_pt_sum = lepton_pt_sum;

  // Select muon pairs from Z pole
  if( m_n_muon_plus > 0 && m_n_muon_minus > 0 ) {

    double tmp_min_diff = 1000.0;
    for(int i=0; i < m_n_muon_plus; i++) {
      
      for(int j=0; j < m_n_muon_minus; j++) {
	
	double dimuon_m = ( P4_MuonPlus[i] + P4_MuonMinus[j] ).M();
	
	if( fabs(dimuon_m - Z_MASS) < tmp_min_diff ) {
	
	  tmp_min_diff = fabs(dimuon_m - Z_MASS);
	  P4_Z_MuonPlus = P4_MuonPlus[i];
	  P4_Z_MuonMinus = P4_MuonMinus[j];
	}
      }
    }
  }

}

void Higgs2zz::saveLeptonConeInfo(std::vector<TLorentzVector> p4_lepton_plus,
				  std::vector<TLorentzVector> p4_lepton_minus,
				  LCCollection* col_PFOs ) {

  std::vector<int> nlep; 
  nlep.push_back(p4_lepton_plus.size()); 
  nlep.push_back(p4_lepton_minus.size());

  std::vector< std::vector<TLorentzVector> > p4;
  p4.push_back(p4_lepton_plus);
  p4.push_back(p4_lepton_minus);

  // Loop for lepton plus & lepton minus.
  // Now assuming that there is at least one lepton plus and one lepton minus
  for(int i = 0; i < static_cast<int>(nlep.size()); i++) {
  
    int nlepton   = nlep[i];
    std::vector<TLorentzVector> p4_lepton = p4[i];  

    // Loop inside lepton plus (lepton minus)
    for(int j = 0; j < nlepton; j++) {
  
      int npfo_within_cone=0;
      double coneE=0;
      double simple_averaged_angle=0.0;
      double weight_averaged_angle=0.0;

      TVector3 P_lepton( p4_lepton[j].Vect() );
      double E_lepton = p4_lepton[j].E();

      // Loop fpr PFOs 
      int npfo = col_PFOs->getNumberOfElements();
      for ( int k = 0; k < npfo; k++ ) {
      
	ReconstructedParticle *a_Reco = dynamic_cast<ReconstructedParticle*>(col_PFOs->getElementAt(k)); 
	TVector3 P( a_Reco->getMomentum() );   
	double E = a_Reco->getEnergy();

	// Skip the pfo, if it is the lepton. It was better to use leptons'pfo directly !
	if( E_lepton == E && P_lepton == P ){ continue; }

	double cosTheta = P_lepton.Dot(P) / ( P_lepton.Mag() * P.Mag() );

	// Count the values inside of the "Cone" 
	if ( cosTheta >= 0.98 ){ // The value 0.98 should be the same as the number in IsolatedLeptonFinder

	  npfo_within_cone++;
	  coneE += E; 

	  double angle = std::acos( cosTheta )* 180.0/M_PI; // convert to unit of degree
	  simple_averaged_angle += angle;
	  weight_averaged_angle += angle * E;
	}
      }
    
      if( npfo_within_cone > 0 ) {
	
	if( i==0 ) { // For lepton plus. 
	  
	  m_cone_lp_npfo.push_back( npfo_within_cone );
	  m_cone_lp_track_energy.push_back( E_lepton );
	  m_cone_lp_cone_energy.push_back( coneE );
	  m_cone_lp_energy_ratio.push_back( coneE / E_lepton );
	  m_cone_lp_simple_averaged_angle.push_back( simple_averaged_angle /= static_cast<double>(npfo_within_cone) );
	  m_cone_lp_weight_averaged_angle.push_back( weight_averaged_angle /= coneE );
	}
	else { // For lepton minus. 
	  
	  m_cone_lm_npfo.push_back( npfo_within_cone );
	  m_cone_lm_track_energy.push_back( E_lepton );
	  m_cone_lm_cone_energy.push_back( coneE );
	  m_cone_lm_energy_ratio.push_back( coneE / E_lepton );
	  m_cone_lm_simple_averaged_angle.push_back( simple_averaged_angle /= static_cast<double>(npfo_within_cone) );
	  m_cone_lm_weight_averaged_angle.push_back( weight_averaged_angle /= coneE );
	}
      }
      else { // push null value
	
	if( i==0 ) { // For lepton plus. 
	  
	  m_cone_lp_npfo.push_back( 0 );
	  m_cone_lp_track_energy.push_back( E_lepton ); 
	  m_cone_lp_cone_energy.push_back( 0.0 );
	  m_cone_lp_energy_ratio.push_back( 0.0 );
	  m_cone_lp_simple_averaged_angle.push_back( 0.0 );
	  m_cone_lp_weight_averaged_angle.push_back( 0.0 );
	}
	else { // For lepton minus. 
	  
	  m_cone_lm_npfo.push_back( 0 );
	  m_cone_lm_track_energy.push_back( E_lepton );
	  m_cone_lm_cone_energy.push_back( 0.0 );
	  m_cone_lm_energy_ratio.push_back( 0.0 );
	  m_cone_lm_simple_averaged_angle.push_back( 0.0 );
	  m_cone_lm_weight_averaged_angle.push_back( 0.0 );
	}
      }
    
    } // End of for(int j = 0; j < nlepton; ...
  } // End of for(int i; i < nlep.size(); ...

}

void Higgs2zz::saveLeptonInfo(std::vector<TLorentzVector> p4_muon_plus, std::vector<TLorentzVector> p4_muon_minus) {

  int nlep_p = p4_muon_plus.size();
  int nlep_m = p4_muon_minus.size();

  for(int i = 0; i < nlep_p; i++) {
  
    for(int j = 0; j < nlep_m; j++) {

      m_mup_e.push_back(p4_muon_plus[i].E());
      m_mup_p.push_back(p4_muon_plus[i].P());
      m_mup_pt.push_back(p4_muon_plus[i].Pt());
      m_mup_px.push_back(p4_muon_plus[i].Px());
      m_mup_py.push_back(p4_muon_plus[i].Py());
      m_mup_pz.push_back(p4_muon_plus[i].Pz());

      m_mum_e.push_back(p4_muon_minus[j].E());
      m_mum_p.push_back(p4_muon_minus[j].P());
      m_mum_pt.push_back(p4_muon_minus[j].Pt());
      m_mum_px.push_back(p4_muon_minus[j].Px());
      m_mum_py.push_back(p4_muon_minus[j].Py());
      m_mum_pz.push_back(p4_muon_minus[j].Pz());

      double mll     = ( p4_muon_plus[i] + p4_muon_minus[j] ).M();
      double pll     = ( p4_muon_plus[i] + p4_muon_minus[j] ).P();
      double ptll    = ( p4_muon_plus[i] + p4_muon_minus[j] ).Pt();
      double pxll    = ( p4_muon_plus[i] + p4_muon_minus[j] ).Px();
      double pyll    = ( p4_muon_plus[i] + p4_muon_minus[j] ).Py();
      double pzll    = ( p4_muon_plus[i] + p4_muon_minus[j] ).Pz();
      double ell     = ( p4_muon_plus[i] + p4_muon_minus[j] ).E();
      double rec_mll = ( P4_Ecms - p4_muon_plus[i] - p4_muon_minus[j] ).M();
      double dphi    = fabs(p4_muon_plus[i].DeltaPhi(p4_muon_minus[j])) *180.0/M_PI;
      double dang    = p4_muon_plus[i].Angle(p4_muon_minus[j].Vect())   *180.0/M_PI;
      
      m_dimuon_m.push_back(mll);
      m_dimuon_p.push_back(pll);
      m_dimuon_pt.push_back(ptll);
      m_dimuon_px.push_back(pxll);
      m_dimuon_py.push_back(pyll);
      m_dimuon_pz.push_back(pzll);
      m_dimuon_e.push_back(ell);
      m_dimuon_rec_m.push_back(rec_mll);
      m_dimuon_dphi.push_back(dphi);
      m_dimuon_dang.push_back(dang);
    }
  }

  // fill dummy value in case of N(muon)=0
  if( nlep_p == 0 ) {

    m_mup_e.push_back( -9999.0 );    
    m_mup_p.push_back( -9999.0 );
    m_mup_pt.push_back( -9999.0 );
    m_mup_px.push_back( -9999.0 );
    m_mup_py.push_back( -9999.0 );
    m_mup_pz.push_back( -9999.0 );
  }

  if( nlep_m == 0 ) {

    m_mum_e.push_back( -9999.0 );    
    m_mum_p.push_back( -9999.0 );
    m_mum_pt.push_back( -9999.0 );
    m_mum_px.push_back( -9999.0 );
    m_mum_py.push_back( -9999.0 );
    m_mum_pz.push_back( -9999.0 );
  }

  if( nlep_p == 0 || nlep_m == 0 ) {

    m_dimuon_m.push_back( -9999.0 );
    m_dimuon_e.push_back( -9999.0 );
    m_dimuon_p.push_back( -9999.0 );
    m_dimuon_pt.push_back( -9999.0 );
    m_dimuon_px.push_back( -9999.0 );
    m_dimuon_py.push_back( -9999.0 );
    m_dimuon_pz.push_back( -9999.0 );
    m_dimuon_rec_m.push_back( -9999.0 );
    m_dimuon_dphi.push_back( -9999.0 );
    m_dimuon_dang.push_back( -9999.0 );
  }

}


void Higgs2zz::saveFastJet( LCCollection* col_Jets , LCCollection* col_rec1 , LCCollection* col_rec2  ) {

  int ncol = col_Jets->getNumberOfElements();
  //std::cout << "nFastJet = " << ncol << std::endl;

  // Save the number of reconstructed particles for each jet
  m_fastjet_npfo1 = col_rec1->getNumberOfElements();
  m_fastjet_npfo2 = col_rec2->getNumberOfElements();

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

    m_dijet_m_fastjet = ( jet1 + jet2 ).M();
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

void Higgs2zz::saveFlavorTag_and_Distance( LCCollection* col_Jets, std::string jet_processor_name ) {

  int ncol = col_Jets->getNumberOfElements();
  
  if( ncol > 0 ) {
    
    if( jet_processor_name == "fastjet" ) {
     
      m_y12 = col_Jets->parameters().getFloatVal( "y_{n-1,n}" );
      m_y23 = col_Jets->parameters().getFloatVal( "y_{n,n+1}" );
      m_y34 = col_Jets->parameters().getFloatVal( "y_{n+1,n+2}" );
      m_y45 = col_Jets->parameters().getFloatVal( "y_{n+2,n+3}" );
      m_y56 = col_Jets->parameters().getFloatVal( "y_{n+3,n+4}" );
      m_y67 = col_Jets->parameters().getFloatVal( "y_{n+4,n+5}" );

      m_btag.push_back(-1.0);    // no flavor information in fastjet
      m_ctag.push_back(-1.0);
      m_bctag.push_back(-1.0);
      m_category.push_back(0.0);
    }
    else if ( jet_processor_name == "lcfiplus" ) {
      
      // Y Distance
      ReconstructedParticle *Jet0 = dynamic_cast<ReconstructedParticle *>(col_Jets->getElementAt(0));
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


      // Flavor Tag
      double tmp_btag  = -1.0;
      double tmp_ctag  = -1.0;
      double tmp_bctag = -1.0;
      double tmp_category = 0.0;  

      int algo   = 0;
      int ibtag  =-1; 
      int ictag  =-1; 
      int ibctag =-1;
      int icat   =-1;

      algo = pidh.getAlgorithmID( "lcfiplus" );
      //algo = pidh.getAlgorithmID( "LCFIFlavourTag" );
      ibtag     = pidh.getParameterIndex (algo,  "BTag");	
      ictag     = pidh.getParameterIndex (algo,  "CTag");	
      ibctag    = pidh.getParameterIndex (algo, "BCTag");
      icat      = pidh.getParameterIndex (algo, "Category");

      for (int j=0 ; j < ncol ; j++ ) {

	ReconstructedParticle *pJet = dynamic_cast<ReconstructedParticle *>(col_Jets->getElementAt(j));
	try {

	  if( ibtag>=0 && ictag>=0 ){
	    const ParticleID &pid = pidh.getParticleID(pJet, algo);
	    tmp_btag  = pid.getParameters()[ibtag ];
	    tmp_ctag  = pid.getParameters()[ictag ];
	    tmp_bctag = pid.getParameters()[ibctag];
	    tmp_category   = pid.getParameters()[icat  ];
	  }
	}
	catch(...) {
	  tmp_btag  = -1.0;
	  tmp_ctag  = -1.0;
	  tmp_bctag = -1.0;
	  tmp_category = 0.0;
	}
	
	// insert to the vector
	m_btag.push_back( tmp_btag );
	m_ctag.push_back( tmp_ctag );
	m_bctag.push_back( tmp_bctag );
	m_category.push_back( tmp_category );
      }
    }
    else {
      
      std::cout << "Input Jet Processor name is wrong. Terminated. "  << std::endl;
      exit(0);
    }
  }
  else {    // ncol == 0
    
    m_y12 = -1.0;
    m_y23 = -1.0;
    m_y34 = -1.0;
    m_y45 = -1.0;
    m_y56 = -1.0;
    m_y67 = -1.0;

    m_btag.push_back(-1.0);
    m_ctag.push_back(-1.0);
    m_bctag.push_back(-1.0);
    m_category.push_back(0.0);
  }
      
}

void Higgs2zz::selectJets( LCCollection* col_Jets, LCCollection* col_rec1 , LCCollection* col_rec2 ) {

  int ncol = col_Jets->getNumberOfElements();
  int jet_npfo1 = col_rec1->getNumberOfElements();
  int jet_npfo2 = col_rec2->getNumberOfElements();
  //std::cout << "njet = " << ncol << std::endl; 

  if ( jet_npfo1 + jet_npfo2 >= JetNpfoMin ) {
    for( int i = 0; i < ncol; i++) {

      ReconstructedParticle *reco_jet = dynamic_cast<EVENT::ReconstructedParticle *>(col_Jets->getElementAt(i));

      double jet_px     = reco_jet->getMomentum()[0];
      double jet_py     = reco_jet->getMomentum()[1];
      double jet_pz     = reco_jet->getMomentum()[2];
      double jet_e      = reco_jet->getEnergy();
    
      TLorentzVector p4vec(jet_px, jet_py, jet_pz, jet_e);

      if ( jet_e > EjetMin ) {
        P4_Jet.push_back( p4vec );
      }
    }
  }

  m_n_jet = P4_Jet.size();

}

void Higgs2zz::saveJetInfo( std::vector<TLorentzVector> p4_jet ) {

  int njet = p4_jet.size();

  // filling leadingjet_e and subleadingjet_e, only true when njet=2
  if (p4_jet[0].E() > p4_jet[1].E())
  {
    m_jet_lead_e.push_back(p4_jet[0].E());
    m_jet_sub_e.push_back(p4_jet[1].E());
  }
  else
  {
    m_jet_lead_e.push_back(p4_jet[1].E());
    m_jet_sub_e.push_back(p4_jet[0].E());
  }

  for( int i=0; i < njet; i++ ) {
    
    m_jet_m.push_back(p4_jet[i].M());
    m_jet_p.push_back(p4_jet[i].P());
    m_jet_pt.push_back(p4_jet[i].Pt());
    m_jet_px.push_back(p4_jet[i].Px());
    m_jet_py.push_back(p4_jet[i].Py());
    m_jet_pz.push_back(p4_jet[i].Pz());
    m_jet_e.push_back(p4_jet[i].E());

    m_jet_phi.push_back(p4_jet[i].Phi()     *180.0/M_PI );
    m_jet_theta.push_back(p4_jet[i].Theta() *180.0/M_PI );

    for( int j=i+1; j < njet; j++) {

      double mjj     = ( p4_jet[i] + p4_jet[j] ).M();
      double pjj     = ( p4_jet[i] + p4_jet[j] ).P();
      double ptjj    = ( p4_jet[i] + p4_jet[j] ).Pt();
      double pxjj    = ( p4_jet[i] + p4_jet[j] ).Px();
      double pyjj    = ( p4_jet[i] + p4_jet[j] ).Py();
      double pzjj    = ( p4_jet[i] + p4_jet[j] ).Pz();
      double ejj     = ( p4_jet[i] + p4_jet[j] ).E();
      double rec_mjj = ( P4_Ecms - p4_jet[i] - p4_jet[j] ).M();
      double dphi    = fabs(p4_jet[i].DeltaPhi(p4_jet[j])) *180.0/M_PI;
      double dang    = p4_jet[i].Angle(p4_jet[j].Vect())   *180.0/M_PI;

      m_dijet_m.push_back( mjj );
      m_dijet_p.push_back( pjj );
      m_dijet_pt.push_back( ptjj );
      m_dijet_px.push_back( pxjj );
      m_dijet_py.push_back( pyjj );
      m_dijet_pz.push_back( pzjj );
      m_dijet_e.push_back( ejj );
      m_dijet_rec_m.push_back( rec_mjj );
      m_dijet_dphi.push_back( dphi );
      m_dijet_dang.push_back( dang );
    }
  }
      
  if( njet <= 1 ) {  // Can not calculate dijet variables

    m_dijet_m.push_back( -9999.0 );
    m_dijet_p.push_back( -9999.0 );
    m_dijet_pt.push_back( -9999.0 );
    m_dijet_px.push_back( -9999.0 );
    m_dijet_py.push_back( -9999.0 );
    m_dijet_pz.push_back( -9999.0 );
    m_dijet_e.push_back( -9999.0 );
    m_dijet_rec_m.push_back( -9999.0 );
    m_dijet_dphi.push_back( -9999.0 );
    m_dijet_dang.push_back( -9999.0 );

    if( njet == 0 ) {

      m_jet_m.push_back( -9999.0 );
      m_jet_p.push_back( -9999.0 );
      m_jet_pt.push_back( -9999.0 );
      m_jet_px.push_back( -9999.0 );
      m_jet_py.push_back( -9999.0 );
      m_jet_pz.push_back( -9999.0 );
      m_jet_e.push_back( -9999.0 );
      m_jet_phi.push_back( -9999.0 );
      m_jet_theta.push_back( -9999.0 );
    }
  }
    
}


void Higgs2zz::saveVariables() {

  // Variables to be stored -- temporal form !!
  if( m_n_jet == 2 ) {

    m_lljj_m = ( P4_Z_MuonPlus + P4_Z_MuonMinus + P4_Jet[0] + P4_Jet[1] ).M(); 
    m_lljj_cos = ( P4_Z_MuonPlus + P4_Z_MuonMinus + P4_Jet[0] + P4_Jet[1] ).CosTheta(); 

    m_rec_lljj_m = ( P4_Ecms - P4_Z_MuonPlus - P4_Z_MuonMinus - P4_Jet[0] - P4_Jet[1] ).M(); 
    m_rec_lljj_e = ( P4_Ecms - P4_Z_MuonPlus - P4_Z_MuonMinus - P4_Jet[0] - P4_Jet[1] ).E();

    // Angle
    m_lj_angle = (P4_Z_MuonPlus + P4_Z_MuonMinus).Angle((P4_Jet[0] + P4_Jet[1]).Vect()) * 180.0/M_PI;

    double dang1 = P4_Z_MuonPlus.Angle(P4_Jet[0].Vect()) * 180.0/M_PI;
    double dang2 = P4_Z_MuonPlus.Angle(P4_Jet[1].Vect()) * 180.0/M_PI;
    double dang3 = P4_Z_MuonMinus.Angle(P4_Jet[0].Vect()) * 180.0/M_PI;
    double dang4 = P4_Z_MuonMinus.Angle(P4_Jet[1].Vect()) * 180.0/M_PI;

    double min_angle = 360.0;
    if( fabs(dang1) < min_angle ) min_angle = fabs(dang1);
    if( fabs(dang2) < min_angle ) min_angle = fabs(dang2);
    if( fabs(dang3) < min_angle ) min_angle = fabs(dang3);
    if( fabs(dang4) < min_angle ) min_angle = fabs(dang4);
    m_lj_minangle = min_angle;
  }
  else { // To gather samples, such as,  ZH->mumu, nunu, nunu, which can not make 2 jets.

    m_rec_lljj_m = -9999.0;
    m_rec_lljj_e = -9999.0;
    m_lj_minangle = -9999.0;
  }

  m_vis_ex_dimuon_m = ( P4_Charged_Sum + P4_Neutral_Sum - P4_Z_MuonPlus - P4_Z_MuonMinus ).M();
  m_vis_ex_dimuon_e = ( P4_Charged_Sum + P4_Neutral_Sum - P4_Z_MuonPlus - P4_Z_MuonMinus ).E();

  m_vis_all_m = ( P4_Charged_Sum + P4_Neutral_Sum ).M();
  m_vis_all_e = ( P4_Charged_Sum + P4_Neutral_Sum ).E();
  m_vis_all_p = ( P4_Charged_Sum + P4_Neutral_Sum ).P();
  m_vis_all_pt = ( P4_Charged_Sum + P4_Neutral_Sum ).Pt();
  m_vis_all_px = ( P4_Charged_Sum + P4_Neutral_Sum ).Px();
  m_vis_all_py = ( P4_Charged_Sum + P4_Neutral_Sum ).Py();
  m_vis_all_pz = ( P4_Charged_Sum + P4_Neutral_Sum ).Pz();
  m_vis_all_cos = ( P4_Charged_Sum + P4_Neutral_Sum ).CosTheta();
  m_cos =  m_vis_all_pz/sqrt(m_vis_all_pz*m_vis_all_pz + m_vis_all_py*m_vis_all_py);

  m_vis_all_rec_m = ( P4_Ecms - P4_Charged_Sum - P4_Neutral_Sum ).M();
  m_vis_all_rec_e = ( P4_Ecms - P4_Charged_Sum - P4_Neutral_Sum ).E();
  m_vis_all_rec_px = ( P4_Ecms - P4_Charged_Sum - P4_Neutral_Sum ).Px();
  m_vis_all_rec_py = ( P4_Ecms - P4_Charged_Sum - P4_Neutral_Sum ).Py();
  m_vis_all_rec_pz = ( P4_Ecms - P4_Charged_Sum - P4_Neutral_Sum ).Pz();
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

void Higgs2zz::checkGenMCInfo( LCCollection* col_MC ) {

  int ncol = col_MC->getNumberOfElements();
  
  for( int i = 0; i < ncol; i++) {

    MCParticle *mcp = dynamic_cast<EVENT::MCParticle *>(col_MC->getElementAt(i));

    std::vector<MCParticle*> pvec;
    pvec = mcp->getParents();

    int pdgid       =  mcp->getPDG();
    int nparents    =  pvec.size();

    int mother_pid=-9999;
    if( nparents > 0 )mother_pid=pvec[0]->getPDG();

    // Save Initial Partons PID
    if( nparents == 0 )h_mc_init_plist->Fill( pdgid );  

    // Save Higgs Daughter PID
    if( nparents == 1 && mother_pid == HIGGS_PID )h_mc_higgs_dlist->Fill( pdgid );
  }
}
      

void Higgs2zz::saveMCTruthInfo( LCCollection* col_MC ) {

  int ncol = col_MC->getNumberOfElements();
  
  int Zcount=0;
  int Wcount=0;
  int decay_flag = 0;
  for( int i = 0; i < ncol; i++) {

    MCParticle *mcp = dynamic_cast<EVENT::MCParticle *>(col_MC->getElementAt(i));

    std::vector<MCParticle*> pvec, dvec;
    pvec = mcp->getParents();
    dvec = mcp->getDaughters();

    int status      =  mcp->getGeneratorStatus(); 
    int pdgid       =  mcp->getPDG();
    //int mass        =  mcp->getMass();
    int nparents    =  pvec.size();
    //int ndaughters  =  dvec.size();

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
      
      if( pdgid == MUON_PID || pdgid == ELECTRON_PID || pdgid == TAU_PID) {
	m_mc_lepton_minus_id = pdgid;
	P4_MCTruth_LeptonMinus.push_back( p4vec );
      }
      if( pdgid == -MUON_PID|| pdgid == -ELECTRON_PID|| pdgid == -TAU_PID){
	m_mc_lepton_plus_id = pdgid;
	P4_MCTruth_LeptonPlus.push_back( p4vec );
      }

      if( pdgid == MUON_NEUTRINO_PID || pdgid == ELECTRON_NEUTRINO_PID || pdgid == TAU_NEUTRINO_PID) {
        m_mc_neutrino_minus_id = pdgid;
      }
      if( pdgid == -MUON_NEUTRINO_PID|| pdgid == -ELECTRON_NEUTRINO_PID|| pdgid == -TAU_NEUTRINO_PID){
        m_mc_neutrino_plus_id = pdgid;
      }

      if( pdgid == 1 || pdgid == 2 || pdgid == 3 || pdgid == 4 || pdgid == 5 || pdgid == 6) {
        m_mc_quark_minus_id = pdgid;
      }
      if( pdgid == -1 || pdgid == -2 || pdgid == -3 || pdgid == -4 || pdgid == -5 || pdgid == -6){
        m_mc_quark_plus_id = pdgid;
      }

      if( pdgid == PHOTON_PID )P4_MCTruth_photon.push_back( p4vec );
      if( pdgid == HIGGS_PID )P4_MCTruth_Higgs.push_back( p4vec );
	
      m_mc_init_pdgid.push_back( pdgid );
    }

    // Search Higgs daughters
    if( nparents == 1 && mother_pid == HIGGS_PID ) { // mother is Higgs

      m_mc_higgs_daughter_pdgid.push_back( pdgid );

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
	    m_mc_z1_daughter_pid.push_back( d_pid );
	    P4_MCTruth_Z1.push_back( p4vec );	    
	  }
	  else if( Zcount == 1 ) {
	    m_mc_z2_daughter_pid.push_back( d_pid );
	    P4_MCTruth_Z2.push_back( p4vec );
	  }
	}
	
	decay_flag = 1;
	Zcount++;
      }

      if( abs(pdgid) == W_PID ) {  // W boson
	
	for( int j = 0; j < 2; j++ )  { // fill daughter's info
	  
	  int d_pid  = dvec[j]->getPDG();
	  
	  double px = dvec[j]->getMomentum()[0];
	  double py = dvec[j]->getMomentum()[1];
	  double pz = dvec[j]->getMomentum()[2];
	  double e = dvec[j]->getEnergy();
      
	  TLorentzVector p4vec(px, py, pz, e);

	  if( Wcount == 0 ) {
	    m_mc_w1_daughter_pid.push_back( d_pid );
	    P4_MCTruth_W1.push_back( p4vec );	    
	  }
	  else if( Wcount == 1 ) {
	    m_mc_w2_daughter_pid.push_back( d_pid );
	    P4_MCTruth_W2.push_back( p4vec );
	  }
	}
	
	decay_flag = 2;
	Wcount++;
      }    
      
      if( abs(pdgid) >= 1  && abs(pdgid) <= 6  ) decay_flag = 3;
      if( abs(pdgid) >= 11 && abs(pdgid) <= 16 ) decay_flag = 4;
      if( pdgid == 21 ) decay_flag = 5;
      if( pdgid == 22 ) decay_flag = 6;
	
    }

    if(status==1 || status==2)m_mc_pdgid.push_back(pdgid);
  }

  m_mc_n_Zboson = Zcount;
  m_mc_higgs_decay_type = decay_flag;

  fillMCInfo();

}

void Higgs2zz::fillMCInfo() {

  int n_init_lepton_p = P4_MCTruth_LeptonPlus.size();
  int n_init_lepton_m = P4_MCTruth_LeptonMinus.size();
  
  // Initial two leptons
  m_mc_init_n_lepton_plus  = n_init_lepton_p;
  m_mc_init_n_lepton_minus = n_init_lepton_m;

  if( n_init_lepton_p > 0 && n_init_lepton_m > 0 ) {

    m_mc_init_leptonp_e  = P4_MCTruth_LeptonPlus[0].E();
    m_mc_init_leptonp_p  = P4_MCTruth_LeptonPlus[0].P();
    m_mc_init_leptonp_pt = P4_MCTruth_LeptonPlus[0].Pt();
    m_mc_init_leptonp_px = P4_MCTruth_LeptonPlus[0].Px();
    m_mc_init_leptonp_py = P4_MCTruth_LeptonPlus[0].Py();
    m_mc_init_leptonp_pz = P4_MCTruth_LeptonPlus[0].Pz();

    m_mc_init_leptonp_phi = P4_MCTruth_LeptonPlus[0].Phi()      *180.0/M_PI;
    m_mc_init_leptonp_theta = P4_MCTruth_LeptonPlus[0].Theta()  *180.0/M_PI;
  
    m_mc_init_leptonm_e  = P4_MCTruth_LeptonMinus[0].E();
    m_mc_init_leptonm_p  = P4_MCTruth_LeptonMinus[0].P();
    m_mc_init_leptonm_pt = P4_MCTruth_LeptonMinus[0].Pt();
    m_mc_init_leptonm_px = P4_MCTruth_LeptonMinus[0].Px();
    m_mc_init_leptonm_py = P4_MCTruth_LeptonMinus[0].Py();
    m_mc_init_leptonm_pz = P4_MCTruth_LeptonMinus[0].Pz();

    m_mc_init_leptonm_phi = P4_MCTruth_LeptonMinus[0].Phi()     *180.0/M_PI;
    m_mc_init_leptonm_theta = P4_MCTruth_LeptonMinus[0].Theta() *180.0/M_PI;
  
    double mll     = ( P4_MCTruth_LeptonPlus[0] + P4_MCTruth_LeptonMinus[0] ).M();
    double ell     = ( P4_MCTruth_LeptonPlus[0] + P4_MCTruth_LeptonMinus[0] ).E();
    double pll     = ( P4_MCTruth_LeptonPlus[0] + P4_MCTruth_LeptonMinus[0] ).P();
    double ptll    = ( P4_MCTruth_LeptonPlus[0] + P4_MCTruth_LeptonMinus[0] ).Pt();
    double pzll    = ( P4_MCTruth_LeptonPlus[0] + P4_MCTruth_LeptonMinus[0] ).Pz();
    double rec_mll = ( P4_Ecms - P4_MCTruth_LeptonPlus[0] - P4_MCTruth_LeptonMinus[0] ).M();
    double dphi    = fabs(P4_MCTruth_LeptonPlus[0].DeltaPhi(P4_MCTruth_LeptonMinus[0])) *180.0/M_PI;
    double dang    = P4_MCTruth_LeptonPlus[0].Angle(P4_MCTruth_LeptonMinus[0].Vect())   *180.0/M_PI;
  
    m_mc_init_dilepton_m = mll;
    m_mc_init_dilepton_e = ell;
    m_mc_init_dilepton_p = pll;
    m_mc_init_dilepton_pt = ptll;
    m_mc_init_dilepton_pz = pzll;
    m_mc_init_dilepton_rec_m = rec_mll;
    m_mc_init_dilepton_dphi = dphi;
    m_mc_init_dilepton_dang = dang;
  }
  else {
    
    m_mc_init_leptonp_e  = -9999.0;
    m_mc_init_leptonp_p  = -9999.0;
    m_mc_init_leptonp_pt = -9999.0;
    m_mc_init_leptonp_px = -9999.0;
    m_mc_init_leptonp_py = -9999.0;
    m_mc_init_leptonp_pz = -9999.0;

    m_mc_init_leptonp_phi = -9999.0;
    m_mc_init_leptonp_theta = -9999.0;
  
    m_mc_init_leptonm_e  = -9999.0;
    m_mc_init_leptonm_p  = -9999.0;
    m_mc_init_leptonm_pt = -9999.0;
    m_mc_init_leptonm_px = -9999.0;
    m_mc_init_leptonm_py = -9999.0;
    m_mc_init_leptonm_pz = -9999.0;

    m_mc_init_leptonm_phi = -9999.0;
    m_mc_init_leptonm_theta = -9999.0;
  
    m_mc_init_dilepton_m = -9999.0;
    m_mc_init_dilepton_e = -9999.0;
    m_mc_init_dilepton_p = -9999.0;
    m_mc_init_dilepton_pt = -9999.0;
    m_mc_init_dilepton_pz = -9999.0;
    m_mc_init_dilepton_rec_m = -9999.0;
    m_mc_init_dilepton_dphi = -9999.0;
    m_mc_init_dilepton_dang = -9999.0;
  }
    
  // Initial photons
  int n_init_photon = P4_MCTruth_photon.size();
  
  m_mc_init_n_photon  = n_init_photon;

  for( int i=0; i<n_init_photon; i++) {

    m_mc_init_photon_e.push_back( P4_MCTruth_photon[i].E() );
    m_mc_init_photon_p.push_back( P4_MCTruth_photon[i].P() );
    m_mc_init_photon_pt.push_back( P4_MCTruth_photon[i].Pt() );
    m_mc_init_photon_pz.push_back( P4_MCTruth_photon[i].Pz() );

    m_mc_init_photon_phi.push_back( P4_MCTruth_photon[i].Phi()*180.0/M_PI );
    m_mc_init_photon_theta.push_back( P4_MCTruth_photon[i].Theta()*180.0/M_PI );
  }

  if( n_init_photon == 0 ) {

    m_mc_init_photon_e.push_back( -99.0 );
    m_mc_init_photon_p.push_back( -99.0 );
    m_mc_init_photon_pt.push_back( -99.0 );
    m_mc_init_photon_pz.push_back( -999.0 );

    m_mc_init_photon_phi.push_back( -99.0 );
    m_mc_init_photon_theta.push_back( -99.0 );
  }


  // Initial Higgs
  int n_higgs = P4_MCTruth_Higgs.size();
  if( n_higgs == 1 ) {

    m_mc_higgs_m = P4_MCTruth_Higgs[0].M();
    m_mc_higgs_e = P4_MCTruth_Higgs[0].E();
    m_mc_higgs_rec_m = ( P4_Ecms - P4_MCTruth_Higgs[0] ).M();
  }
  else {

    m_mc_higgs_m = -9999.0;
    m_mc_higgs_e = -9999.0;
    m_mc_higgs_rec_m = -9999.0;
  }


  // H->ZZ* or H->WW* channels   
  int n_z1_daughters = P4_MCTruth_Z1.size();
  int n_z2_daughters = P4_MCTruth_Z2.size();
  int n_w1_daughters = P4_MCTruth_W1.size();
  int n_w2_daughters = P4_MCTruth_W2.size();

  int h2zz_flag=0;
  int h2ww_flag=0;
  m_mc_zz_flag = -1;
  m_mc_ww_flag = -1;

  TLorentzVector p4_zw1_daughter_1, p4_zw1_daughter_2;
  TLorentzVector p4_zw2_daughter_1, p4_zw2_daughter_2;

  // Higgs -> ZZ
  if( n_higgs == 1 && n_z1_daughters == 2 && n_z2_daughters == 2 ) {

    h2zz_flag = 1;

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

    // Strange Combination
    if( (m_mc_z2_daughter_pid[0] + m_mc_z2_daughter_pid[1]) != 0 ) { flag2 = 4; }

    m_mc_zz_flag = flag2*10 + flag1;
  
    // Replace Neutrino component to "invisible"
    TLorentzVector p4_null(0,0,0,0);

    p4_zw1_daughter_1 = P4_MCTruth_Z1[0];
    p4_zw1_daughter_2 = P4_MCTruth_Z1[1];
    p4_zw2_daughter_1 = P4_MCTruth_Z2[0];
    p4_zw2_daughter_2 = P4_MCTruth_Z2[1];

    if( flag1 == 2 ) { // neutrino
    
      p4_zw1_daughter_1 = p4_null;
      p4_zw1_daughter_2 = p4_null;
    }
    if( flag2 == 2 ) { // neutrino
    
      p4_zw2_daughter_1 = p4_null;
      p4_zw2_daughter_2 = p4_null;
    }
  }

  // Higgs -> WW
  if( n_higgs == 1 && n_w1_daughters == 2 && n_w2_daughters == 2  ) {     

    h2ww_flag = 1;

    int flag1=0;
    int flag2=0;
    //*******  W1 decay combination   *******//
    // W1->qq
    if( abs(m_mc_w1_daughter_pid[0]) >= 1 && abs(m_mc_w1_daughter_pid[0]) <= 6 ) { flag1 = 1; }

    // W1->nu+l
    if( abs(m_mc_w1_daughter_pid[0]) == ELECTRON_NEUTRINO_PID  || 
        abs(m_mc_w1_daughter_pid[0]) == MUON_NEUTRINO_PID      ||
	abs(m_mc_w1_daughter_pid[0]) == TAU_NEUTRINO_PID            ) { flag1 = 2; }

    // W1->l+nu
    if( abs(m_mc_w1_daughter_pid[1]) == ELECTRON_NEUTRINO_PID  || 
        abs(m_mc_w1_daughter_pid[1]) == MUON_NEUTRINO_PID      ||
	abs(m_mc_w1_daughter_pid[1]) == TAU_NEUTRINO_PID            ) { flag1 = 3; }

  
    //*******  W2 decay combination   *******//
    // W2->qq
    if( abs(m_mc_w2_daughter_pid[0]) >= 1 && abs(m_mc_w2_daughter_pid[0]) <= 6 ) { flag2 = 1; }

    // W2->nu+l
    if( abs(m_mc_w2_daughter_pid[0]) == ELECTRON_NEUTRINO_PID  || 
        abs(m_mc_w2_daughter_pid[0]) == MUON_NEUTRINO_PID      ||
	abs(m_mc_w2_daughter_pid[0]) == TAU_NEUTRINO_PID            ) { flag2 = 2; }

    // W2->l+nu
    if( abs(m_mc_w2_daughter_pid[1]) == ELECTRON_NEUTRINO_PID  || 
        abs(m_mc_w2_daughter_pid[1]) == MUON_NEUTRINO_PID      ||
	abs(m_mc_w2_daughter_pid[1]) == TAU_NEUTRINO_PID            ) { flag2 = 3; }


    m_mc_ww_flag = flag2*10 + flag1;

    // Replace Neutrino component to "invisible"
    TLorentzVector p4_null(0,0,0,0);
    p4_zw1_daughter_1 = P4_MCTruth_W1[0];
    p4_zw1_daughter_2 = P4_MCTruth_W1[1];
    p4_zw2_daughter_1 = P4_MCTruth_W2[0];
    p4_zw2_daughter_2 = P4_MCTruth_W2[1];

    if( flag1 == 2 ) p4_zw1_daughter_1 = p4_null; // neutrino
    if( flag1 == 3 ) p4_zw1_daughter_2 = p4_null; // neutrino

    if( flag2 == 2 ) p4_zw2_daughter_1 = p4_null; // neutrino
    if( flag2 == 3 ) p4_zw2_daughter_2 = p4_null; // neutrino
  }


  // Save Variables ( H->ZZ*/WW* )
  if( h2zz_flag == 0 && h2ww_flag == 0 ) m_mc_h2gaugeboson_flag = 0;
  if( h2zz_flag == 1 && h2ww_flag == 0 ) m_mc_h2gaugeboson_flag = 1;
  if( h2zz_flag == 0 && h2ww_flag == 1 ) m_mc_h2gaugeboson_flag = 2;
  if( h2zz_flag == 1 && h2ww_flag == 1 ) m_mc_h2gaugeboson_flag = 3;


  if( h2zz_flag == 1 || h2ww_flag == 1 ) {

    double zw1_m  = ( p4_zw1_daughter_1 + p4_zw1_daughter_2 ).M();
    double zw1_p  = ( p4_zw1_daughter_1 + p4_zw1_daughter_2 ).P();
    double zw1_pt = ( p4_zw1_daughter_1 + p4_zw1_daughter_2 ).Pt();
    double zw1_e  = ( p4_zw1_daughter_1 + p4_zw1_daughter_2 ).E();
    double zw1_rec_m  = ( P4_Ecms - p4_zw1_daughter_1 - p4_zw1_daughter_2 ).M();

    double zw2_m  = ( p4_zw2_daughter_1 + p4_zw2_daughter_2 ).M();
    double zw2_p  = ( p4_zw2_daughter_1 + p4_zw2_daughter_2 ).P();
    double zw2_pt = ( p4_zw2_daughter_1 + p4_zw2_daughter_2 ).Pt();
    double zw2_e  = ( p4_zw2_daughter_1 + p4_zw2_daughter_2 ).E();
    double zw2_rec_m  = ( P4_Ecms - p4_zw2_daughter_1 - p4_zw2_daughter_2 ).M();

    double zw1zw2_m = ( p4_zw1_daughter_1 + p4_zw1_daughter_2 + p4_zw2_daughter_1 + p4_zw2_daughter_2 ).M();
    double zw1zw2_e = ( p4_zw1_daughter_1 + p4_zw1_daughter_2 + p4_zw2_daughter_1 + p4_zw2_daughter_2 ).E();
    double zw1zw2_rec_m = ( P4_Ecms - p4_zw1_daughter_1 - p4_zw1_daughter_2 - p4_zw2_daughter_1 - p4_zw2_daughter_2 ).M();

    m_mc_zw1_m  = zw1_m;
    m_mc_zw1_p  = zw1_p;
    m_mc_zw1_pt = zw1_pt;
    m_mc_zw1_e  = zw1_e;
    m_mc_zw1_rec_m = zw1_rec_m;

    m_mc_zw2_m  = zw2_m;
    m_mc_zw2_p  = zw2_p;
    m_mc_zw2_pt = zw2_pt;
    m_mc_zw2_e  = zw2_e;
    m_mc_zw2_rec_m = zw2_rec_m;

    m_mc_zw1zw2_m = zw1zw2_m;
    m_mc_zw1zw2_e = zw1zw2_e;
    m_mc_zw1zw2_rec_m = zw1zw2_rec_m;
  }
  else {

    m_mc_zw1_m  = -9999.0;
    m_mc_zw1_p  = -9999.0;
    m_mc_zw1_pt = -9999.0;
    m_mc_zw1_e  = -9999.0;
    m_mc_zw1_rec_m = -9999.0;

    m_mc_zw2_m  = -9999.0;
    m_mc_zw2_p  = -9999.0;
    m_mc_zw2_pt = -9999.0;
    m_mc_zw2_e  = -9999.0;
    m_mc_zw2_rec_m = -9999.0;

    m_mc_zw1zw2_m = -9999.0;
    m_mc_zw1zw2_e = -9999.0;
    m_mc_zw1zw2_rec_m = -9999.0;
  }

}

