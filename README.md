# Higgs2ZZ

Higgs to ZZ* analysis 

## Note

- Server : SLC6 ( lxslc6.ihep.ac.cn ).  It does not work under the SLC5 (lxslc5.ihep.ac.cn) environment.

- Since the batch job system (HTCondor) requests the output directory not be located under /afs ,
you need to make sure this point. Especially, a "run" directory is going to be created during the procedure (submit.sh) 
and all of output files are stored in, therefore, the PATH of "run" directory should be taken care.  


## 1. Install  

> ssh -X lxslc6.ihep.ac.cn

> cd {some directory under which you want to setup the code}

> git clone https://github.com/cepc/hig2zz.git

> cd hig2zz


## 2. Setup 

> source setup.sh


## 3. Build code

> ./build.sh 


## 4. Submit jobs

> ./submit.sh


## Some styles to follow 

- Minimize the number of main c++ files

- Keep functions length less than one screen

- Seperate hard-coded cuts into script file

- Use pull-request mode on git

- Document well the high-level bash file for work flow
