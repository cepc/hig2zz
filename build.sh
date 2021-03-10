#!/usr/bin/env bash 

# MarlinFastJet

cd ./MarlinFastJet-00-02
rm -fr build
mkdir build
cd build
cmake ../
make install 
cd ../../


# IsolatedLeptonFinder && Higgs2zz

rm -fr build
mkdir build
cd build
cmake ../
make install
cd ..

