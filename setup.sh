#!/usr/bin/env bash

# Unset MARLIN_DLL
unset MARLIN_DLL

# Set Variables for MARLIN Execution
shopt -s expand_aliases
#source /besfs/groups/higgs/Software/v01-17-05_slc6/init_ilcsoft.sh
#source $PWD/init_ilcsoft.sh

source /cvmfs/cepc.ihep.ac.cn/software/cepcenv/setup.sh
cepcenv -r /cvmfs/cepc.ihep.ac.cn/software/cepcsoft use 0.1.0-rc9

# Unset MARLIN_DLL again.  MARIN_DLL is set during above initilization. 
# To set user specific DLL setting, unset once.
unset MARLIN_DLL

# Following is copy&paste after above initilization without "unset MARLIN_DLL" 
# But, removing MarlinFastjet DLL ( /cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/HighLevelObjectFinding/Jets/MarlinFastJet/00-02/lib/libMarlinFastJet.so )
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/Tracking/MarlinTrkProcessors/01-10/lib/libMarlinTrkProcessors.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/Tracking/ForwardTracking/01-07/lib/libForwardTracking.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/Tracking/Clupatra/00-10/lib/libClupatra.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Analysis/SubDetectorStudy/TPC/MarlinTPC/00-16/lib/libMarlinTPC.so

# LCFIPlus ... which causes a core dump at the end of run. Not sure exactly what happens.  
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/HighLevelObjectFinding/Jets/LCFIPlus/00-05-02/lib/libLCFIPlus.so
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/HighLevelObjectFinding/Jets/LCFIPlus/00-05-02/lib/libLCFIPlus.so

export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/PFA/Pandora/MarlinPandora/00-11/lib/libMarlinPandora.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/HighLevelObjectFinding/Jets/FastJetClustering/00-02/lib/libFastJetClustering.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/PFA/Garlic/2.10.1/lib/libGarlic.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/HighLevelObjectFinding/Jets/LCFIVertex/00-06-01/lib/libLCFIVertex.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/Digitization/MarlinReco/01-09/lib/libMarlinReco.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/EventDisplay/CEDViewer/01-07-02/lib/libCEDViewer.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/PFA/Pandora/PandoraAnalysis/00-05/lib/libPandoraAnalysis.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Analysis/Overlay/00-13/lib/libOverlay.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/PFA/Arbor/3.4.1/lib/libRanger.so
export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-centos7-gcc49/cepcsoft/0.1.0-rc9/Framework/LCTuple/01-03/lib/libLCTuple.so

#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/Tracking/MarlinTrkProcessors/01-10/lib/libMarlinTrkProcessors.so
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/Tracking/ForwardTracking/01-07/lib/libForwardTracking.so
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/Tracking/Clupatra/00-10/lib/libClupatra.so
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Analysis/SubDetectorStudy/TPC/MarlinTPC/00-16/lib/libMarlinTPC.so
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/PFA/Pandora/MarlinPandora/00-11/lib/libMarlinPandora.so:
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/PFA/Garlic/2.10.1/lib/libGarlic.so
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/HighLevelObjectFinding/Jets/LCFIVertex/00-06-01/lib/libLCFIVertex.so
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/Digitization/MarlinReco/01-09/lib/libMarlinReco.so
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/EventDisplay/CEDViewer/01-07-02/lib/libCEDViewer.so
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/PFA/Pandora/PandoraAnalysis/00-05/lib/libPandoraAnalysis.so
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Analysis/Overlay/00-13/lib/libOverlay.so
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Reconstruction/PFA/Arbor/3.4.1/lib/libRanger.so:
#export MARLIN_DLL=${MARLIN_DLL}:/cvmfs/cepc.ihep.ac.cn/software/cepcsoft/x86_64-sl6-gcc49/cepcsoft/0.1.0-rc9/Framework/LCTuple/01-03/lib/libLCTuple.so

# FastJet
export MARLIN_DLL=$PWD/MarlinFastJet-00-02/lib/libMarlinFastJet.so:$MARLIN_DLL

# Add MARLIN Library Path 
export LD_LIBRARY_PATH=$PWD/lib:$LD_LIBRARY_PATH
export MARLIN_DLL=$PWD/lib/libHiggs2zz.so:$MARLIN_DLL

# For Condor Job Submit
export PATH=/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin:$PATH


# PyROOT 
export PYTHONPATH=$ROOTSYS/lib:$PYTHONPATH
