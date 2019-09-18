#include "frame.h"

using namespace std;
using namespace CommonFunc;
using namespace RooStats;

double median(double NLL, double minNLL)
{

  double delta_NLL = 2*fabs( NLL-minNLL ) ;
  double pvalue =  ROOT::Math::chisquared_cdf(delta_NLL,2);

  return pvalue;
}

int main(int argc, char **argv){

    TString CHANNEL=argv[1];
    TString pois;

    vector<TString> plist;

    if(argc>2) pois=argv[2];
    if (pois != "") {
      vector<TString> poilist = SplitString( pois, ',' );
      for (UInt_t i=0; i<poilist.size(); i++) {
        vector<TString> rangelist = SplitString( poilist[i], '=' );
        for (UInt_t j=0; j<rangelist.size(); j++) plist.push_back(rangelist[j]); 
        if(rangelist.size()==2)  {
          cout << "NLL scan of " << rangelist[0] << " with " <<rangelist[1]<<" bins."<< endl;
        }
        else cout<<"ERROR: wrong format of poi list"<<endl;
      }
    }

    TString name_poi1 = plist[0];
    int nBin1 = atoi(plist[1]);
    TString name_poi2 = plist[2];
    int nBin2 = atoi(plist[3]);

    SetAtlasStyle();
    double luminosity=36.1;

    TString inputMinFile="outs/singleFit/singleFit_"+CHANNEL+".root";

    TFile *f=new TFile(inputMinFile,"read");
    assert(f);
    TTree *t=(TTree*)f->Get("nllscan");

    double v_poi1,v_poi2,minNLL;

    t->SetBranchAddress(name_poi1,&v_poi1);
    t->SetBranchAddress(name_poi2,&v_poi2);
    t->SetBranchAddress("nll",&minNLL);

    t->GetEntry(0);
    cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;
    cout<<name_poi1<<" = "<<v_poi1<<endl;
    cout<<name_poi2<<" = "<<v_poi2<<endl;
    cout<<"minNLL = "<<minNLL<<endl;
    cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;

    TCanvas* c = CreateCanvas("c","Contour List",1024,768);

    // Load Histogram Data
    vector<int> points1, points2;
    double arr_poi1[1000], arr_poi2[1000];
    double arr_nll[1000][1000];
    int npoi1=0, npoi2=0;
    for (Int_t i = 0; i < nBin1; i++) {
      for(Int_t j = 0; j < nBin2; j++){
      	TString inputFile=Form("outs/nllScan/"+CHANNEL+"/2DScan/"+CHANNEL+"_"+name_poi1+"_%d_"+name_poi2+"_%d.root",i,j);
      	double temp_poi1, temp_poi2, temp_nll;
      	TFile *f=new TFile(inputFile,"read");

        if(gSystem->AccessPathName(inputFile)) {
          std::cout << "File : " << inputFile << " does not exist, and the job should be re-run."<< std::endl;
          points1.push_back(i); points2.push_back(j);
          continue;
        }
      	assert(f);
      	TTree *t=(TTree*)f->Get("nllscan");

      	t->SetBranchAddress(name_poi1,&temp_poi1);
      	t->SetBranchAddress(name_poi2,&temp_poi2);
      	t->SetBranchAddress("nll",&temp_nll);
      	t->GetEntry(0);
      	cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;
      	cout<<name_poi1<<" = "<<temp_poi1<<endl;
      	cout<<name_poi2<<" = "<<temp_poi2<<endl;
      	cout<<"minNLL = "<<temp_nll<<endl;
      	cout<<"+++++++++++++++++++++++++++++++++++++++"<<endl;
      	f->Close();
        arr_poi1[npoi1]=temp_poi1;
        arr_poi2[npoi2]=temp_poi2;
        arr_nll[i][j]=temp_nll;
        npoi1=i+1;
        npoi2=j+1;
      }
    }

    double binw1 = (arr_poi1[npoi1-1]-arr_poi1[0])/(npoi1-1);
    double binw2 = (arr_poi2[npoi2-1]-arr_poi2[0])/(npoi2-1);
    TH2D *HistStreamFn = new TH2D("HstreamFn",  "HstreamFn",
          npoi1, arr_poi1[0]-binw1/2, arr_poi1[npoi1-1]+binw1/2, npoi2, arr_poi2[0]-binw2/2, arr_poi2[npoi2-1]+binw2/2);

    for(int i=0;i<npoi1;i++) {
      for(int j=0;j<npoi2;j++) {
        HistStreamFn->SetBinContent(i+1,j+1, median(arr_nll[i][j],minNLL));
      }
    }

    system("mkdir -vp outs/jobs/2DScan/");
    TString name_output = "outs/jobs/2DScan/"+CHANNEL+"_missingPoints.sh";
    cout<<"Please run missing jobs with "<<name_output<<endl<<endl;;
    fstream fout(name_output,ios::out);
    fout<<"### missing points for 2D scan in "<<CHANNEL<<" with "<<name_poi1<<" and "<<name_poi2<<endl<<endl;
    fout<<"POINTS1=( ";
    for(unsigned int i=0;i<points1.size();i++) fout<<"\""<<points1[i]<<"\" ";
    fout<<")"<<endl;
    fout<<"POINTS2=( ";
    for(unsigned int i=0;i<points2.size();i++) fout<<"\""<<points2[i]<<"\" ";
    fout<<")"<<endl;
    fout.close();

    const int ncontour=2;
    Double_t contours[ncontour];
    contours[0] = 0.68;
    contours[1] = 0.95;

    HistStreamFn->SetContour(ncontour, contours);

    // Draw contours as filled regions, and Save points
    HistStreamFn->Draw("CONTZ,LIST");
    c->Update(); // Needed to force the plotting and retrieve the contours in TGraphs
    // Get Contours
    TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
    TList* contLevel = NULL;
    TGraph* curv     = NULL;
    TGraph* gc[ncontour]       = {NULL};

    Int_t nGraphs    = 0;
    Int_t TotalConts = 0;

    if (conts == NULL){
      printf("*** No Contours Were Extracted!\n");
      TotalConts = 0;
      return -1;
    } else {
      TotalConts = conts->GetSize();
    }

    printf("TotalConts = %d\n", TotalConts);

    for(int i = 0; i < TotalConts; i++){
      contLevel = (TList*)conts->At(i);
      printf("Contour %d has %d Graphs\n", i, contLevel->GetSize());
      nGraphs += contLevel->GetSize();
    }

    nGraphs = 0;

    TCanvas* c1 = new TCanvas("c1","Contour List",600,600);
    c1->SetTopMargin(0.15);
    TH2F *hr = new TH2F("hr","hr", 2, arr_poi1[0]-25*binw1/2, arr_poi1[npoi1-1]+10*binw1/2, 2, arr_poi2[0]-20*binw2/2, arr_poi2[npoi2-1]+70*binw2/2);
    TString title_x = name_poi1, title_y = name_poi2;
    if(name_poi1=="k_V") title_x = "#kappa_{V}";
    if(name_poi2=="k_f") title_y = "#kappa_{f}";
    hr->GetXaxis()->SetTitle(title_x);
    hr->GetYaxis()->SetTitle(title_y);
    hr->GetXaxis()->SetTitleSize(0.07);
    hr->GetXaxis()->SetTitleOffset(0.7);
    hr->GetXaxis()->SetLabelSize(0.03);
    hr->GetXaxis()->SetNdivisions(508);
    hr->GetYaxis()->SetNdivisions(508);
    hr->GetYaxis()->SetTitleSize(0.07);
    hr->GetYaxis()->SetTitleOffset(0.9);
    hr->GetYaxis()->SetLabelSize(0.03);
    hr->Draw();
    Double_t x0, y0, z0;

    for(int i = 0; i < TotalConts; i++){
      contLevel = (TList*)conts->At(i);
      z0 = contours[i];
      printf("Z-Level Passed in as:  Z = %f\n", z0);

      // Get first graph from list on curves on this level
      curv = (TGraph*)contLevel->First();
      for(int j = 0; j < contLevel->GetSize(); j++){
      	curv->GetPoint(0, x0, y0);
      	nGraphs ++;
      	printf("\tGraph: %d  -- %d Elements\n", nGraphs,curv->GetN());

      	// Draw clones of the graphs to avoid deletions in case the 1st
      	// pad is redrawn.
      	gc[i] = (TGraph*)curv->Clone();
      	if(i==0) gc[i]->SetLineColor(ColorWheel(2));
      	else if(i==1) gc[i]->SetLineColor(ColorWheel(1));
      	gc[i]->Draw("L");

      	curv = (TGraph*)contLevel->After(curv); // Get Next graph
      }
    }
//     c1->Update();
    printf("\n\n\tExtracted %d Contours and %d Graphs \n", TotalConts, nGraphs );
    TMarker marker;
    marker.SetMarkerStyle(34);
    marker.SetMarkerSize(1);
    marker.SetMarkerColor(kRed);
    marker.DrawMarker(v_poi1,v_poi2);

    double x1,y1,x2,y2;
    GetX1Y1X2Y2(c1,x1,y1,x2,y2);
    vector<TString> pavetext;
    pavetext.push_back("#bf{#it{CEPC}}");
    pavetext.push_back("#scale[0.6]{#int}Ldt=5 ab^{-1}, #sqrt{s}=250GeV");

    TPaveText* text=CreatePaveText(x1+0.05,y2-0.2,x1+0.35,y2-0.05,pavetext,0.03);
    TLegend* legend=FastLegend(x1+0.45,y2-0.2,x1+0.8,y2-0.05,0.03);
    legend->AddEntry(&marker, "Expected value","P");
    legend->AddEntry(gc[0], "Expected 68% CL","L");
    legend->AddEntry(gc[1], "Expected 95% CL","L");
    c1->cd();
    text->Draw("same");
    legend->Draw("same");
    c1->Update();
    system("mkdir -vp outs/plots/contour/");
    PrintCanvas(c1,"outs/plots/contour/contour_"+name_poi1+"_"+name_poi2+"_"+CHANNEL);
}

