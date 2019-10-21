#include "src/RooGaussDoubleSidedExp.h"
#include "src/RooGaussDoubleSidedExp.cxx"
#include "src/CEPCCDRstyle.cxx"
RooFitResult* Minimize(RooAbsPdf *&pdf, RooDataSet &data)
{
  RooAbsReal *nll = pdf->createNLL(data);
//   RooAbsReal *nll = pdf->createNLL(data);
  RooMinimizer minim(*nll);
  minim.setStrategy( 2 );
  minim.setPrintLevel( -1 );    // now -1 is the best choice;
//   minim.setProfile(); /* print out time */
  minim.setEps( 1e-01 ); //large……
  minim.setOffsetting( true );
  minim.optimizeConst( 2 );

  int status = 0;
  status += minim.minimize( "Minuit2" );
  cout<<"minimize Finished"<<endl;
  cout<<"status:"<<status<<endl;
  RooFitResult* result = minim.save();
  return result;
}
void GaussExp()
{
    SetCEPCCDRStyle();
gROOT->ProcessLine(".L /afs/ihep.ac.cn/users/z/zhangkl/wfs/workspace/lib/libRooGaussExp.so"); 
TFile f1("out/workspace/part/ws_qqqq_5.root");
RooWorkspace *w=(RooWorkspace*)f1.Get("wspace");
RooDataSet* d=(RooDataSet*)w->data("d_mass_bb");
RooRealVar* inv=(RooRealVar*)w->var("invMass");
RooRealVar mH    ("signal_mean",  "mean of Higgs", 125, 125 - 5, 125 + 5);
RooRealVar sigma ("mRes",  "Resolution", 1, 0.1, 10);
RooRealVar Tn    ("tailN", "tail N of Higgs", 5., 0.1, 20);
RooRealVar Tn2    ("tailN2", "tail N of Higgs2", 5., 0.1, 20);
RooGaussDoubleSidedExp::RooGaussDoubleSidedExp *pdf=new RooGaussDoubleSidedExp("pdf", "pdf", *inv, mH, sigma, Tn, Tn2);
// RooFitResult* result=Minimize(&pdf, *d)；
pdf->fitTo(*d);
// result->Print("v");
TCanvas *canvas = new TCanvas("c1", "c1", 800, 800);
RooPlot *frame=inv->frame(50);
d->plotOn(frame);
pdf->plotOn(frame); 
frame->Draw();
canvas->SaveAs("temp.png");
w->import(*pdf);
w->importClassCode("*");
w->importClassCode("RooGaussDoubleSidedExp");
w->importClassCode(RooGaussDoubleSidedExp::Class());

w->Print("v");
w->writeToFile("temp.root");
}
