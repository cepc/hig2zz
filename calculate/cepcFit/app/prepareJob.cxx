#include "inc/CommonHead.h"
#include "inc/RooFitHead.h"
#include "inc/RooStatsHead.h"

#include <boost/program_options.hpp>
#include "inc/auxUtils.h"

std::string _job = "";
std::string _channel = "";
std::string _poiStr = "";
std::string _mode = "";
int _nbin = 50;
bool _useMINOS = false;

int main( int argc, char** argv )
{
  namespace po = boost::program_options;
  po::options_description desc( "scanPlot options");
  desc.add_options()
    ( "job,j",       po::value<std::string>(&_job),  "Specify the type of job (REQUIRED)" )
    ( "channel,c",       po::value<std::string>(&_channel),  "Specify the channel to be studied (REQUIRED)" )
    ( "poi,p",         po::value<std::string>(&_poiStr),     "Specify POIs" )
    ( "bin,b",        po::value<int>(&_nbin)->default_value(_nbin),  "Set number of bins for scan" )
    ( "mode,m",       po::value<std::string>(&_mode)->default_value(_mode),  "Specify the mode to be studied" )
    ( "minos",         po::value<bool>(&_useMINOS)->default_value(_useMINOS), "Get asymmetric errors with MINOS fit" )
  ;

  po::variables_map vm;
  po::store( po::command_line_parser( argc, argv ).options( desc ).run(), vm );
  po::notify( vm );

  std::cout << "Usage: manager [options]\n";
  std::cout << desc;

  TString m_job = _job;
  TString m_mode = _mode;
  cout<<"Current job is "<<m_job<<endl;
  TString filename;
  filename = "outs/singleFit/singleFit_"+_channel+".root";

  TFile* f1 = new TFile(filename);
  RooFitResult* fitResult = (RooFitResult*) f1->Get("fitResult");

  vector<TString> name_poi;
  vector<double> rangelo1;
  vector<double> rangehi1;
  vector<double> rangelo2;
  vector<double> rangehi2;
  vector<double> rangelo3;
  vector<double> rangehi3;
  if ( vm.count("poi") ) {
    cout << endl << "Print parameters of interest in minos as [central, minus, plus]:" << endl <<endl;
    std::vector<std::string> poiStrs = auxUtils::Tokenize( _poiStr, "," );
    for( unsigned int ipoi(0); ipoi < poiStrs.size(); ipoi++ ) {
      std::vector<std::string> poiTerms = auxUtils::Tokenize( poiStrs[ipoi], "=" );
      double min_poi = -100, max_poi = 100;
      if (poiTerms.size() > 1) {
        std::vector<std::string> poiVals = auxUtils::Tokenize( poiTerms[1], "_" );
        if (poiVals.size() == 3) {
          min_poi = stof(poiVals[1]);
          max_poi = stof(poiVals[2]);
        }
      }
      TString poi_tmp = (TString) poiTerms[0];
      //cout<<"current poi is "<<poi_tmp<<endl;
      RooRealVar* par1_fitResult = (RooRealVar*) fitResult->floatParsFinal().find(poi_tmp);
      double central = par1_fitResult->getVal();
      double  errhi = par1_fitResult->getErrorHi();
      double  errlo = par1_fitResult->getErrorLo();
      if(_useMINOS) {
        cout<<"Set range with asymmetry error from minos"<<endl;
        errhi = par1_fitResult->getAsymErrorHi();
        errlo = par1_fitResult->getAsymErrorLo();
      }
      std::cout << std::fixed << std::showpoint;
      std::cout << std::setprecision(3);
      cout<<"\""<<poi_tmp<<"\": [ "<<central<<", "<<fabs(errlo)<<", "<<errhi<<" ],"<<endl;
      double stepsize = (errhi-errlo)*0.025;
      double rangelow_tmp2 = central+2*errlo;
      double rangehigh_tmp2 = central+2*errhi;
      double rangelow2 = rangelow_tmp2-10*stepsize;
      double rangehigh2 = rangehigh_tmp2+10*stepsize;
      if(rangelow2<min_poi) rangelow2 = min_poi;
      if(rangehigh2>max_poi) rangehigh2 = max_poi;
      name_poi.push_back(poi_tmp);
      rangelo2.push_back(rangelow2);
      rangehi2.push_back(rangehigh2);
      double rangelow3 = rangelow_tmp2-10*stepsize;
      double rangehigh3 = rangehigh_tmp2+30*stepsize;
      if(rangelow3<min_poi) rangelow3 = min_poi;
      if(rangehigh3>max_poi) rangehigh3 = max_poi;
      rangelo3.push_back(rangelow3);
      rangehi3.push_back(rangehigh3);
      double rangelow_tmp1 = central+1*errlo;
      double rangehigh_tmp1 = central+1*errhi;
      double rangelow1 = rangelow_tmp1-5*stepsize;
      double rangehigh1 = rangehigh_tmp1+5*stepsize;
      if(rangelow1<min_poi) rangelow1 = min_poi;
      if(rangehigh1>max_poi) rangehigh1 = max_poi;
      rangelo1.push_back(rangelow1);
      rangehi1.push_back(rangehigh1);
    }
  }

  if(m_job.Contains("nllScan")) {
    system("mkdir -vp outs/setups/"+m_job);
    TString name_output = Form("outs/setups/"+m_job+"/"+(TString)_channel+"_"+m_job+"_%dbin.sh", _nbin);
    cout<<"Print nll scan setting with "<<_nbin<<" bins to "<<name_output<<endl<<endl;;
    ofstream fout(name_output,ios::out);
    fout<<"### setups for "<<_channel<<" with nll scan in "<<_nbin<<" bins:"<<endl<<endl;
    fout<<"NBIN=\""<<_nbin<<"\""<<endl;
    fout<<"CHANNEL=\""<<_channel<<"\""<<endl;
    fout<<"POIS=\""<<_poiStr<<"\""<<endl;
    fout<<"PROFILES=( ";
    for(unsigned int i=0;i<name_poi.size();i++) fout<<"\""<<name_poi[i]<<"\" ";
    fout<<")"<<endl;
    fout << std::fixed << std::showpoint;
    fout << std::setprecision(3);
    if(_nbin==50) {
      fout<<"RANGELOW=( ";
      for(unsigned int i=0;i<rangelo1.size();i++) fout<<"\""<<rangelo1[i]<<"\" ";
      fout<<")"<<endl;
      fout<<"RANGEHIGH=( ";
      for(unsigned int i=0;i<rangehi1.size();i++) fout<<"\""<<rangehi1[i]<<"\" ";
      fout<<")"<<endl<<endl;
    }
    else if(_nbin==100) {
      fout<<"RANGELOW=( ";
      for(unsigned int i=0;i<rangelo2.size();i++) fout<<"\""<<rangelo2[i]<<"\" ";
      fout<<")"<<endl;
      fout<<"RANGEHIGH=( ";
      for(unsigned int i=0;i<rangehi2.size();i++) fout<<"\""<<rangehi2[i]<<"\" ";
      fout<<")"<<endl<<endl;
    }
    fout.close();
  }
  if(m_job.Contains("2DScan")) {
    system("mkdir -vp outs/setups/"+m_job);
    TString name_output = Form("outs/setups/"+m_job+"/"+(TString)_channel+"_"+m_job+"_%dbin.sh", _nbin);
    cout<<"Print 2D scan setting with "<<_nbin<<" bins to "<<name_output<<endl<<endl;;
    ofstream fout(name_output,ios::out);
    fout<<"### setups for "<<_channel<<" with nll scan in "<<_nbin<<" bins:"<<endl<<endl;
    fout<<"NBIN=\""<<_nbin<<"\""<<endl;
    fout<<"CHANNEL=\""<<_channel<<"\""<<endl;
    fout<<"POIS=\""<<_poiStr<<"\""<<endl;
    fout<<"PROFILES=( ";
    for(unsigned int i=0;i<name_poi.size();i++) fout<<"\""<<name_poi[i]<<"\" ";
    fout<<")"<<endl;
    fout << std::fixed << std::showpoint;
    fout << std::setprecision(3);
    if(_nbin==20) {
      fout<<"RANGELOW=( ";
      for(unsigned int i=0;i<rangelo1.size();i++) fout<<"\""<<rangelo1[i]<<"\" ";
      fout<<")"<<endl;
      fout<<"RANGEHIGH=( ";
      for(unsigned int i=0;i<rangehi1.size();i++) fout<<"\""<<rangehi1[i]<<"\" ";
      fout<<")"<<endl<<endl;
    }
    else if(_nbin==40) {
      fout<<"RANGELOW=( ";
      for(unsigned int i=0;i<rangelo2.size();i++) fout<<"\""<<rangelo2[i]<<"\" ";
      fout<<")"<<endl;
      fout<<"RANGEHIGH=( ";
      for(unsigned int i=0;i<rangehi2.size();i++) fout<<"\""<<rangehi2[i]<<"\" ";
      fout<<")"<<endl<<endl;
    }
    else if(_nbin==60) {
      fout<<"RANGELOW=( ";
      for(unsigned int i=0;i<rangelo3.size();i++) fout<<"\""<<rangelo3[i]<<"\" ";
      fout<<")"<<endl;
      fout<<"RANGEHIGH=( ";
      for(unsigned int i=0;i<rangehi3.size();i++) fout<<"\""<<rangehi3[i]<<"\" ";
      fout<<")"<<endl<<endl;
    }
    fout.close();
  }

  if(m_job.Contains("calSig")) {
    system("mkdir -vp outs/jobs/"+m_job+"/");
    TString name_output = Form("outs/jobs/"+m_job+"/"+m_job+"_"+(TString)_channel+"_%dbin.sh", _nbin);
    cout<<"Creat job scritps to plot NLL with "<<_nbin<<" bins as: "<<name_output<<endl<<endl;;
    ofstream fout(name_output,ios::out);
    fout<<"### plot NLL for "<<_channel<<" with "<<_nbin<<" bins:"<<endl<<endl;
    fout << std::fixed << std::showpoint;
    fout << std::setprecision(3);
    if(_nbin==50) {
      for(unsigned int i=0;i<name_poi.size();i++) fout<<"calSig "<<_channel<<" "<<name_poi[i]<<" "<<rangelo1[i]<<" "<<rangehi1[i]<<endl;
    }
    else if(_nbin==100) {
      for(unsigned int i=0;i<name_poi.size();i++) fout<<"calSig "<<_channel<<" "<<name_poi[i]<<" "<<rangelo2[i]<<" "<<rangehi2[i]<<endl;
    }
    fout.close();
  }

  if(m_job.Contains("plotNLL")) {
    system("mkdir -vp outs/jobs/"+m_job+"/");
    TString name_output = Form("outs/jobs/"+m_job+"/"+m_job+"_"+(TString)_channel+"_%dbin.sh", _nbin);
    cout<<"Creat job scritps to plot NLL with "<<_nbin<<" bins as: "<<name_output<<endl<<endl;;
    ofstream fout(name_output,ios::out);
    fout<<"### plot NLL for "<<_channel<<" with "<<_nbin<<" bins:"<<endl<<endl;
    fout << std::fixed << std::showpoint;
    fout << std::setprecision(3);
    if(_nbin==50) {
      for(unsigned int i=0;i<name_poi.size();i++) fout<<"plotnllscan "<<_channel<<" "<<name_poi[i]<<" "<<rangelo1[i]<<" "<<rangehi1[i]<<endl;
    }
    else if(_nbin==100) {
      for(unsigned int i=0;i<name_poi.size();i++) fout<<"plotnllscan "<<_channel<<" "<<name_poi[i]<<" "<<rangelo2[i]<<" "<<rangehi2[i]<<endl;
    }
    fout.close();
  }
  if(m_job.Contains("plotMultiNLL")) {
    system("mkdir -vp outs/jobs/"+m_job+"/");
    TString name_output = Form("outs/jobs/"+m_job+"/"+m_job+"_"+(TString)_channel+"_%dbin.sh", _nbin);
    cout<<"Creat job scritps to plot NLL with "<<_nbin<<" bins as: "<<name_output<<endl<<endl;;
    ofstream fout(name_output,ios::out);
    fout<<"### plot NLL for "<<_channel<<" with "<<_nbin<<" bins:"<<endl<<endl;
    fout << std::fixed << std::showpoint;
    fout << std::setprecision(3);
    if(_nbin==50) {
      for(unsigned int i=0;i<name_poi.size();i++) fout<<"plotmultiplenll "<<_channel<<" "<<name_poi[i]<<" "<<rangelo1[i]<<" "<<rangehi1[i]<<" "<<m_mode<<endl;
    }
    else if(_nbin==100) {
      for(unsigned int i=0;i<name_poi.size();i++) fout<<"plotmultiplenll "<<_channel<<" "<<name_poi[i]<<" "<<rangelo2[i]<<" "<<rangehi2[i]<<" "<<m_mode<<endl;
    }
    fout.close();
  }
  if(m_job.Contains("plot2D")) {
    system("mkdir -vp outs/jobs/"+m_job);
    TString name_output = Form("outs/jobs/"+m_job+"/"+m_job+"_"+(TString)_channel+"_%dbin.sh", _nbin);
    cout<<"Creat job scritps to plot 2D with "<<_nbin<<" bins as: "<<name_output<<endl<<endl;;
    ofstream fout(name_output,ios::out);
    fout << std::fixed << std::showpoint;
    fout << std::setprecision(3);
    fout<<"plotcontour "<<_channel<<" "<<name_poi[0]<<"="<<_nbin<<","<<name_poi[1]<<"="<<_nbin<<endl;
    fout.close();
  }
  if(m_job.Contains("errorSplit3")) {
    system("mkdir -vp outs/errors/"+m_job);
    TString name_output = Form("outs/errors/"+m_job+"/"+m_job+"_"+(TString)_channel+"_%dbin.txt", _nbin);
    cout<<"Print error array from likelihood scan for channel "<<_channel<<" with "<<m_job<<" in: "<<name_output<<endl<<endl;;

    ofstream fout(name_output,ios::out);
    fout << std::fixed << std::showpoint;
    fout << std::setprecision(3);
    fout<<"### error splitting for "<<m_job<<" with as: central total- total+ stat- stat+ exp- exp+ theory- theory+"<<endl<<endl;
    for(unsigned int i=0;i<name_poi.size();i++) {
      vector<double> split_central, split_errlo, split_errhi;
      TString input_tmp1 = "outs/plots/nllScan/"+(TString)_channel+"/nllScan_"+name_poi[i]+".txt";
      ifstream fi1;
      fi1.open(input_tmp1);
      string lineContent1;
      while(fi1.good() && !fi1.eof())
      {
        string lineContent_tmp;
        getline(fi1,lineContent_tmp);
        if(lineContent_tmp[0]=='#') continue;
        else if(lineContent_tmp=="") continue;
        else lineContent1=lineContent_tmp;
      }
      fi1.close();
      std::vector<std::string> errorStr1 = auxUtils::Tokenize( lineContent1, " " );
      double c_poi1, l_poi1, h_poi1;
      if (errorStr1.size() == 3) {
        c_poi1 = stof(errorStr1[0]);
        l_poi1 = stof(errorStr1[1]);
        h_poi1 = stof(errorStr1[2]);
      }
      split_central.push_back(c_poi1);
      split_errlo.push_back(l_poi1);
      split_errhi.push_back(h_poi1);

      TString input_tmp2 = "outs/plots/nllScan/"+(TString)_channel+"-Stat/nllScan_"+name_poi[i]+".txt";
      ifstream fi2;
      fi2.open(input_tmp2);
      string lineContent2;
      while(fi2.good() && !fi2.eof())
      {
        string lineContent_tmp;
        getline(fi2,lineContent_tmp);
        if(lineContent_tmp[0]=='#') continue;
        else if(lineContent_tmp=="") continue;
        else lineContent2=lineContent_tmp;
      }
      fi2.close();
      std::vector<std::string> errorStr2 = auxUtils::Tokenize( lineContent2, " " );
      double c_poi2, l_poi2, h_poi2;
      if (errorStr2.size() == 3) {
        c_poi2 = stof(errorStr2[0]);
        l_poi2 = stof(errorStr2[1]);
        h_poi2 = stof(errorStr2[2]);
      }
      split_central.push_back(c_poi2);
      split_errlo.push_back(l_poi2);
      split_errhi.push_back(h_poi2);

      TString input_tmp3 = "outs/plots/nllScan/"+(TString)_channel+"-noExp/nllScan_"+name_poi[i]+".txt";
      ifstream fi3;
      fi3.open(input_tmp3);
      string lineContent3;
      while(fi3.good() && !fi3.eof())
      {
        string lineContent_tmp;
        getline(fi3,lineContent_tmp);
        if(lineContent_tmp[0]=='#') continue;
        else if(lineContent_tmp=="") continue;
        else lineContent3=lineContent_tmp;
      }
      fi3.close();
      std::vector<std::string> errorStr3 = auxUtils::Tokenize( lineContent3, " " );
      double c_poi3, l_poi3, h_poi3;
      if (errorStr3.size() == 3) {
        c_poi3 = stof(errorStr3[0]);
        l_poi3 = stof(errorStr3[1]);
        h_poi3 = stof(errorStr3[2]);
      }
      split_central.push_back(c_poi3);
      split_errlo.push_back(l_poi3);
      split_errhi.push_back(h_poi3);

      TString input_tmp4 = "outs/plots/nllScan/"+(TString)_channel+"-noTheory/nllScan_"+name_poi[i]+".txt";
      ifstream fi4;
      fi4.open(input_tmp4);
      string lineContent4;
      while(fi4.good() && !fi4.eof())
      {
        string lineContent_tmp;
        getline(fi4,lineContent_tmp);
        if(lineContent_tmp[0]=='#') continue;
        else if(lineContent_tmp=="") continue;
        else lineContent4=lineContent_tmp;
      }
      fi4.close();
      std::vector<std::string> errorStr4 = auxUtils::Tokenize( lineContent4, " " );
      double c_poi4, l_poi4, h_poi4;
      if (errorStr4.size() == 3) {
        c_poi4 = stof(errorStr4[0]);
        l_poi4 = stof(errorStr4[1]);
        h_poi4 = stof(errorStr4[2]);
      }
      split_central.push_back(c_poi4);
      split_errlo.push_back(l_poi4);
      split_errhi.push_back(h_poi4);
      fout<<name_poi[i]<<" "<<split_central[0]<<" "<<split_errlo[0]<<" "<<split_errhi[0]<<" "<<split_errlo[1]<<" "<<split_errhi[1];
      for(unsigned int m_vi=2;m_vi<split_central.size();m_vi++) {
        fout<<" "<<sqrt(split_errlo[0]*split_errlo[0]-split_errlo[m_vi]*split_errlo[m_vi])<<" "<<sqrt(split_errhi[0]*split_errhi[0]-split_errhi[m_vi]*split_errhi[m_vi]);
      }
      fout<<" "<<endl;

//      fout << std::setprecision(2);
//      fout<<"#"<<name_poi[i]<<" = "<<split_central[0]<<"_{-"<<split_errlo[0]<<"}^{+"<<split_errhi[0]<<"}="<<split_central[0]<<"_{-"<<split_errlo[1]<<"}^{+"<<split_errhi[1]<<"} \\,  (stat.) \\, ";
//      fout<<"{}_{-"<<sqrt(split_errlo[0]*split_errlo[0]-split_errlo[2]*split_errlo[2])<<"}^{+"<<sqrt(split_errhi[0]*split_errhi[0]-split_errhi[2]*split_errhi[2])<<"} \\, (exp.) \\, ";
//      fout<<"{}_{-"<<sqrt(split_errlo[0]*split_errlo[0]-split_errlo[3]*split_errlo[3])<<"}^{+"<<sqrt(split_errhi[0]*split_errhi[0]-split_errhi[3]*split_errhi[3])<<"} \\, (theo.)"<<endl;
    }
    fout.close();
  }
  if(m_job.Contains("errorSplit2")) {
    system("mkdir -vp outs/errors/"+m_job);
    TString name_output = Form("outs/errors/"+m_job+"/"+m_job+"_"+(TString)_channel+"_%dbin.txt", _nbin);
    cout<<"Print error array from likelihood scan for channel "<<_channel<<" with "<<m_job<<" in: "<<name_output<<endl<<endl;;

    ofstream fout(name_output,ios::out);
    fout << std::fixed << std::showpoint;
    fout << std::setprecision(3);
    fout <<"### error splitting for "<<m_job<<" with as: central total- total+ stat- stat+ sys- sys+"<<endl<<endl;
    for(unsigned int i=0;i<name_poi.size();i++) {
      vector<double> split_central, split_errlo, split_errhi;
      TString input_tmp1 = "outs/plots/nllScan/"+(TString)_channel+"/nllScan_"+name_poi[i]+".txt";
      ifstream fi1;
      fi1.open(input_tmp1);
      string lineContent1;
      while(fi1.good() && !fi1.eof())
      {
        string lineContent_tmp;
        getline(fi1,lineContent_tmp);
        if(lineContent_tmp[0]=='#') continue;
        else if(lineContent_tmp=="") continue;
        else lineContent1=lineContent_tmp;
      }
      fi1.close();
      std::vector<std::string> errorStr1 = auxUtils::Tokenize( lineContent1, " " );
      double c_poi1, l_poi1, h_poi1;
      if (errorStr1.size() == 3) {
        c_poi1 = stof(errorStr1[0]);
        l_poi1 = stof(errorStr1[1]);
        h_poi1 = stof(errorStr1[2]);
      }
      split_central.push_back(c_poi1);
      split_errlo.push_back(l_poi1);
      split_errhi.push_back(h_poi1);

      TString input_tmp2 = "outs/plots/nllScan/"+(TString)_channel+"-Stat/nllScan_"+name_poi[i]+".txt";
      ifstream fi2;
      fi2.open(input_tmp2);
      string lineContent2;
      while(fi2.good() && !fi2.eof())
      {
        string lineContent_tmp;
        getline(fi2,lineContent_tmp);
        if(lineContent_tmp[0]=='#') continue;
        else if(lineContent_tmp=="") continue;
        else lineContent2=lineContent_tmp;
      }
      fi2.close();
      std::vector<std::string> errorStr2 = auxUtils::Tokenize( lineContent2, " " );
      double c_poi2, l_poi2, h_poi2;
      if (errorStr2.size() == 3) {
        c_poi2 = stof(errorStr2[0]);
        l_poi2 = stof(errorStr2[1]);
        h_poi2 = stof(errorStr2[2]);
      }
      split_central.push_back(c_poi2);
      split_errlo.push_back(l_poi2);
      split_errhi.push_back(h_poi2);

//      fout<<"\""<<name_poi[i]<<"\": [ "<<split_central[0]<<", "<<split_errlo[0]<<", "<<split_errhi[0]<<", "<<split_errlo[1]<<", "<<split_errhi[1];
//      fout<<", "<<sqrt(split_errlo[0]*split_errlo[0]-split_errlo[1]*split_errlo[1])<<", "<<sqrt(split_errhi[0]*split_errhi[0]-split_errhi[1]*split_errhi[1]);
//      fout<<" ]"<<endl;
      fout<<name_poi[i]<<" "<<split_central[0]<<" "<<split_errlo[0]<<" "<<split_errhi[0]<<" "<<split_errlo[1]<<" "<<split_errhi[1];
      fout<<" "<<sqrt(split_errlo[0]*split_errlo[0]-split_errlo[1]*split_errlo[1])<<" "<<sqrt(split_errhi[0]*split_errhi[0]-split_errhi[1]*split_errhi[1])<<" 0"<<endl;
    }
    fout.close();
  }
  if(m_job.Contains("errorNote")) {
    system("mkdir -vp outs/errors/"+m_job);
    TString name_output = Form("outs/errors/"+m_job+"/"+m_job+"_"+(TString)_channel+"_%dbin.txt", _nbin);
    cout<<"Print error array from likelihood scan for channel "<<_channel<<" with "<<m_job<<" in: "<<name_output<<endl<<endl;;

    ofstream fout(name_output,ios::out);
    fout << std::fixed << std::showpoint;
    fout << std::setprecision(2);
    fout <<"### error splitting for "<<m_job<<" with as: central total- total+ stat- stat+ exp- exp+ theory- theory+"<<endl<<endl;
    for(unsigned int i=0;i<name_poi.size();i++) {
      vector<double> split_central, split_errlo, split_errhi;
      TString input_tmp1 = "outs/plots/nllScan/"+(TString)_channel+"/nllScan_"+name_poi[i]+".txt";
      ifstream fi1;
      fi1.open(input_tmp1);
      string lineContent1;
      while(fi1.good() && !fi1.eof())
      {
        string lineContent_tmp;
        getline(fi1,lineContent_tmp);
        if(lineContent_tmp[0]=='#') continue;
        else if(lineContent_tmp=="") continue;
        else lineContent1=lineContent_tmp;
      }
      fi1.close();
      std::vector<std::string> errorStr1 = auxUtils::Tokenize( lineContent1, " " );
      double c_poi1, l_poi1, h_poi1;
      if (errorStr1.size() == 3) {
        c_poi1 = stof(errorStr1[0]);
        l_poi1 = stof(errorStr1[1]);
        h_poi1 = stof(errorStr1[2]);
      }
      split_central.push_back(c_poi1);
      split_errlo.push_back(l_poi1);
      split_errhi.push_back(h_poi1);
      TString m_channel = _channel;
      if(m_channel.Contains("Cg")||m_channel.Contains("CV")) {
        TString poiname = "";
        if(name_poi[i]=="CV") poiname = "\\kappa_{V}";
        if(name_poi[i]=="CF") poiname = "\\kappa_{f}";
        if(name_poi[i]=="Cg") poiname = "\\kappa_{g}";
        if(name_poi[i]=="Cy") poiname = "\\kappa_{\\gamma}";
        if(m_channel.Contains("MC")) poiname = poiname+"^{expected}";
        fout<<"$"<<poiname<<" = "<<split_central[0]<<"_{-"<<split_errlo[0]<<"}^{+"<<split_errhi[0]<<"}$"<<endl;
      }
      else {
        TString input_tmp2 = "outs/plots/nllScan/"+(TString)_channel+"-Stat/nllScan_"+name_poi[i]+".txt";
        ifstream fi2;
        fi2.open(input_tmp2);
        string lineContent2;
        while(fi2.good() && !fi2.eof())
        {
          string lineContent_tmp;
          getline(fi2,lineContent_tmp);
          if(lineContent_tmp[0]=='#') continue;
          else if(lineContent_tmp=="") continue;
          else lineContent2=lineContent_tmp;
        }
        fi2.close();
        std::vector<std::string> errorStr2 = auxUtils::Tokenize( lineContent2, " " );
        double c_poi2, l_poi2, h_poi2;
        if (errorStr2.size() == 3) {
          c_poi2 = stof(errorStr2[0]);
          l_poi2 = stof(errorStr2[1]);
          h_poi2 = stof(errorStr2[2]);
        }
        split_central.push_back(c_poi2);
        split_errlo.push_back(l_poi2);
        split_errhi.push_back(h_poi2);

        TString input_tmp3 = "outs/plots/nllScan/"+(TString)_channel+"-noExp/nllScan_"+name_poi[i]+".txt";
        ifstream fi3;
        fi3.open(input_tmp3);
        string lineContent3;
        while(fi3.good() && !fi3.eof())
        {
          string lineContent_tmp;
          getline(fi3,lineContent_tmp);
          if(lineContent_tmp[0]=='#') continue;
          else if(lineContent_tmp=="") continue;
          else lineContent3=lineContent_tmp;
        }
        fi3.close();
        std::vector<std::string> errorStr3 = auxUtils::Tokenize( lineContent3, " " );
        double c_poi3, l_poi3, h_poi3;
        if (errorStr3.size() == 3) {
          c_poi3 = stof(errorStr3[0]);
          l_poi3 = stof(errorStr3[1]);
          h_poi3 = stof(errorStr3[2]);
        }
        split_central.push_back(c_poi3);
        split_errlo.push_back(l_poi3);
        split_errhi.push_back(h_poi3);

        TString input_tmp4 = "outs/plots/nllScan/"+(TString)_channel+"-noTheory/nllScan_"+name_poi[i]+".txt";
        ifstream fi4;
        fi4.open(input_tmp4);
        string lineContent4;
        while(fi4.good() && !fi4.eof())
        {
          string lineContent_tmp;
          getline(fi4,lineContent_tmp);
          if(lineContent_tmp[0]=='#') continue;
          else if(lineContent_tmp=="") continue;
          else lineContent4=lineContent_tmp;
        }
        fi4.close();
        std::vector<std::string> errorStr4 = auxUtils::Tokenize( lineContent4, " " );
        double c_poi4, l_poi4, h_poi4;
        if (errorStr4.size() == 3) {
          c_poi4 = stof(errorStr4[0]);
          l_poi4 = stof(errorStr4[1]);
          h_poi4 = stof(errorStr4[2]);
        }
        split_central.push_back(c_poi4);
        split_errlo.push_back(l_poi4);
        split_errhi.push_back(h_poi4);
        TString poiname = "";
        if(name_poi[i]=="r_ggF") poiname = "\\sigma_{ggF}";
        if(name_poi[i]=="r_VBF") poiname = "\\sigma_{VBF}";
        if(name_poi[i]=="r_VH") poiname = "\\sigma_{VH}";
        if(name_poi[i]=="r_ttH") poiname = "\\sigma_{ttH}";
        if(name_poi[i]=="r_gg_H_ZZ") poiname = "\\sigma_{ggF} \\scale[0.5]{\\bullet} B_{4#it{l}}";
        if(name_poi[i]=="r_BR_yy_o_ZZ") poiname = "B_{\\gamma\\gamma}/B_{4#it{l}}";
        if(name_poi[i]=="vbf_o_ggf") poiname = "\\sigma_{VBF}/\\sigma_{ggF}";
        if(name_poi[i]=="vh_o_ggf") poiname = "\\sigma_{VH}/\\sigma_{ggF}";
        if(name_poi[i]=="tth_o_ggf") poiname = "\\sigma_{ttH}/\\sigma_{ggF}";
        if(name_poi[i]=="mu") poiname = "\\mu";
        if(name_poi[i]=="RgVh") poiname = "\\kappa_{gV}";
        if(name_poi[i]=="RVg") poiname = "\\lambda_{Vg}";
        if(name_poi[i]=="RyV") poiname = "\\lambda_{\\gammaV}";
        if(name_poi[i]=="RFg") poiname = "\\lambda_{fg}";
        if(m_channel.Contains("MC")) poiname = poiname+"^{expected}";
        fout<<"$"<<poiname<<" = "<<split_central[0]<<"_{-"<<split_errlo[0]<<"}^{+"<<split_errhi[0]<<"}="<<split_central[0]<<"_{-"<<split_errlo[1]<<"}^{+"<<split_errhi[1]<<"} \\,  (stat.) \\, ";
        fout<<"{}_{-"<<sqrt(split_errlo[0]*split_errlo[0]-split_errlo[2]*split_errlo[2])<<"}^{+"<<sqrt(split_errhi[0]*split_errhi[0]-split_errhi[2]*split_errhi[2])<<"} \\, (exp.) \\, ";
        fout<<"{}_{-"<<sqrt(split_errlo[0]*split_errlo[0]-split_errlo[3]*split_errlo[3])<<"}^{+"<<sqrt(split_errhi[0]*split_errhi[0]-split_errhi[3]*split_errhi[3])<<"} \\, (theo.)$"<<endl;
      }
    }
    fout.close();
  }
}
