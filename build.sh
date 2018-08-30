#!/usr/bin/env bash 

# FastJet

cd ./MarlinFastJet-00-02
rm -fr build
mkdir build
cd build
cmake -C ../ILCSoft.cmake ..
make install 
cd ../../


# Higgs2zz

rm -fr build
mkdir build
cd build
cmake -C /afs/ihep.ac.cn/soft/common/gcc/v01-17-05/ILCSoft.cmake .. 
make install
cd ..

