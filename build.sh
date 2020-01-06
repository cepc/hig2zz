#!/usr/bin/env bash 

# MarlinFastJet

cd ./MarlinFastJet-00-02
rm -fr build
mkdir build
cd build
#cmake -C ../ILCSoft.cmake ..
cmake -C ../ILCSoft.cmake.mod ..
make install 
cd ../../


# IsolatedLepton && Higgs2zz

rm -fr build
mkdir build
cd build
#cmake -C /afs/ihep.ac.cn/soft/common/gcc/v01-17-05/ILCSoft.cmake .. 
cmake -C /cefs/higgs/kiuchi/Higgs2zz/Emergency_Copied_Marlin/ILCSoft.cmake ..
make install
cd ..

