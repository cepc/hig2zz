

#define DEBUG 1 // to 1: more details 
#include "head.h"
using namespace std;
using namespace RooFit;
using namespace RooStats;
//#include "MyDict.cxx"
// #include "HggTwoSidedCBPdf.cxx"
// #include "HggTwoSidedCBPdf.h"
//#include "RooGaussExp.cxx"
// #include "RooGaussExp.h"
// #include "RooGaussDoubleSidedExp.h"
// #include "HggTwoSidedCBPdf.h"
RooWorkspace *makespace(TString cname, int index, int lu)
{
    RooMsgService::instance().setGlobalKillBelow(RooFit::FATAL);
    lum=number[lu];
    lu_n=n[lu];
//gROOT->ProcessLine(".L /afs/ihep.ac.cn/users/z/zhangkl/wfs/workspace/src/RooGaussExp_cxx.so"); 

    channel c=channelbyname(cname);
    checkcname(cname);
    
    std::cerr << "Sep. 20th, 2019 " << std::endl;
    std::cerr << "change(set) the bool variable isz to false" << std::endl;
    std::cerr << "You may check/change the flags and so on for the other analysis" << std::endl;
    isz=false;

    n_sig =  c.nsig;
    n_bkg =  c.nbkg;
    m_low =  c.mlow;
    m_high=  c.mhigh;
    invMass.setRange(m_low, m_high);
    
    if (is2d)
    {
        if (cname.Contains("qqyy")) { v2_low=70; v2_high=120; } 
        if (cname.Contains("mmyy")) { v2_low=105; v2_high=145; }
        // if (cname.Contains("mmyy")) { v2_low=86; v2_high=100; }
        if (cname.Contains("vvyy")) { v2_low=70; v2_high=110; } 
        if (cname.Contains("qw4q")) { v2_low=65; v2_high=115; }  
        if (cname.Contains("mmtt")) { v2_low=-6; v2_high=  5; } 
        if (cname.Contains("qqtt")) { v2_low=-6; v2_high=  4; } 
        if (cname.Contains("eett")) { v2_low=-6; v2_high=  5; } 
        if (cname.Contains("vvtt")) { v2_low=-6; v2_high=  5; } 
        if (cname.Contains("vw4q")) { v2_low=75; v2_high=125; }
        recMass.setRange(v2_low, v2_high);
    }
    for (int i=0;i<n_sig;i++) { proc[i]  =  c.name_sig[i]; }

    cout << "Makeing workspace for channel " << cname << endl;  
    
    TString ECM="250"; 
    if (!is250) ECM="240";
    if (DEBUG && (index==0) )  cerr << "Begin "<<ECM<<" workspace building"<<endl;
    
    if (    
            // (isuseexistingpdf) && 
            false
            // (index<56)
            //  (!gSystem->AccessPathName("out/workspace/part/wchannel_"+cname+"_5.root")) 
            // !(cname.Contains("inc")) 
            // !( cname=="qqzy") 
            // !(ismuon || cname=="mcom")
            // !(is2d) || (istautau) 
            //  !( index==0 || index==4 || index==9)
            // !(cname.Contains("vvyy") || cname.Contains("mmyy") )
            // !(cname.Contains("vvlvlv") || cname.Contains("vvevev") || cname.Contains("vvevmv") || cname.Contains("vvmvmv"))
            // true
            // ( 
                //  (!gSystem->AccessPathName("out/workspace/part/wchannel_"+cname+"_5.root")) 
       )
    {
        cerr <<"-->Use existing workspace "<< cname << endl;
        // TFile fchannel("out/workspace/good/wchannel_"+cname+"_5.root");
        TFile fchannel("out/workspace/part/wchannel_"+cname+"_5.root");
        RooWorkspace *wchannel=(RooWorkspace*)fchannel.Get("wchannel_"+cname);
        return wchannel;
    }

    cerr << "Makeing workspace for channel " << cname << endl; //direnctly to screen
    RooWorkspace wspace("wspace");
    wspace.importClassCode();
    RooArgSet poi,nuispara,globobs,observable,un,constraints;

    // add cross section un 0.5%
    wspace.factory("sigma_cx["+sigma_cx+"]");
    wspace.factory("sum::un_cx(1, prod::uncer_cx(nuis_cx[0,-5,5], sigma_cx ))");
    wspace.factory("RooGaussian::constraint_cx(nuis_cx,global_nuis_cx[0,-5,5],1)");
    nuispara.add(*wspace.var("nuis_cx"));
    globobs.add(*wspace.var("global_nuis_cx"));
    un.add(*wspace.function("un_cx"));
    constraints.add(*wspace.pdf("constraint_cx"));

    // ADD luminosity un 0.1%
    wspace.factory("sigma_lumi["+sigma_lumi+"]");
    wspace.factory("sum::un_lumi(1, prod::uncer_lumi(nuis_lumi[ 0 , -5 , 5 ], sigma_lumi))");
    wspace.factory("RooGaussian::constraint_lumi(nuis_lumi,global_nuis_lumi[0,-5,5],1)");

    nuispara.add(*wspace.var("nuis_lumi"));
    globobs.add (*wspace.var("global_nuis_lumi"));
    un.add      (*wspace.function("un_lumi"));
    constraints.add(*wspace.pdf("constraint_lumi"));

    RooProdPdf constraint("constraint", "constraint", constraints);
    wspace.import(constraint);

    RooProduct u_c("u_c", "u_c", un); //uncer_common
    wspace.import(u_c);

        //Declare data path, number of signals, pois per channel
    if (cname=="vvhbb") poi.add(RooArgSet(zhbb, vvhbb)); 
    if (cname=="vvqq") poi.add(RooArgSet(vvbb));
    if ( isbcg  )   poi.add(RooArgSet(mu_bb,  mu_cc, mu_gg, mu_ww, mu_zz, zhbb)); 
    if (isyy)       poi.add(RooArgSet(mu_yy));
    if (ismuon)     poi.add(RooArgSet(mu_mu));
    if (isinvi)     poi.add(RooArgSet(mu_in));
    if (istautau)   poi.add(RooArgSet(mu_tt, mu_ww, mu_zz));
    if (cname=="mzvj") poi.add(RooArgSet(mu_tt, mu_ww, mu_zz, mu_zr));
    if (cname=="mzjv") poi.add(RooArgSet(mu_tt, mu_ww, mu_zz, mu_zr, mu_bb,  mu_cc, mu_gg));
    if (cname=="qqzy") poi.add(RooArgSet(mu_zr));
    if (isz)        poi.add(RooArgSet(mu_zz));
    if (isw)        poi.add(RooArgSet(mu_ww));
    if (cname.Contains("w4q"))  poi.add(RooArgSet(mu_zz));

    wspace.import(poi);

    // get yields and shape of signal and background
    Float_t ns, nbkg;
    TString ns_str, nbkg_str;
    TString a1, b1, a2, kcom, ksub, ksig, kzh, kz, a3, b3, a4, b4;

    TString modelname  = "SUM::modelSB(";
    kcom = "u_c";
    kzh  = "u_c";
    TString cname_collect;
    observable.add(weight);

    d_tot=new RooDataSet("d_tot","d_tot", RooArgSet(invMass, weight), WeightVar(weight));

if ( isforplot )
{
    observable.add(invMass);
    wspace.import(observable);
    wspace.defineSet("Observables", observable, kTRUE); //只能在此马上定义，出定义域会失效

    for (int i = 0; i < n_sig; i++) 
    {
        // ns = pdfShape(wspace, c, proc[i], "GaussExp");
        ns = pdfShape(wspace, c, proc[i], "DSCB");
        
        // if (DEBUG) cerr<<cname<<","<<proc[i]<<", events:"<<ns<<endl;
        ns_str=(TString)to_string(ns);
        a1 = "n_"+proc[i];
        if (i < (n_sig - 1)) modelname += a1 + "*pdf_" + proc[i] + ",";
        else if (n_bkg != 0) modelname += a1 + "*pdf_" + proc[i] + ",";
        else                 modelname += a1 + "*pdf_" + proc[i] + ")";

        b1 = "prod::" + a1 + "(" + ns_str ;

        TString cnamex;
        if (n_sig==1) cnamex=cname;
            else      cnamex=cname+"_"+proc[i];
        cname_collect+=cnamex+",";
        wspace.factory(cnamex+"[1,-1,5]");
        poi.add(*wspace.var(cnamex));
        b1 += ","+ cnamex + ")";

        wspace.factory(b1);
    }
    if (n_bkg != 0)
    {
        nbkg = pdfShape(wspace, c, "b" , "exp2");
        // if (DEBUG) cerr<<cname<<",b, events:"<<nbkg<<endl;
        nbkg_str=(TString)to_string(nbkg);
        wspace.factory("n_b[" + nbkg_str + "]");
        modelname += "n_b*pdf_b)";
    }
}
else if ( isbcg) 
{   
    // if ( cname=="eeqq" ||  cname=="mmqq") 
    observable.add(invMass);
    observable.add(blikeness);
    observable.add(clikeness);
    wspace.import(observable);
    wspace.defineSet("Observables", observable, kTRUE);

    for (int i = 0; i < n_sig; i++) 
    {
        // ns = tempsetShape(wspace, c, proc[i]);  
        ns = llh3dShape  (wspace, c, proc[i]);

        ns_str=(TString)to_string(ns);

        // if (DEBUG) cerr<<cname<<","<<proc[i]<<", events:"<<ns<<endl;
        modelname +="n_"+proc[i] + "*pdf_" + proc[i] + ",";              //multiply parameters on nsig
        b1 =  "prod::n_"+proc[i] + "(" + ns_str + "," + kcom;

        TString cnamex=cname+"_"+proc[i];
        cname_collect+=cnamex+",";
        wspace.factory(cnamex+"[1,-1,5]");
        poi.add(*wspace.var(cnamex));
        
        b1 += ","+cnamex;

        if (cnamex.Contains("eeqq_bb")) b1+=", zhbb";
        if (cnamex.Contains("mmqq_bb")) b1+=", zhbb";
        if (cnamex.Contains("qqqq_bb")) b1+=", zhbb";
        if (cnamex.Contains("vvqq_bb")) b1+=", vvbb";
        if (proc[i].Contains("bb")) b1+=", mu_bb)";
        if (proc[i].Contains("cc")) b1+=", mu_cc)";
        if (proc[i].Contains("gg")) b1+=", mu_gg)";
        if ( cname=="eeqq" ||  cname=="mmqq")
        {
            if (proc[i].Contains("ww")) b1+=", mu_ww)";
            if (proc[i].Contains("zz")) b1+=", mu_zz)";
        }
        else
        {
            if (proc[i].Contains("ww")) b1+=")";
            if (proc[i].Contains("zz")) b1+=")";
        }
        if (proc[i].Contains("tt")) b1+=")"; //bcg中的tautau不计入

        wspace.factory(b1);
    }
        // nbkg = tempsetShape(wspace, c, "b"); 
        nbkg = llh3dShape  (wspace, c, "b");
        nbkg_str=(TString)to_string(nbkg);
        // if (DEBUG) cerr<<cname<<","<<"b"<<", events:"<<nbkg<<endl;
    wspace.factory("n_b[" + nbkg_str + "]");
    modelname += "n_b*pdf_b)";
}
else if (cname=="vvhbb")
{
    observable.add(costheta);
    observable.add(invMass);
    wspace.import(observable);
    wspace.defineSet("Observables", observable, kTRUE);

    d_tot=new RooDataSet("d_tot","d_tot", RooArgSet(invMass, weight), WeightVar(weight));
    
    ns = fusionShape(wspace, c, "s");
        ns_str=(TString)to_string(ns);
        b1  = "prod::n_s(" + ns_str + ","+ kcom +", vvhbb)";
        wspace.factory(b1);
        // if (DEBUG) cerr<<cname<<","<<"s"<<", events:"<<ns<<endl;

    ns = fusionShape(wspace, c, "zh");
        ns_str=(TString)to_string(ns);
        b1  = "prod::n_zh(" + ns_str + "," + kzh + ",zhbb)";
        wspace.factory(b1);
        // if (DEBUG) cerr<<cname<<","<<"zh"<<", events:"<<ns<<endl;
    
    nbkg = fusionShape(wspace, c, "b");
        nbkg_str=(TString)to_string(nbkg);
        wspace.factory("n_b[" + nbkg_str + "]");
        // if (DEBUG) cerr<<cname<<",b, events:"<<nbkg<<endl;
        modelname+="n_s*pdf_s, n_zh*pdf_zh, n_b*pdf_b)";
}
else if ( isonebin )
{
    RooRealVar sample("invMass", "invMass", 0, onebinrange);
    observable.add(sample);
    wspace.import(observable);
    wspace.defineSet("Observables", observable, kTRUE);

    ns   =weightscale(cname, "s")*c.mlow* onebinShape(wspace, c, "s");      //mlow contains its signal event number
    // if (DEBUG) cerr<<cname<<",s, events:"<<ns<<endl;
    ns_str=(TString)to_string(ns);
    b1 = "prod::n_s(" + ns_str + ","+kcom;
    
    TString cnamex=cname;
    cname_collect+=cnamex+",";
    wspace.factory(cnamex+"[1,-1,5]");
    poi.add(*wspace.var(cnamex));
    if  (  cname.Contains("vvlvlv") || cname.Contains("vvevev") || cname.Contains("vvevmv") || cname.Contains("vvmvmv"))  b1+= ","+cnamex+",mu_ww)";
    // if  ( cname.Contains("qwlq"))   b1+= ",mu_ww)";
    // if  ( cname.Contains("incl"))   b1+= ", incl)";
    wspace.factory(b1);

    nbkg =weightscale(cname, "b")*c.mhigh* onebinShape(wspace, c, "b"); //high for bkg.
    // if (DEBUG) cerr<<cname<<",b, events:"<<nbkg<<endl;
    nbkg_str=(TString)to_string(nbkg);
    wspace.factory("n_b[" + nbkg_str + "]");
    modelname += "n_s*pdf_s, n_b*pdf_b)";
}
else 
{   //1d unbinned fit
    observable.add(invMass);
    // RooRealVar v2("v2", "second variable in 2d fit", m_low, m_high);
    // cout<<"Now we are here"<<endl;
    if (is2d) observable.add(recMass);
        
    wspace.import(observable);
    wspace.defineSet("Observables", observable, kTRUE);

    // d_tot=new RooDataSet("d_tot","d_tot", RooArgSet(invMass, weight), WeightVar(weight));

    if (cname.Contains("qqzy"))
    {
        ns =weightscale(cname, "s")*zgammaShape(wspace, c, "s");   
        ns_str=(TString)to_string(ns);
        b1 = "prod::n_s(" + ns_str + ","+kcom+ ", mu_zr)";
        wspace.factory(b1);

        nbkg =weightscale(cname, "b")*zgammaShape(wspace, c, "b");
        nbkg_str=(TString)to_string(nbkg);
        wspace.factory("n_b[" + nbkg_str + "]");
        modelname += "n_s*pdf_s, n_b*pdf_b)";
    }
    else
    for (int i = 0; i < n_sig; i++) 
    {
        TString func="DSCB";
        if (isbinned) func="binned";
        ns = pdfShape(wspace, c, proc[i], func);
        // if (DEBUG) cerr<<cname<<","<<proc[i]<<", events:"<<ns<<endl;  
        ns_str=(TString)to_string(ns);
        a1 = "n_"+proc[i];
        if (i < (n_sig - 1)) modelname += a1 + "*pdf_" + proc[i] + ",";
        else if (n_bkg != 0) modelname += a1 + "*pdf_" + proc[i] + ",";
        else                 modelname += a1 + "*pdf_" + proc[i] + ")";

        b1 = "prod::" + a1 + "(" + ns_str + "," + kcom;
        
        if (cname=="mcom")               b1 += ")";
        if (proc[i].Contains("zh"))      b1 += ")";
        else 
        {
            TString cnamex;
            if (n_sig==1) cnamex=cname;
                else      cnamex=cname+"_"+proc[i];
            cname_collect+=cnamex+",";
            wspace.factory(cnamex+"[1,-1,5]");
            poi.add(*wspace.var(cnamex));
            b1 += ","+cnamex;
            if (cname.Contains("mzvj"))
            {
                if (proc[i].Contains("s"))  b1 +=",mu_zz)";
                if (proc[i].Contains("ww")) b1 +=",mu_ww)";
                if (proc[i].Contains("zz")) b1 +=",mu_zz)";
                if (proc[i].Contains("tt")) b1 +=",mu_tt)";
                if (proc[i].Contains("zy")) b1 +=",mu_zr)";
            }
            if (cname.Contains("mzjv"))
            {
                if (proc[i].Contains("s"))  b1 +=",mu_zz)";
                if (proc[i].Contains("ww")) b1 +=",mu_ww)";
                if (proc[i].Contains("zz")) b1 +=",mu_zz)";
                if (proc[i].Contains("tt")) b1 +=",mu_tt)";
                if (proc[i].Contains("zy")) b1 +=",mu_zr)";
                if (proc[i].Contains("bb")) b1+=", mu_bb)";
                if (proc[i].Contains("cc")) b1+=", mu_cc)";
                if (proc[i].Contains("gg")) b1+=", mu_gg)";
            }
            else if (isinvi)  b1 += ",mu_in)";
            else if (isz)     b1 += ",mu_zz)";
            else if (isyy)    b1 += ",mu_yy)";
            else if (ismuon)  b1 += ",mu_mu)";
            else if (proc[i].Contains("s") && isw ) b1 += ",mu_ww)";
            else if (cname.Contains("w4q") || istautau )
            {
                if (proc[i].Contains("bb")) b1 +=")";
                if (proc[i].Contains("cc")) b1 +=")";
                if (proc[i].Contains("gg")) b1 +=")";
                if (proc[i].Contains("ww")) b1 +=",mu_ww)";
                if (proc[i].Contains("zz")) b1 +=",mu_zz)";
                if (proc[i].Contains("tt")) b1 +=",mu_tt)";
            }
        }
        wspace.factory(b1);
    }
    if (n_bkg != 0)
    {
        TString func="exp2";
        if (isbinned) func="binned";
        nbkg = pdfShape(wspace, c, "b" , func);

        // if (DEBUG) cerr<<cname<<",b, events:"<<nbkg<<endl;  
        nbkg_str=(TString)to_string(nbkg);
        wspace.factory("n_b[" + nbkg_str + "]");
        modelname += "n_b*pdf_b)";
    }
}

if (!(cname.Contains("qqzy") || isonebin )) wspace.import(*d_tot);
wspace.factory(modelname);
wspace.factory("RooUniform::Uniform(Uni[1])");

wspace.defineSet("Pois", poi, kTRUE);
wspace.Print("v");

if (index == 0) wspace.factory("PROD::model(modelSB,constraint)");
else            wspace.factory("PROD::model(modelSB,Uniform)");


TString correlated = "Uni, Uniform, sigma_cx, sigma_lumi, zhbb, vvhbb, vvbb, mu_bb, mu_cc, mu_gg, mu_zz, mu_yy, mu_zr, mu_ww, mu_tt, mu_in, mu_mu,";
correlated+=cname_collect;

// cout<<"correlated var:"<<correlated<<endl;

TIterator  *iter_nui = nuispara.createIterator();
RooRealVar *parg_nui = NULL;
while ((parg_nui = (RooRealVar *)iter_nui->Next())) {
    correlated =correlated + "," + parg_nui->GetName()+ ", global_"+ parg_nui->GetName();
}

RooWorkspace *wchannel = new RooWorkspace("wchannel_" + cname);
wchannel->importClassCode();
wchannel->import(poi, RooFit::RecycleConflictNodes());
wchannel->import(*wspace.pdf("model"), RooFit::RenameAllNodes(cname),
                    RooFit::RenameAllVariablesExcept(cname, correlated),
                    RooFit::RecycleConflictNodes());
wchannel->import(constraint);

RooArgSet *nuisance_wchannel = new RooArgSet();
iter_nui->Reset();
while ((parg_nui = (RooRealVar *)iter_nui->Next())) nuisance_wchannel->add(*(RooRealVar *)wchannel->obj(parg_nui->GetName()));

RooArgSet *global_wchannel = new RooArgSet();
TIterator *iter_global = globobs.createIterator();
iter_global->Reset();
RooRealVar *parg_global = NULL;
while ((parg_global = (RooRealVar *)iter_global->Next())) global_wchannel->add(*(RooRealVar *)wchannel->obj(parg_global->GetName()));

RooArgSet *observable_wchannel = new RooArgSet();
TIterator *iter_observable = wspace.set("Observables")->createIterator();
RooRealVar *parg_observable;
while ((parg_observable = (RooRealVar *)iter_observable->Next())) 
{
    TString name_observable = parg_observable->GetName() + (TString)"_" + cname;
    if ((bool)wchannel->obj(name_observable) == true) observable_wchannel->add(*(RooRealVar *)wchannel->obj(name_observable));
}

RooArgSet *poi_set = new RooArgSet();
TIterator *iter_poi = wspace.set("Pois")->createIterator();
RooRealVar *parg_poi;
while ((parg_poi = (RooRealVar *)iter_poi->Next())) 
{
    if ((bool)wchannel->obj(parg_poi->GetName()) == true) poi_set->add(*(RooRealVar *)wchannel->obj(parg_poi->GetName()));
}

wchannel->defineSet("Pois",                 *poi_set,               kTRUE);
wchannel->defineSet("Observables",          *observable_wchannel,   kTRUE);
wchannel->defineSet("nuisanceParameters",   *nuisance_wchannel,     kTRUE);
wchannel->defineSet("globalObservables",    *global_wchannel,       kTRUE);

RooArgSet *obs_plus_wt = new RooArgSet();
obs_plus_wt->add(wt);
obs_plus_wt->add(*wchannel->set("Observables"));
RooDataSet *AsimovSB =  new RooDataSet("AsimovSB", "AsimovSB", *obs_plus_wt, WeightVar(wt));

Float_t npoints = 1000.;
Float_t total_SBevents = 0;
if ( isforplot )             npoints = 100.;
// if ( cname.Contains("inc") ) npoints = 5000.;
//now seems enough.
if ( isinvi ) npoints*= 20;

for (int i = 0; i < n_sig; i++) total_SBevents += (*wchannel->function("n_" + proc[i] +"_" + cname)).getVal();
// if ( n_bkg != 0)   total_SBevents += (*wchannel->var("n_b_" + cname)).getVal();
if ( cname.Contains("qqzy") || n_bkg != 0)   total_SBevents += (*wchannel->var("n_b_" + cname)).getVal();
cerr<<"Begin making Asimov data"<<endl;

RooAbsReal *integral;
Float_t integral_weight; 
if (  isbcg )  //3d 
{
    RooRealVar *mas = wchannel->var("invMass_" + cname);
    RooRealVar *b = wchannel->var("blikeness_" + cname);
    RooRealVar *c = wchannel->var("clikeness_" + cname);
    RooArgSet mbc(*mas, *b, *c);
    npoints = Float_t(templatebins);         
    // npoints = Float_t(20.);
    Float_t width = 1./20;  //老问题,除号时要加点……
    Float_t b_val, c_val;
    Float_t m_val = m_low;
    Float_t massrange = m_high - m_low;
    Float_t mwidth = massrange /50.;
    Float_t integral_weight;
    RooAbsReal *integral;
    Float_t sum=0;
    for (b_val = 0; b_val < 1; b_val += width) 
    {
        b->setRange("range", b_val, b_val + width);
        b->setVal(b_val + 0.5 * width);
    for (c_val = 0; b_val+c_val < 1; c_val += width) //Triangle attention! 10k points in total
    {
        c->setRange("range", c_val, c_val + width);
        c->setVal(c_val + 0.5 * width);
    for ( m_val=m_low; m_val<m_high; m_val+=mwidth)         
    {
        mas->setRange("range", m_val, m_val + mwidth);
        mas->setVal(m_val+0.5*mwidth);
        integral =(RooAbsReal *)(wchannel->pdf("modelSB_" + cname))->createIntegral(mbc, NormSet(mbc), Range("range"));          //对bc都进行归一化。只对一个归一是错的
        if (DEBUG && (c_val==0) && (m_val==m_low)) cerr<<"b:"<<b_val<<" b+c:"<<b_val+c_val<<" mass:"<<m_val<<" Int:"<<integral->getVal()<<endl;
        sum+=integral->getVal();
        integral_weight= integral->getVal() * total_SBevents;
        wt.setVal(integral_weight);
        AsimovSB->add(RooArgSet(*mas, *b, *c, wt), integral_weight);
    }
    }
    }
    integral =(RooAbsReal *)(wchannel->pdf("modelSB_" + cname))->createIntegral(mbc, NormSet(mbc));
    cerr<<"tot="<<integral->getVal()<<", sum="<<sum<<endl;
}
else  
if (is2d || cname=="vvhbb") //2d
{
     TString tv2="recMass"; 
     if (cname=="vvhbb") { tv2="costheta"; v2_high=1; v2_low=-1;}
     RooRealVar *v1 = wchannel->var("invMass_" + cname);
     RooRealVar *v2 = wchannel->var(tv2+   "_" + cname);
    Float_t v1range = c.mhigh - c.mlow;
    Float_t v1width = v1range / 50.;
    Float_t v2range = v2_high - v2_low;
    Float_t v2width = v2range / 50.;
    RooArgSet v12(*v1, *v2);
    for (Float_t v1_val  = c.mlow; v1_val < c.mhigh; v1_val += v1width) 
    {
        v1->setRange("range", v1_val, v1_val + v1width);
        v1->setVal(v1_val + 0.5 * v1width);
    for (Float_t v2_val  = v2_low; v2_val < v2_high; v2_val += v2width) 
    {
        v2->setRange("range", v2_val, v2_val + v2width);
        v2->setVal(v2_val + 0.5 * v2width);
        integral =(RooAbsReal *)
            (wchannel->pdf("modelSB_" + cname))->createIntegral(v12, NormSet(v12), Range("range"));
            //  if (DEBUG) cerr<<"v1:"<<v1->getVal()<<" v2:"<<v2->getVal()<<" Int:"<<integral->getVal()<<endl;
        integral_weight = integral->getVal() * total_SBevents;
        wt.setVal(integral_weight);
        AsimovSB->add(RooArgSet(*v1, *v2, wt), integral_weight);
    }
    }
}
else  //1d
{
    RooRealVar *mas = wchannel->var("invMass_" + cname);
    // if (cname.Contains("imp")) mas=wchannel->var("impact_" + cname);
    Float_t massrange = c.mhigh - c.mlow;
    Float_t width = massrange / npoints;
    Float_t mass_val  = c.mlow;
    if (isonebin)
    {
        npoints    = 500;       //one bin npoints无关。但不能太小
        massrange  = onebinrange;
        width      = massrange / npoints;
        mass_val   = 0;
    }
    for (int i = 0; i < npoints; i++) {
        mas->setRange("range", mass_val, mass_val + width);
        integral =(RooAbsReal *)
            (wchannel->pdf("modelSB_" + cname)->createIntegral(RooArgSet(*mas), NormSet(*mas),Range("range")));
        mas->setVal(mass_val+ 0.5 * width);
        integral_weight = integral->getVal() * total_SBevents ;
        wt.setVal(integral_weight);
        AsimovSB->add(RooArgSet(*mas, wt), integral_weight);
        mass_val += width;
    }
}

    wchannel->import(*AsimovSB);
// wspace.import(*AsimovSB);
//     if (lu==2)
// {
    if ( isbcg || cname.Contains("qqzy") || isonebin )
        //  ||  cname.Contains("imp")
    {
        cout << "dimension plot To be added" << endl;
    }
     else
    {   //便于plot
        wchannel->import(*d_tot, RooFit::RenameAllNodes(cname),
          RooFit::RenameAllVariablesExcept(cname, correlated),
          RooFit::RecycleConflictNodes(),
          RooFit::RenameVariable("invMass","invMass_"+cname));

    }
// }

    wspace.writeToFile("out/workspace/part/ws_"+cname+"_"+lu_n+".root");
    wchannel->writeToFile("out/workspace/part/wchannel_"+cname+"_"+lu_n+".root");

    for (int i=0;i<n_sig;i++) { proc[i]  =  ""; }  
    return wchannel;
}
Float_t fusionShape(RooWorkspace &ws,   channel c, TString proc) 
{
    TString cname=c.name;
    TString ntuple;
    if (proc=="b") ntuple=c.f_bkg; 
    else ntuple =c.f_sig.at(proc);

    TFile *f = new TFile(ntuple);
    TTree *data = (TTree *)f->Get("HiggsTree");

    Float_t var, theta, scale;

    data->SetBranchAddress("Mass_invar", &var);
    data->SetBranchAddress("costheta",   &theta);
    data->SetBranchAddress("weight",     &scale);

    TH1F *dist = new TH1F("d2", "d2", 25, -1, 1.); //100 bin结果反而变差了

    RooDataSet d_mass ("d_mass_"+proc,  "d_mass_"+proc,  RooArgSet(invMass,  weight), WeightVar(weight));
    RooDataSet d_theta("d_theta_"+proc, "d_theta_"+proc, RooArgSet(costheta, weight), WeightVar(weight));

    Int_t nentries = data->GetEntries();
    Float_t ns = 0;

    for (Int_t i = 0; i < nentries; i++) 
    {
        data->GetEvent(i);
        
        if (weightsetting(cname, proc)!=1) 
        scale =weightsetting(cname, proc);
        scale*=weightscale  (cname, proc);
        
        ns += scale;

        invMass .setVal(var);
        costheta.setVal(theta);
        dist->Fill (theta,    scale);
        d_mass.add (invMass,  scale);
        d_theta.add(costheta, scale);
        d_tot->add(invMass,  scale);
    }
    RooDataHist d_Hist((TString)("d_" + proc+"_"+lu_n),
                       (TString)("d_" + proc+"_"+lu_n), costheta, dist);
    RooHistPdf h_pdf  ((TString)("hpdf_" + proc), (TString)("hpdf_" + proc), costheta, d_Hist, 1);

    cout << "primez_label=" << proc << "," << cname << endl;
    cout << "Building a 2d pdf from wwfusion histogram " << endl;

    RooAbsPdf* pdf;
    if ( isuseexistingpdf ) 
    {
        cerr<<"using existing mass pdf"<<endl;
        TFile fs("out/workspace/part/ws_"+cname+"_5.root");
        RooWorkspace *wchannel=(RooWorkspace*)fs.Get("wspace");
        pdf =wchannel->pdf("mpdf_"+proc);
        ws.import(*pdf);
        // "out/workspace/part/wchannel_"+cname+"_5.root"
    }
    else
    {
        pdf = pdffit(cname, invMass, d_mass, "keys");
        pdf->SetNameTitle("mpdf_"+proc, "mpdf_"+proc);
        // pdf = new RooKeysPdf("mpdf_"+proc, "mpdf_"+proc, invMass, d_mass, RooKeysPdf::MirrorAsymBoth, 5);
        ws.import(*pdf);
    }
    ws.import(h_pdf);
    ws.import(d_mass);
    // ws.import(m_pdf);
    // ws.import(d_Hist);
    ws.factory("PROD:pdf_"+proc+"(mpdf_"+proc+", hpdf_"+proc+")");

    delete f;
    return ns;
}
Float_t zgammaShape(RooWorkspace &ws,   channel c, TString proc) 
{
    TString cname=c.name;
    TFile *f   =new TFile(c.f_bkg);
    TString n;
    if (proc.Contains("s")) n="hdm_zg";
    if (proc.Contains("b")) n="hdm_Pvv";
    TH1F *dist = (TH1F*)f->Get(n);
    Float_t ns = dist->GetSum();

    // RooRealVar invMass("invMass", "invMass", c.mlow, c.mhigh);
    RooDataHist d_Hist((TString)("d_mass_" + proc),
                       (TString)("d_mass_" + proc),
                       invMass, dist);

    if (proc.Contains("b"))
    {
        RooRealVar mean("mean", "mean", 42, 30, 60);
        RooRealVar Sigma1("Sigma1", "Sigma1", 2, 0.1, 20);
        RooRealVar Sigma2("Sigma2", "Sigma2", 2, 0.1, 20);
        RooAbsPdf* pdf=new RooBifurGauss("pdf_b", "pdf_b", invMass, mean, Sigma1, Sigma2);
        // RooAbsPdf* pdf=new RooGaussian("pdf_b", "pdf_b", invMass, mean, Sigma1);
        // RooFitResult* result_mu=Minimize(pdf,  (RooDataSet)d_Hist);
        pdf->fitTo(d_Hist); //自己写的Minimize 不支持RooDataHist (其实重载一个即可 懒得写)
        
        p0=(TString)to_string(mean .getVal());
        p1=(TString)to_string(Sigma1.getVal());
        p2=(TString)to_string(Sigma2.getVal());
        cout<<"p0:"<<p0<<endl;
        cout<<"p1:"<<p1<<endl;
        cout<<"p2:"<<p2<<endl;
        ws.factory("RooBifurGauss::pdf_" +proc+ "(invMass, mean1_" +proc+ "["+p0+"],sigma1_" +proc+ "["+p1+"],sigma2_" +proc+ "["+p2+"]);");
    }
    else
    {
        // as requested, only 1 single gaussian
        RooRealVar mean2("mean2", "mean2", 35, 30, 36);
        RooRealVar Sigma2("Sigma2", "Sigma2", 2, 0.01, 3);
        RooGaussian peak  ("peak",   "peak",    invMass, mean2, Sigma2);
        peak.fitTo(d_Hist);
        p2=(TString)to_string(mean2 .getVal());
        p3=(TString)to_string(Sigma2.getVal());
        ws.factory("RooGaussian::pdf_s (invMass, mean_s["+p2+"],sigma_s["+p3+"]);");
    }

    cout << "primez_label=" << proc << "," << cname << endl;
    cout << "Building a 1d pdf from binned histogram " << endl;

    ws.import(d_Hist);

    return ns;
}
Float_t onebinShape(RooWorkspace &ws,   channel c, TString proc) 
{
    TString cname=c.name;
    cout << "primez_label=" << proc << "," << cname << endl;
    cout << "Building a 1d pdf from event number " << endl;
    invMass.setRange(0, onebinrange);
    RooUniform h_pdf((TString)("pdf_" + proc), (TString)("pdf_" + proc), invMass); // flat 即可
    ws.import(h_pdf);
    return 1;
}
Float_t llh3dShape(RooWorkspace &ws,   channel c, TString proc)
{
    TString cname=c.name;

    TString ntuple;
    if (proc=="b") ntuple=c.f_bkg; 
    else ntuple =c.f_sig.at(proc);

    TFile *f = new TFile(ntuple);
    TTree *data = (TTree *)f->Get("HiggsTree");

    Float_t blike, clike;
    Float_t scale, var;

    data->SetBranchAddress("Blikeness", &blike);
    data->SetBranchAddress("Clikeness", &clike);
    data->SetBranchAddress("Mass_invar",&var);
    data->SetBranchAddress("weight", &scale);

    RooDataSet d_mass ("d_mass_"+proc,  "d_mass_"+proc,  RooArgSet(invMass,   weight), WeightVar(weight));

    Int_t nentries = data->GetEntries();
    Float_t ns = 0;

    Int_t binnumber=20;
    // binnumber=20;
    TH2F *dist = new TH2F("d_" + proc, "d_" + proc, binnumber, 0., 1., binnumber, 0., 1.);

    for (Int_t i = 0; i < nentries; i++) 
    {
        data->GetEvent(i);
        if (( var < c.mlow || var > c.mhigh))  continue;

        if (weightsetting(cname, proc)!=1) 
        scale =weightsetting(cname, proc);
        scale*=weightscale  (cname, proc);

        ns += scale;
        dist->Fill(blike, clike, scale);
        // Float_t x=fabs(blike-clike)/(blike+clike);
        // Float_t y=blike+clike;
        // dist->Fill(x, y, 0.5*scale);
        // dist->Fill(1-x, 1-y, 0.5*scale);         // 这个拓展到0-1平面的也不行

        // dist->Fill(blike, clike, 0.5*scale);
        // dist->Fill(1-blike, 1-clike, 0.5*scale); //镜像法大量损失了信息

        invMass.setVal(var);
        d_mass.add(invMass, scale);
        d_tot->add(invMass, scale);
    }

    RooAbsPdf *pdf;
    // if ( true )
    if ( isuseexistingpdf ) 
    {
        cerr<<"using existing mass pdf"<<endl;
        TFile fs("out/workspace/part/ws_"+cname+"_5.root");
        RooWorkspace *wchannel=(RooWorkspace*)fs.Get("wspace");
        pdf =wchannel->pdf("mpdf_"+proc);
        ws.import(*pdf);
        // "out/workspace/part/wchannel_"+cname+"_5.root"
    }
    else 
    {
    if ((proc=="b") && (cname.Contains("eeqq") || cname.Contains("mmqq")))
    {
        pdf = pdffit(cname, invMass, d_mass, "exp2");
        ws.factory("EXPR::mpdf_" + proc + "('" + exps + "',invMass, p0_" + proc + "[" + p0 + "], p1_" + proc + "[" + p1 + "])");
    }
    else if (cname.Contains("eeqq") || cname.Contains("mmqq"))
    {
        pdf = pdffit(cname, invMass, d_mass, "DSCB");
        ws.factory("RooCBShape::peakPdf_"    + proc + "(invMass,mH_"   + proc + "[" +tmH + "],sigma_" + proc + "[" + tsigma + "],Talpha_"+ proc + "[" + tTalpha+ "],Tn_"    + proc + "[" + tTn    + "]);");
        ws.factory("RooBifurGauss::tailPdf_" + proc + "(invMass,mtail_"+ proc + "[" +tmH + "],sigL_"  + proc + "[" + tsigL  + "],sigR_"  + proc + "[" + tsigR  + "]);");
        ws.factory("SUM::mpdf_" + proc + "(r_"+ proc + "[" + tratio +"]*peakPdf_" + proc + ",tailPdf_" + proc + ")");
    }
    else
    {
        pdf = pdffit(cname, invMass, d_mass, "keys");
        pdf->SetNameTitle("mpdf_"+proc, "mpdf_"+proc);
        // pdf = new RooKeysPdf("mpdf_"+proc, "mpdf_"+proc, invMass, d_mass, RooKeysPdf::MirrorAsymBoth, 5);
        ws.import(*pdf);
    }
    }

    RooDataHist d_Hist((TString)("d_" + proc + "_" + cname),
                       (TString)("d_" + proc + "_" + cname),
                       RooArgList(blikeness, clikeness), dist);
    RooHistPdf h_pdf((TString)("hpdf_" + proc), (TString)("hpdf_" + proc),
                       RooArgList(blikeness, clikeness), d_Hist, 0);

    cout << "primez_label=" << proc << "," << cname << endl;
    cout << "Building a 3d pdf from tempset histogram " << endl;

    ws.import(h_pdf);
    ws.import(d_Hist);
    ws.import(d_mass);

    ws.factory("PROD:pdf_"+proc+"(mpdf_"+proc+", hpdf_"+proc+")");
    delete f;
    return ns;
}
Float_t pdfShape(RooWorkspace &ws, channel c, TString proc, TString func) 
{
    TString cname=c.name;
    TString ntuple;
    if (proc=="b") ntuple=c.f_bkg; 
    else ntuple =c.f_sig.at(proc);

    TFile *f = new TFile(ntuple);
    TTree *data = (TTree *)f->Get("HiggsTree");

    Float_t var;   Float_t var2;
    Float_t scale;
    Int_t nentries = data->GetEntries();
    Float_t ns = 0;

    RooDataSet d_mass("d_mass_"+proc, "d_mass_"+proc, RooArgSet(invMass, weight), WeightVar(weight));
 
    RooDataSet *d_v2;
    if (is2d)
    {
        d_v2  = new RooDataSet("d_v2_"+proc, "d_v2_"+proc, RooArgSet(recMass, weight), WeightVar(weight));
            if (cname.Contains("qqyy")) data->SetBranchAddress("r_yy",       &var2); 
            // if (cname.Contains("mmyy")) data->SetBranchAddress("r_yy",       &var2);
            if (cname.Contains("mmyy")) data->SetBranchAddress("r_ll",       &var2);
            if (cname.Contains("vvyy")) data->SetBranchAddress("r_yy",       &var2); 
            if (cname.Contains("qw4q")) data->SetBranchAddress("Mass_Z",     &var2);  
            if (cname.Contains("mmtt")) data->SetBranchAddress("impact",     &var2); 
            if (cname.Contains("qqtt")) data->SetBranchAddress("impact",     &var2); 
            if (cname.Contains("eett")) data->SetBranchAddress("impact",     &var2); 
            if (cname.Contains("vvtt")) data->SetBranchAddress("impact",     &var2); 
            if (cname.Contains("vw4q")) data->SetBranchAddress("Mass_missing", &var2);
    }
    data->SetBranchAddress(varnamesetting(cname), &var);
    data->SetBranchAddress("weight",     &scale);
    for (Int_t i = 0; i < nentries; i++) 
    {
        data->GetEvent(i);
        if (( var < c.mlow || var > c.mhigh))  continue;

        if (weightsetting(cname, proc)!=1) 
        scale =weightsetting(cname, proc);
        scale*=weightscale  (cname, proc);

        ns += scale;

        invMass.setVal(var);
        d_mass.add(invMass, scale);
        d_tot->add(invMass, scale);
        if (is2d) 
        {
            recMass.setVal(var2);
            d_v2-> add(recMass, scale);
        }
    }
    ws.import(d_mass);
    if (is2d) ws.import(*d_v2);
    RooAbsPdf *pdf;
    // if (true) 
    
    if ( isuseexistingpdf ) 
    {   //  using existing pdf
        TFile fs("out/workspace/part/ws_"+cname+"_5.root");
        RooWorkspace *wchannel=(RooWorkspace*)fs.Get("wspace");
        pdf =wchannel->pdf("pdf_"+proc);
        ws.import(*pdf);
        //
        // "out/workspace/part/wchannel_"+cname+"_5.root"
    }
    else 
{
    TString fun=funcsetting(cname, proc, 1);
    std::cerr << std::endl;
    std::cerr << "The func type to be fitted to each pdf is set in pdfShape function " << std::endl;
    std::cerr << "If you want to change that, please visit the line here" << std::endl;
    // if( proc.Contains("zz") ){  func = "exp2" ; }

    if ((fun!="") && (!cname.Contains("_"))) func=fun;
    if (nentries<28) func="keys";
    cerr << "primez_label=" << proc << "," << cname <<", 1st func="<<func<< endl;


if (!is2d)
{
    if (cname.Contains("rec")) test_mass = 91.19;
    pdf = pdffit(cname, invMass, d_mass, func);

    if ( func.Contains("cheb")  )
    { 
        ws.factory("RooChebychev::pdf_" + proc + "( invMass,{p0_"+ proc + "[" + p0+ "],p1_"+ proc + "[" + p1+ "],p2_"+ proc + "[" + p2+ "],p3_"+ proc + "[" + p3+ "],p4_"+ proc + "[" + p4+ "]});");
    }
    else if ( func.Contains("keys")  || func.Contains("binned") )
    {
        pdf->SetNameTitle("pdf_"+proc, "pdf_"+proc);
        ws.import(*pdf);
    }
    else if ( func.Contains("exp2"))
    {
        ws.factory("EXPR::pdf_" + proc + "('" + exps + "',invMass, p0_1" + proc + "[" + p0 + "], p1_1" + proc + "[" + p1 + "])");
    }
    else if ( func.Contains("Voigtian")  )
    {
        ws.factory("Voigtian::pdf_" + proc + "(invMass, mH_" + proc + "[" + p0 + "], width_" + proc + "[" + p1 + "], sigma_"+ proc +"["+ p2 +"])");
    }
    else if ( func.Contains("BifurGuassian") )
    {
        ws.factory("BifurGauss::pdf_" + proc + "(invMass, mH_" + proc + "[" + p0 + "], sigL_" + proc + "[" + p1 + "], sigR_"+ proc +"["+ p2 +"])");
    }
    else if ( func.Contains("GaussExp") )
    {
        // gROOT->ProcessLine(".L /afs/ihep.ac.cn/users/z/zhangkl/wfs/workspace/lib/libRooGaussExp.so"); 
        // pdf->Print();
        ws.importClassCode("RooGaussExp");
        ws.factory("mH_"    + proc + "[" + tmH + "]");
        ws.factory("sigma_" + proc + "[" + tsigma + "]");
        ws.factory("Tn_" + proc + "[" + tTn + "]");
        ws.factory("RooGaussExp::pdf_" + proc + "(invMass, mH_" + proc + ", sigma_" + proc + ", Tn_"+ proc +")");
        //Factory 并不行。 在非编译环境下可以factory/ import, 但依然不能将workspace存入文件.
        cout<<__LINE__<<endl;
        cout<<"20180826"<<endl;
        ws.Print("v");
    }
    else if ( func.Contains("CB") )
    {
        ws.factory("RooCBShape::peakPdf_"    + proc + "(invMass,mH_"   + proc + "[" +tmH + "],sigma_" + proc + "[" + tsigma + "],Talpha_"+ proc + "[" + tTalpha+ "],Tn_"    + proc + "[" + tTn    + "]);");
        ws.factory("RooBifurGauss::tailPdf_" + proc + "(invMass,mtail_"+ proc + "[" +tmH + "],sigL_"  + proc + "[" + tsigL  + "],sigR_"  + proc + "[" + tsigR  + "]);");
        ws.factory("SUM::pdf_" + proc + "(r_"+ proc + "[" + tratio +"]*peakPdf_" + proc + ",tailPdf_" + proc + ")");
        //  ws.factory("RooGaussExp::pdf_" + proc + "(invMass, mH_" + proc + "[" + p0 + "], sigma_" + proc + "[" + p1 + "], sigR_"+ proc +"["+ p2 +"])");
    }
// result_mu->Print("v");
}
else
{

pdf = pdffit(cname, invMass, d_mass, func);

    if ( func.Contains("cheb")  )
    { 
        ws.factory("RooChebychev::pdf1_" + proc + "( invMass,{p0_"+ proc + "[" + p0+ "],p1_"+ proc + "[" + p1+ "],p2_"+ proc + "[" + p2+ "],p3_"+ proc + "[" + p3+ "],p4_"+ proc + "[" + p4+ "]});");
    }
    else if ( func.Contains("keys")  || func.Contains("binned") )
    {
        pdf->SetNameTitle("pdf1_"+proc, "pdf1_"+proc);
        ws.import(*pdf);
    }
    else if ( func.Contains("exp2"))
    {
        ws.factory("EXPR::pdf1_" + proc + "('" + exps + "',invMass, p0_1" + proc + "[" + p0 + "], p1_1" + proc + "[" + p1 + "])");
    }
    else if ( func.Contains("Voigtian")  )
    {
        ws.factory("Voigtian::pdf1_" + proc + "(invMass, mH_" + proc + "[" + p0 + "], width_" + proc + "[" + p1 + "], sigma_"+ proc +"["+ p2 +"])");
    }
    else if ( func.Contains("BifurGuassian") )
    {
        ws.factory("BifurGauss::pdf1_" + proc + "(invMass, mH_" + proc + "[" + p0 + "], sigL_" + proc + "[" + p1 + "], sigR_"+ proc +"["+ p2 +"])");
    }
    else if ( func.Contains("CB") )
    {
        ws.factory("RooCBShape::peakPdf1_"    + proc + "(invMass,mH_"   + proc + "[" +tmH + "],sigma_" + proc + "[" + tsigma + "],Talpha_"+ proc + "[" + tTalpha+ "],Tn_"    + proc + "[" + tTn    + "]);");
        ws.factory("RooBifurGauss::tailPdf1_" + proc + "(invMass,mtail_"+ proc + "[" +tmH + "],sigL_"  + proc + "[" + tsigL  + "],sigR_"  + proc + "[" + tsigR  + "]);");
        ws.factory("SUM::pdf1_" + proc + "(r_"+ proc + "[" + tratio +"]*peakPdf1_" + proc + ",tailPdf1_" + proc + ")");
    }

TString fun=funcsetting(cname, proc, 2);
if (cname!="mmyy") test_mass = 91.19;
if (fun!="") func=fun;

if (DEBUG) cerr<<"begin 2nd pdf,"<<proc<<","<<func<<endl;

pdf = pdffit(cname, recMass, *d_v2, func);

    if ( func.Contains("cheb")  )
    {
        ws.factory("RooChebychev::pdf2_" + proc + "(recMass,{p0_2"+ proc + "[" + p0+ "],p1_2"+ proc + "[" + p1+ "],p2_2"+ proc + "[" + p2+ "],p3_2"+ proc + "[" + p3+ "],p4_2"+ proc + "[" + p4+ "]});");
    }
    else if ( func.Contains("keys")  || func.Contains("binned") )
    {
        pdf->SetNameTitle("pdf2_"+proc, "pdf2_"+proc);
        ws.import(*pdf);
    }
    else if ( func.Contains("exp2"))
    {
        ws.factory("EXPR::pdf2_" + proc + "('" + exps + "',recMass, p0_2" + proc + "[" + p0 + "], p1_2" + proc + "[" + p1 + "])");
    }
    else if ( func.Contains("Voigtian")  )
    {
        ws.factory("Voigtian::pdf2_" + proc + "(recMass, mH_2" + proc + "[" + p0 + "], width_2" + proc + "[" + p1 + "], sigma2_"+ proc +"["+ p2 +"])");
    }
    else if ( func.Contains("BifurGuassian") )
    {
        ws.factory("BifurGauss::pdf2_" + proc + "(recMass, mH_2" + proc + "[" + p0 + "], sigL_2" + proc + "[" + p1 + "], sigR_2"+ proc +"["+ p2 +"])");
    }
    else if ( func.Contains("CB") )
    {
        ws.factory("RooCBShape::peakPdf2_"    + proc + "(recMass,mH_2"   + proc + "[" +tmH + "],sigma2_" + proc + "[" + tsigma + "],Talpha2_"+ proc + "[" + tTalpha+ "],Tn_2"    + proc + "[" + tTn    + "]);");
        ws.factory("RooBifurGauss::tailPdf2_" + proc + "(recMass,mtail2_"+ proc + "[" +tmH + "],sigL2_"  + proc + "[" + tsigL  + "],sigR2_"  + proc + "[" + tsigR  + "]);");
        ws.factory("SUM::pdf2_" + proc + "(r_2"+ proc + "[" + tratio +"]*peakPdf2_" + proc + ",tailPdf2_" + proc + ")");
    }
    ws.factory("PROD:pdf_"+proc+"(pdf1_"+proc+", pdf2_"+proc+")");
}
    }    

    exps = "exp(@1*(@0-100)/100.0+@2*(@0-100)*(@0-100)/10000.0)";
    test_mass = 125.;       //reset configuration
    delete f;
    return ns;
}

RooAbsPdf* pdffit(TString cname, RooRealVar &var, RooDataSet &data, TString func)
{
    RooAbsPdf *pdf;
    RooFitResult *result_mu;
    // cerr<<"Now fitting: "<<func<<endl;
        
        Float_t Res_min=0.1;    //resolution
        Float_t Res_max=10;
        Float_t GaussWidthMax=8;
        if (cname.Contains("tt"))   Res_min=0.25;
        if (cname.Contains("qqtt")) Res_min=0.2;
        if (cname.Contains("eeqq_rec") ) Res_max=5;
        if (cname.Contains("vzmj")) GaussWidthMax=3;

        RooRealVar p0v("p0", "p0v", -0.1, -10, 10);
        RooRealVar p1v("p1", "p1v", -0.2, -10, 10);
        RooRealVar p2v("p2", "p2v", -0.1, -10, 10);
        RooRealVar p3v("p3", "p3v", -0.2, -10, 10);
        RooRealVar p4v("p4", "p4v", -0.1, -10, 10);
        RooRealVar mH    ("signal_mean",  "mean of Higgs", test_mass, test_mass - 5, test_mass + 5);
        RooRealVar width ("signal_width", "width of Higgs", 1, 0, 10); //voigitian
        RooRealVar sigma ("mRes",  "Resolution", 1, Res_min, Res_max);
        RooRealVar sigL  ("sigL", "sigTail_L", 3, 0.1, GaussWidthMax);
        RooRealVar sigR  ("sigR", "sigTail_R", 3, 0.1, GaussWidthMax);
        RooRealVar Talpha("tailAlpha", "tail alpha of Higgs", -1.50, -10, 10);
        RooRealVar Tn    ("tailN", "tail N of Higgs", 5., 0.1, 20);
        RooRealVar ratio ("ratio", "ratio", 0.9, 0.2, 1);

if ( func.Contains("cheb")  )
    {
        pdf = new RooChebychev("pdf", "pdf", var, RooArgSet( p0v, p1v, p2v, p3v, p4v));
        result_mu = Minimize(pdf,  data);
        p0=(TString)to_string(p0v.getVal());
        p1=(TString)to_string(p1v.getVal());
        p2=(TString)to_string(p2v.getVal());
        p3=(TString)to_string(p3v.getVal());
        p4=(TString)to_string(p4v.getVal());
    }
if ( func.Contains("exp2"))
    {
        pdf = new RooGenericPdf("pdf", "pdf", exps, RooArgSet(var, p0v, p1v));
        result_mu = Minimize(pdf,  data);
        if (result_mu->status()!=0) 
        {
            cout<<"turn to exp with 125"<<endl;
            exps="exp(@1*(@0-125)/125.0+@2*(@0-125)*(@0-125)/15625.0)";
            pdf = new RooGenericPdf("pdf", "pdf", exps, RooArgSet(invMass, p0v, p1v));
            
            result_mu = Minimize(pdf,  data);
        }
        if (result_mu->status()!=0) 
        {
            cout<<"turn to exp with 70"<<endl;
            exps="exp(@1*(@0-70)/125.0+@2*(@0-70)*(@0-70)/6400.0)";
            pdf = new RooGenericPdf("pdf", "pdf", exps, RooArgSet(invMass, p0v, p1v));
            result_mu = Minimize(pdf,  data);
        }
        if (result_mu->status()!=0) cerr<<"exp2 failed"<<endl;
            // cout << "Building a second order ploy exponential pdf " << endl;
        p0=(TString)to_string(p0v.getVal());
        p1=(TString)to_string(p1v.getVal());
        // ws.factory("EXPR::pdf_" + proc + "('" + exps + "',invMass, p0_1" + proc + "[" + p0 + "], p1_1" + proc + "[" + p1 + "])");
    }
if ( func.Contains("Voigtian")  )
    {
        pdf =new RooVoigtian("pdf", "pdf", var, mH, width, sigma);
        result_mu = Minimize(pdf,  data);
        p0=(TString)to_string(mH.getVal());
        p1=(TString)to_string(width.getVal());
        p2=(TString)to_string(sigma.getVal());
        // ws.factory("Voigtian::pdf_" + proc + "(invMass, mH_" + proc + "[" + p0 + "], width_" + proc + "[" + p1 + "], sigma_"+ proc +"["+ p2 +"])");
    }
if ( func.Contains("BifurGuassian") )
    {
        pdf =new RooBifurGauss("bifurPdf", "bifur", var, mH, sigL, sigR);
        result_mu = Minimize(pdf,  data);
        p0=(TString)to_string(mH.getVal());
        p1=(TString)to_string(sigL.getVal());
        p2=(TString)to_string(sigR.getVal());
        // ws.factory("BifurGauss::pdf_" + proc + "(invMass, mH_" + proc + "[" + p0 + "], sigL_" + proc + "[" + p1 + "], sigR_"+ proc +"["+ p2 +"])");
    }
if ( func.Contains("CB") )
    {
        
//gROOT->ProcessLine(".L /afs/ihep.ac.cn/users/z/zhangkl/wfs/workspace/src/RooGaussExp_cxx.so"); 
        RooCBShape    peakPdf("peakPdf", "peak", var, mH, sigma, Talpha, Tn);
        RooBifurGauss tailPdf("tailPdf", "tail", var, mH, sigL, sigR);
        pdf =new RooAddPdf("pdf", "pdf", RooArgList(peakPdf, tailPdf), ratio);
        // pdf =new RooGaussExp("pdf", "pdf", var, mH, sigma, Tn);
        result_mu = Minimize(pdf,  data);
 //       result_mu = Minimize(pdf,  data);
        
        if (DEBUG) result_mu->Print("v");

        // if (cname.Contains("eemm")||cname.Contains("qqmm")||cname.Contains("qqmm")||cname.Contains("vvmm")||cname.Contains("mcom")) 

        tmH    =(TString)to_string( mH    .getVal());
        tsigma =(TString)to_string( sigma .getVal());
        tTalpha=(TString)to_string( Talpha.getVal());
        tTn    =(TString)to_string( Tn    .getVal());
        tsigL  =(TString)to_string( sigL  .getVal());
        tsigR  =(TString)to_string( sigR  .getVal());
        tratio =(TString)to_string( ratio .getVal());
        if (cname.Contains("eemm")||cname.Contains("qqmm")||cname.Contains("qqmm")||cname.Contains("vvmm")||cname.Contains("mcom"))
        { 
            tsigma =(TString)to_string( sigma .getVal()*1.17);
            tsigL  =(TString)to_string( sigL  .getVal()*1.17);
            tsigR  =(TString)to_string( sigR  .getVal()*1.17);
        }
        // ws.factory("RooCBShape::peakPdf_"    + proc + "(invMass,mH_"   + proc + "[" +tmH + "],sigma_" + proc + "[" + tsigma + "],Talpha_"+ proc + "[" + tTalpha+ "],Tn_"    + proc + "[" + tTn    + "]);");
        // ws.factory("RooBifurGauss::tailPdf_" + proc + "(invMass,mtail_"+ proc + "[" +tmH + "],sigL_"  + proc + "[" + tsigL  + "],sigR_"  + proc + "[" + tsigR  + "]);");
        // ws.factory("SUM::pdf_" + proc + "(r_"+ proc + "[" + tratio +"]*peakPdf_" + proc + ",tailPdf_" + proc + ")");
    }
if ( func.Contains("GaussExp") )
    {
        // pdf =new RooGaussExp("pdf", "pdf", var, mH, sigma, Tn);
        result_mu = Minimize(pdf,  data);
 //       result_mu = Minimize(pdf,  data);
        
        if (DEBUG) result_mu->Print("v");

        // if (cname.Contains("eemm")||cname.Contains("qqmm")||cname.Contains("qqmm")||cname.Contains("vvmm")||cname.Contains("mcom")) 

        tmH    =(TString)to_string( mH    .getVal());
        tsigma =(TString)to_string( sigma .getVal());
        tTn    =(TString)to_string( Tn    .getVal());
        if (cname.Contains("eemm")||cname.Contains("qqmm")||cname.Contains("qqmm")||cname.Contains("vvmm")||cname.Contains("mcom"))
        { 
            tsigma =(TString)to_string( sigma .getVal()*1.17);
        }
    }
if ( func.Contains("keys")  || func.Contains("binned") )
    {
        Float_t rho=2;
        if (cname.Contains("imp")) 
              rho=2;        //qqtt不自然的样子 抹平
        if ((cname.Contains("qqqq")) ||(cname.Contains("vvqq")) || cname.Contains("yy") || (cname.Contains("w4q" )))
              rho=5;
        else if (cname.Contains("ezej") || cname.Contains("ezmj") 
               ||cname.Contains("vweq") || cname.Contains("vwmq") ||cname.Contains("vzej") || cname.Contains("vzmj")
          || cname=="vvtt" || cname=="qqtt"
          ||(cname.Contains("vvhbb" ))
          ||cname.Contains("ewevev")||cname.Contains("ewevmv")||cname.Contains("ewmvmv")||cname.Contains("mwevev")||cname.Contains("mwevmv")||cname.Contains("mwmvmv"))
              rho=3;
        pdf = new RooKeysPdf("pdf", "pdf", var, data, RooKeysPdf::MirrorAsymBoth, rho); // special for the Z peak
        // ws.import(*pdf);
    }
    return pdf;
}
RooFitResult* Minimize(RooAbsPdf *&pdf, RooDataSet &data)
{
  RooAbsReal *nll = pdf->createNLL(data, NumCPU(4), Offset(kTRUE) );
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




