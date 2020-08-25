#!/usr/bin/env bash

# Unset MARLIN_DLL
unset MARLIN_DLL

# Set Variables for MARLIN Execution
shopt -s expand_aliases
#source /besfs/groups/higgs/Software/v01-17-05_slc6/init_ilcsoft.sh
source $PWD/init_ilcsoft.sh

# FastJet
export MARLIN_DLL=$PWD/MarlinFastJet-00-02/lib/libMarlinFastJet.so:$MARLIN_DLL

# Add MARLIN Library Path 
export LD_LIBRARY_PATH=$PWD/lib:$LD_LIBRARY_PATH
export MARLIN_DLL=$PWD/lib/libHiggs2zz.so:$MARLIN_DLL

# For Condor Job Submit
export PATH=/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin:$PATH


# PyROOT 
export PYTHONPATH=$ROOTSYS/lib:$PYTHONPATH

# New environment
source /cvmfs/cepc.ihep.ac.cn/software/cepcenv/setup.sh
cepcenv -r /cvmfs/cepc.ihep.ac.cn/software/cepcsoft use 0.1.0-rc9

# Current settings
source /cvmfs/cepc.ihep.ac.cn/software/cepcenv/setup.sh
cepcenv -r /cvmfs/cepc.ihep.ac.cn/software/cepcsoft use 0.1.0-rc9 
source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.20.06/x86_64-centos7-gcc48-opt/bin/thisroot.sh
