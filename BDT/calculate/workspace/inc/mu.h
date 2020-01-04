#include "TStopwatch.h"
#include "RooGlobalFunc.h"
#include "RooRealVar.h"
#include "RooProdPdf.h"
#include "RooWorkspace.h"
#include "RooDataSet.h"
#include "TCanvas.h"
#include "TStopwatch.h"
#include "TH1.h"
#include "RooPlot.h"
#include "RooMsgService.h"

#include "RooStats/NumberCountingUtils.h"

#include "RooStats/HybridCalculator.h"
#include "RooStats/ToyMCSampler.h"
#include "RooStats/HypoTestPlot.h"

#include "RooStats/ProfileLikelihoodTestStat.h"
#include "RooStats/SimpleLikelihoodRatioTestStat.h"
#include "RooStats/RatioOfProfiledLikelihoodsTestStat.h"
#include "RooStats/MaxLikelihoodEstimateTestStat.h"

#include "TMath.h"
#include "TRandom3.h"
#include "TFile.h"
#include "TTree.h"
#include "TChain.h"
#include "TCanvas.h"
#include "RooPlot.h"
#include "TROOT.h"
#include "THStack.h"
#include "TString.h"
#include "TH1.h"
#include "TRandom.h"
#include "RooRealVar.h"
#include "RooExponential.h"
#include "RooPlot.h"
#include "RooGaussian.h"
#include "RooPolynomial.h"
#include "RooAddPdf.h"
#include "RooAbsData.h"
#include "RooAbsRealLValue.h"
#include "RooAbsPdf.h"
#include "RooMinuit.h"
#include "RooCategory.h"
#include "RooDataSet.h"
#include "RooArgSet.h"
#include "RooDataHist.h"
#include "RooNLLVar.h"
#include "RooSimultaneous.h"
#include "RooExponential.h"
#include "RooGlobalFunc.h"
#include "RooCBShape.h"
#include "RooFormula.h"
#include "RooRandom.h"
#include "RooFitResult.h"
#include "RooProdPdf.h"
#include "RooProfileLL.h"
#include "RooLognormal.h"
#include "RooPoisson.h"
#include "RooProduct.h"
#include "RooAddition.h"
#include "RooBifurGauss.h"
#include "TLatex.h"
#include "TLine.h"
#include <stdlib.h>
#include <stdio.h>
#include <iostream>

using namespace std;
using namespace RooFit;
using namespace RooStats;

#include <sys/stat.h>

map<string,double> fitmu( RooWorkspace* w , RooArgSet *&nuispara, TString m_opt)
{

  RooSimultaneous* combPdf =  (RooSimultaneous*)w->pdf("CombinedPdf") ;
  RooArgSet* nuisanceParameters = (RooArgSet*)w->set("nuisanceParameters");
  RooArgSet* globalObservables = (RooArgSet*)w->set("globalObservables");

  TIterator *iter_nui_release = nuisanceParameters -> createIterator();
  RooRealVar* parg_nui_release = NULL;
  while((parg_nui_release=(RooRealVar*)iter_nui_release->Next()) )
  {
    if(m_opt.Contains("noSys")) parg_nui_release->setConstant(kTRUE);
    else parg_nui_release->setConstant(kFALSE);
  }

  TIterator *iter_global = globalObservables -> createIterator();
  RooRealVar* parg_global = NULL;
  while((parg_global=(RooRealVar*)iter_global->Next()) )
  { parg_global->setConstant(); }

  RooArgSet variable_minos ;

  if(m_opt.Contains("fitbr")) {
    cout<<"fit mu of each production mode"<<endl;
    (*w->var("mu")).setVal(1);
    (*w->var("mu")).setConstant(true) ;
    (*w->var("mu_JJ")).setVal(1);
    (*w->var("mu_JJ")).setConstant(true) ; // get br of bb, cc and gg
//   variable_minos.add(*w->var("mu_JJ")) ;
/*
    (*w->var("mu_WW")).setVal(1);
    (*w->var("mu_WW")).setConstant(false) ;
    variable_minos.add(*w->var("mu_WW")) ;
    (*w->var("mu_TauTau")).setVal(1);
    (*w->var("mu_TauTau")).setConstant(false) ;
    variable_minos.add(*w->var("mu_TauTau")) ;
    (*w->var("mu_GammaGamma")).setVal(1);
    (*w->var("mu_GammaGamma")).setConstant(false) ;
    variable_minos.add(*w->var("mu_GammaGamma")) ;
*/
(*w->var("mu_tt")).setVal(1);
(*w->var("mu_tt")).setConstant(false);
(*w->var("mu_ww")).setVal(1);
(*w->var("mu_ww")).setConstant(false);
(*w->var("mu_invi")).setVal(1);
(*w->var("mu_invi")).setConstant(false);
(*w->var("mu_mumu")).setVal(1);
(*w->var("mu_mumu")).setConstant(false);

    (*w->var("mu_bb")).setVal(1);
    (*w->var("mu_bb")).setConstant(false) ;
    variable_minos.add(*w->var("mu_bb")) ;
    (*w->var("mu_cc")).setVal(1);
    (*w->var("mu_cc")).setConstant(false) ;
    variable_minos.add(*w->var("mu_cc")) ;
    (*w->var("mu_gg")).setVal(1);
    (*w->var("mu_gg")).setConstant(false) ;
    variable_minos.add(*w->var("mu_gg")) ;
    (*w->var("mu_zz")).setVal(1);
    (*w->var("mu_zz")).setConstant(false) ;
    variable_minos.add(*w->var("mu_zz")) ;
    (*w->var("mu_aa")).setVal(1);
    (*w->var("mu_aa")).setConstant(false) ;
    variable_minos.add(*w->var("mu_aa")) ;
  }
  else {
    cout<<"fit global mu"<<endl;
    (*w->var("mu")).setVal(1);
    (*w->var("mu")).setConstant(kFALSE);
    variable_minos.add(*w->var("mu")) ;
    (*w->var("mu_JJ")).setVal(1);
    (*w->var("mu_JJ")).setConstant(true) ;
/*
    (*w->var("mu_WW")).setVal(1);
    (*w->var("mu_WW")).setConstant(true) ;
    (*w->var("mu_TauTau")).setVal(1);
    (*w->var("mu_TauTau")).setConstant(true) ;
    (*w->var("mu_GammaGamma")).setVal(1);
    (*w->var("mu_GammaGamma")).setConstant(true) ;
*/

(*w->var("mu_tt")).setVal(1);
(*w->var("mu_tt")).setConstant(true);
(*w->var("mu_ww")).setVal(1);
(*w->var("mu_ww")).setConstant(true);
(*w->var("mu_invi")).setVal(1);
(*w->var("mu_invi")).setConstant(true);
(*w->var("mu_mumu")).setVal(1);
(*w->var("mu_mumu")).setConstant(true);

    (*w->var("mu_bb")).setVal(1);
    (*w->var("mu_bb")).setConstant(true) ;
    (*w->var("mu_cc")).setVal(1);
    (*w->var("mu_cc")).setConstant(true) ;
    (*w->var("mu_gg")).setVal(1);
    (*w->var("mu_gg")).setConstant(true) ;
    (*w->var("mu_zz")).setVal(1);
    (*w->var("mu_zz")).setConstant(true) ;
    (*w->var("mu_aa")).setVal(1);
    (*w->var("mu_aa")).setConstant(true) ;
  }


 RooFitResult *result_mu = combPdf->fitTo((*w->data("AsimovSB")),Constrain(*w->set("nuisanceParameters")),Minos(variable_minos),Save(), Minimizer("Minuit","migrad"),Strategy(2),PrintLevel(0));
//  RooFitResult *result_mu = combPdf->fitTo((*w->data("obsData")),Constrain(*w->set("nuisanceParameters")),Minos(variable_minos),Save(), Minimizer("Minuit","migrad"),Strategy(2),PrintLevel(0));

  double fitted_mu = (*w->var("mu")).getVal();
  double error_mu =  (*w->var("mu")).getError();
  double error_mu_low = w->var("mu")->getErrorLo();
  double error_mu_high = w->var("mu")->getErrorHi();

  delete w;
  delete result_mu ;

  map<string,double> result ;

  result["fitted_mu"] = fitted_mu ;
  result["error_mu"] = error_mu ;
  result["error_mu_low"] = error_mu_low ;
  result["error_mu_high"] = error_mu_high ;

  return result ;
}
