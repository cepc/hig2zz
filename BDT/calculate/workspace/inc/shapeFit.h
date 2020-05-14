#ifndef SHAPE_H
#define SHAPE_H
bool is250=false;
bool isuseexistingpdf=false;
const int Nch = 6;
const TString m_CN[Nch] = {"mzvj","mzjv","vzmj","vzjm","qzvm","qzmv"};

typedef struct
{
    TString name;
    int nsig=1;
    int nbkg=1;
    Float_t mlow=110;
    Float_t mhigh=150;
    TString f_bkg;
    TString name_sig[10];
    map<TString, TString> f_sig;    
} channel;

const channel c[150]=
{
 {"mzvj", 4, 1, 110, 140,
  "data/new_zz/mzvj/mzvj_sm.root",
  {"s", "zz", "ww", "tt"},
  {
   {"s",   "data/new_zz/mzvj/mzvj_sig.root"},
   {"zz",  "data/new_zz/mzvj/mzvj_zz.root"},
   {"ww",  "data/new_zz/mzvj/mzvj_ww.root"},
   {"tt",  "data/new_zz/mzvj/mzvj_tt.root"}
  }
 },
 {"mzjv", 8, 1, 110, 140,
  "data/new_zz/mzjv/mzjv_sm.root",
  {"s", "zz", "ww", "tt", "bb", "cc", "gg", "zy"},
  {
   {"s",   "data/new_zz/mzjv/mzjv_sig.root"},
   {"zz",  "data/new_zz/mzjv/mzjv_zz.root"},
   {"ww",  "data/new_zz/mzjv/mzjv_ww.root"},
   {"tt",  "data/new_zz/mzjv/mzjv_tt.root"},
   {"bb",  "data/new_zz/mzjv/mzjv_bb.root"},
   {"cc",  "data/new_zz/mzjv/mzjv_cc.root"},
   {"gg",  "data/new_zz/mzjv/mzjv_gg.root"},
   {"zy",  "data/new_zz/mzjv/mzjv_az.root"}
  }
 },
 {"vzmj", 4, 1, 110, 140,
  "data/new_zz/vzmj/vzmj_sm.root",
  {"s", "zz", "ww", "tt"},
  {
   {"s",   "data/new_zz/vzmj/vzmj_sig.root"},
   {"zz",  "data/new_zz/vzmj/vzmj_zz.root"},
   {"ww",  "data/new_zz/vzmj/vzmj_ww.root"},
   {"tt",  "data/new_zz/vzmj/vzmj_tt.root"},
  }
 },
 {"vzjm", 6, 1, 110, 140,
  "data/new_zz/vzjm/vzjm_sm.root",
  {"s", "zz", "ww", "tt", "bb", "cc"},
  {
   {"s",   "data/new_zz/vzjm/vzjm_sig.root"},
   {"zz",  "data/new_zz/vzjm/vzjm_zz.root"},
   {"ww",  "data/new_zz/vzjm/vzjm_ww.root"},
   {"tt",  "data/new_zz/vzjm/vzjm_tt.root"},
   {"bb",  "data/new_zz/vzjm/vzjm_bb.root"},
   {"cc",  "data/new_zz/vzjm/vzjm_cc.root"},
  }
 },
 {"qzvm", 6, 1, 110, 140,
  "data/new_zz/qzvm/qzvm_sm.root",
  {"s", "zz", "ww", "tt", "bb", "cc"},
  {
   {"s",   "data/new_zz/qzvm/qzvm_sig.root"},
   {"zz",  "data/new_zz/qzvm/qzvm_zz.root"},
   {"ww",  "data/new_zz/qzvm/qzvm_ww.root"},
   {"tt",  "data/new_zz/qzvm/qzvm_tt.root"},
   {"bb",  "data/new_zz/qzvm/qzvm_bb.root"},
   {"cc",  "data/new_zz/qzvm/qzvm_cc.root"},
  }
 },
 {"qzmv", 8, 1, 110, 140,
  "data/new_zz/qzmv/qzmv_sm.root",
  {"s", "zz", "ww", "tt", "bb", "cc", "zy", "mm"},
  {
   {"s",   "data/new_zz/qzmv/qzmv_sig.root"},
   {"zz",  "data/new_zz/qzmv/qzmv_zz.root"},
   {"ww",  "data/new_zz/qzmv/qzmv_ww.root"},
   {"tt",  "data/new_zz/qzmv/qzmv_tt.root"},
   {"bb",  "data/new_zz/qzmv/qzmv_bb.root"},
   {"cc",  "data/new_zz/qzmv/qzmv_cc.root"},
   {"zy",  "data/new_zz/qzmv/qzmv_az.root"},
   {"mm",  "data/new_zz/qzmv/qzmv_mm.root"}
  }
 }
};

bool isonebin =false;
bool isbinned =false;
bool isforplot=false;
bool useexisting=false;
bool is2d =false;

bool isbcg=false;
bool istautau=false;
bool isyy=false;
bool isw=false;
bool isz=false;
bool isinvi=false;
bool ismuon=false;
bool isextrapolatetau=false;

int indexbyname(TString cname)
{
    for (int i=0; i<100; i++)
        if (c[i].name==cname) return i;
    return 0;
}
channel channelbyname(TString cname)
{
    for (int i=0; i<100; i++)
        if (c[i].name==cname) return c[i];
    return c[0];
}

TString funcsetting(TString cname, TString proc, Int_t index=1)
{
  TString f="";
  if (index==1)
  {
    if (proc=="b")
    {
	f="keys";
    }
    else
    { //signal
      if (cname.Contains("mzvj"))
      {
	if (proc=="zz") f="Voigtian";
      }
      if (cname.Contains("mzjv"))
      {
        if (proc=="zz") f="Voigtian";
	if (proc=="tt") f="keys";
        if (proc=="zy") f="keys";
      }
      if (cname.Contains("vzmj"))
      {
//	if (proc=="s")  f="Voigtian";
        if (proc=="zz") f="keys";
        if (proc=="ww") f="keys";
        if (proc=="tt") f="keys";
      }
      if (cname.Contains("vzjm"))
      { 
        if (proc=="s")  f="Voigtian";
        if (proc=="zz") f="keys";
        if (proc=="ww") f="keys";
        if (proc=="tt") f="keys";
        if (proc=="bb") f="Voigtian";
        if (proc=="cc") f="keys";
      } 
      if (cname.Contains("qzvm"))
      {
	if (proc=="s")  f="Voigtian";
        if (proc=="zz") f="Voigtian";
	if (proc=="bb") f="Voigtian";
        if (proc=="tt") f="Voigtian";
        if (proc=="ww") f="keys";
        if (proc=="cc") f="keys";
	if (proc=="gg") f="keys";
	if (proc=="zy") f="keys";
      }
      if (cname.Contains("qzmv"))
      {
        if (proc=="s")  f="Voigtian";
        if (proc=="zz") f="Voigtian";
        if (proc=="bb") f="Voigtian";
	if (proc=="tt") f="Voigtian";
        if (proc=="ww") f="keys";
        if (proc=="cc") f="keys";
        if (proc=="gg") f="keys";
        if (proc=="zy") f="keys";
      }
    }
  }
  return f;
}

Float_t lum=1; // 5 ab-1 to 5.6 ab-1

Float_t weightsetting(TString cname, TString proc)
{
    Float_t w=1;
    return w;
}
Float_t weightscale  (TString cname, TString proc)
{
    Float_t w=1;

    if (proc=="b")
    {
    }
    else
    {
        if (cname.Contains("mmtt")||cname.Contains("eett")||cname.Contains("qqtt") ||cname.Contains("tttt"))   
        {
        }
        else 
        {
            if ( cname.Contains("ew")  || cname.Contains("ez") || cname.Contains("eett") || cname.Contains("eeqq")  || cname.Contains("einc")) w*= 0.928;
            if ( cname.Contains("mw")                          || cname.Contains("mmtt") || cname.Contains("mmqq")  || cname.Contains("minc")) w*= 0.954;
            if ( cname.Contains("tw")  || cname.Contains("tz") || cname.Contains("tttt") || cname.Contains("ttqq") ) w*= 0.954;
            if ( cname.Contains("qw")  || cname.Contains("qz") || cname.Contains("qqtt") || cname.Contains("qqqq")) w*= 0.954;
            if ( cname.Contains("vw")  || cname.Contains("vz") || cname.Contains("vvtt") || cname.Contains("vvqq") || cname.Contains("vvmm") || cname.Contains("vv")) w*= 0.946;
            if ( cname.Contains("qqzy") ) w*= 0.950;
        }

    }
    return w;
}


void checkcname(TString cname)
{
    isz =false;

    if (!(cname.Contains("4v")) && !(cname.Contains("qqzy")) && cname.Contains("z") ) 
        isz=true;
    int test= isz;
    if (test!=1) cerr<<"Check channels with error!"<<endl;
}

int templatebins=20;  
Float_t onebinrange=50000;

Float_t number[4]={0.1,0.4,1,2};
TString lu_n="5";
TString n[4]={"0.5","2","5","10"}; 

Float_t uncer_cx    = 0.005; // this is uncer of cx.
TString sigma_cx    ="0.005";
Float_t uncer_lumi  = 0.001;
TString sigma_lumi  ="0.001";

int     n_sig, n_bkg;
Float_t m_low, m_high;
Float_t v2_high, v2_low;
TString proc[10];

    RooRealVar mu_s ("mu_s",  "mu_s",  1, -1, 5);
    RooRealVar mu_bb("mu_bb", "mu_bb", 1, -1, 5);
    RooRealVar mu_cc("mu_cc", "mu_cc", 1, -1, 5);
    RooRealVar mu_gg("mu_gg", "mu_gg", 1, -1, 5);
    RooRealVar mu_zz("mu_zz", "mu_zz", 1, -1, 5);
    RooRealVar mu_yy("mu_yy", "mu_yy", 1, -1, 5);
    RooRealVar mu_ww("mu_ww", "mu_ww", 1, -1, 5);
    RooRealVar mu_tt("mu_tt", "mu_tt", 1, -1, 5);
    RooRealVar mu_mu("mu_mu", "mu_mu", 1, -1, 5);
    RooRealVar mu_zr("mu_zr", "mu_zr", 1, -1, 5);

    RooRealVar zhbb("zhbb", "zhbb", 1, -1, 5);
    RooRealVar vvbb("vvbb", "vvbb", 1, -1, 5);
    RooRealVar vvhbb("vvhbb", "vvhbb", 1, -1, 5);
   
RooRealVar weight   ("weight", "weight", 1, -1, 10000.);
RooRealVar blikeness("blikeness", "blikeness", 0, 1);
RooRealVar clikeness("clikeness", "clikeness", 0, 1);
RooRealVar costheta("costheta","costheta", -1, 1);
RooRealVar invMass ("invMass", "invMass", 120, 150);
RooRealVar recMass ("recMass", "recMass", 70, 110);
RooRealVar logB("logB", "logB", 0, 2);
RooRealVar logC("logC", "logC", 0, 5);
RooRealVar wt("wt", "wt", 1);

// TString 2dname;
RooDataSet* d_tot;

        TString p0, p1, p2, p3, p4;
        TString tmH    ;
        TString tsigma ;
        TString tTalpha;
        TString tTn    ;
        TString tsigL  ;
        TString tsigR  ;
        TString tratio ;
        TString exps = "exp(@1*(@0-100)/100.0+@2*(@0-100)*(@0-100)/10000.0)";
        Float_t test_mass = 125.;

const map<TString, TString> name=
{
    {"vzej",    "Z#rightarrow#nu#nu, H#rightarrowZZ*#rightarrowe^{+}e^{-}q#bar{q}"},
    {"vzmj",    "Z#rightarrow#nu#nu, H#rightarrowZZ*#rightarrow#mu^{+}#mu^{-}q#bar{q}"},
    {"mzvj",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowZZ*#rightarrow#nu#nuq#bar{q}"},
    {"mzjv",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowZZ*#rightarrowq#bar{q}#nu#nu"},
    {"qzmv",    "Z#rightarrowq#bar{q}, H#rightarrowZZ*#rightarrow#mu^{+}#mu^{-}#nu#nu"},
    {"qzvm",    "Z#rightarrowq#bar{q}, H#rightarrowZZ*#rightarrow#nu#nu#mu^{+}#mu^{-}"},
};
const map<TString, TString> xrec=
{
    {"mzvj",        "Recoil"},
    {"mzjv",        "Recoil"},
    {"qzmv",        "Recoil"},
    {"qzvm",        "Recoil"},
};
const map<TString, TString> xname=
{
    {"vzej",    "eeq#bar{q}"},
    {"vzmj",    "#mu#muq#bar{q}"},
    {"mzvj",    "#mu#mu"},
    {"mzjv",    "#mu#mu"},
    {"qzmv",    "q#bar{q}"},
    {"qzvm",    "q#bar{q}"},
};
const map<TString, TString> varname=
{
    {"mzvj",            "Mass_H"},
    
};
const map<TString, Float_t> histomax=
{
    {"vzej",    80   },
};

TString varnamesetting(TString cname)
{
    TString str="Mass_H";
    if ( varname.count(cname)>0 )  str=varname.at(cname);
    return str;
}
TString namesetting(TString cname)
{
    TString str="";
    if ( name.count(cname)>0 )      str=name.at(cname);
    return str;
}
TString xnamesetting(TString cname)
{
    TString str="";
    if ( xname.count(cname)>0 )  str=xname.at(cname);
    return str;
}
TString xrecsetting(TString cname)
{
    TString str="";
    if ( xrec.count(cname)>0 )  str=xrec.at(cname);
    return str;
}

Float_t PlotMaximum=0;
bool SetPlotMaximum(TString cname )
{
    bool defined=false;
    if ( histomax.count(cname)>0 ) 
    {
        defined     = true;
        PlotMaximum = histomax.at(cname)*1.12;  // 5 to 5.6;
    }
    return defined;
}

RooWorkspace *makespace(TString cname, int index, Float_t lu);
Float_t pdfShape    (RooWorkspace &ws,   channel c, TString proc, TString func);

RooAbsPdf* pdffit(TString cname, RooRealVar &var, RooDataSet &data, TString func);
void plotFit    (RooWorkspace *wchannel,channel c, TString proc="s",TString lu_n="5");
void plotImport (RooWorkspace *wspace,  channel c, TString proc,    TString lu_n="5"); 
void FormatAxis(TAxis * axis, double offset);
void FormatLegend(TLegend *legend);
RooFitResult* Minimize(RooAbsPdf *&pdf, RooDataSet &data);

#endif
