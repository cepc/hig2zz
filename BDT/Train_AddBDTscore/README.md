# H->ZZ Analysis, BDT Training part

## Environment Requirements
* Since we are using siki-learn (machine learning package in python) instead of traditional TMVA to do the BDT part in the analysis, the environment requirements are listed below:
  - python 3
  - ROOT 6
  - sklearn 
  - pandas
  - matplotlib

* Anaconda is recommended to set up the environment needed to run the code.
* If error message like "no module named XXX" shows, the simplest way to solve it is to install it by conda:
  - conda install XXX
  or
  - conda install -c conda-forge XXX

## Demonstration about the code stucture
This part of code (under Train_AddBDTscore/ folder) is used to do the BDT training.

To be more specific, this part contains 3 steps for each channel:
1. Merge signal and background rootfile seperately to get the two root files as training input.  
   Related part in submit_train.sh: 1.1.1, 2.1.1, 3.1.1
2. BDT training (main program: train.py), get the output ROC Curve, BDT score distribution (unnormalized), and BDT model (pkl file).
   Related part in submit_train.sh: 1.1.2, 2.1.2, 3.1.2
3. Add a Branch named "BDT_score" to all the ntuples (main program: ./python/add_BDTscore.py), so that we can apply BDT score cut in the following analysis.
   Related part in submit_train.sh: 1.1.3~1.1.7, 2.1.3~2.1.7, 3.1.3~3.1.7

## How to run
* ./submit_train.sh

## Author Info
*  Min Zhong <zmind@mail.ustc.edu.cn>
   University of Science and Technology of China
   Created on Dec. 17, 2019
