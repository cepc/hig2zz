#!/usr/bin/env bash

# Main driver to submit jobs (BDT part) 
# Author Min Zhong <zmind@mail.ustc.edu.cn>
# Created [2019-11-17 Sun 15:00] 

usage() {
	printf "NAME\n\tsubmit.sh - Main driver to submit BDT training jobs\n"
	printf "\nSYNOPSIS\n"
	printf "\n\t%-5s\n" "./submit_train.sh [OPTION]" 
	printf "\nOPTIONS\n" 
        printf "\n\t%-9s  %-40s"  "1"      "[run Z(->ll)H(->ZZ*) channel]"
        printf "\n\t%-9s  %-40s"  "2"      "[run Z(->nn)H(->ZZ*) channel]"
        printf "\n\t%-9s  %-40s"  "3"      "[run Z(->qq)H(->ZZ*) channel]"
        printf "\n\n"
	printf "\nDATE\n"
	printf "\n\t%-5s\n" "November 2019" 
}

usage_1() {
        printf "\n\t%-9s  %-40s"  "1.1"      "[run Z(->mumu)H(->ZZ*->nnjj) channel]"
}

usage_2() {
        printf "\n\t%-9s  %-40s"  "2.1"      "[run Z(->nn)H(->ZZ*->mumujj) channel]"
}

usage_3() {
        printf "\n\t%-9s  %-40s"  "3.1"      "[run Z(->qq)H(->ZZ*->nnmumu) channel]"
}

usage_1_1() { 
	printf "\n\t%-9s  %-40s"  "1.1"      "[Run mumuHZZ sample]" 
	printf "\n\t%-9s  %-40s"  "1.1.1"    "Merge signal and background samples for training" 
	printf "\n\t%-9s  %-40s"  "1.1.2"    "BDT training" 
	printf "\n\t%-9s  %-40s"  "1.1.3"    "Add BDT score branch to root files (signal)" 
	printf "\n\t%-9s  %-40s"  "1.1.4"    "Merge zh root files (make it easier to add branch)" 
	printf "\n\t%-9s  %-40s"  "1.1.5"    "Add BDT score branch to root files (zh)" 
	printf "\n\t%-9s  %-40s"  "1.1.6"    "Merge bg root files (make it easier to add branch)" 
	printf "\n\t%-9s  %-40s"  "1.1.7"    "Add BDT score branch to root files (bg)" 	
}

usage_2_1() {  
        printf "\n\t%-9s  %-40s"  "2.1"      "[Run mumuHZZ sample]" 
        printf "\n\t%-9s  %-40s"  "2.1.1"    "Merge signal and background samples for training"
        printf "\n\t%-9s  %-40s"  "2.1.2"    "BDT training" 
        printf "\n\t%-9s  %-40s"  "2.1.3"    "Add BDT score branch to root files (signal)" 
        printf "\n\t%-9s  %-40s"  "2.1.4"    "Merge zh root files (make it easier to add branch)"
        printf "\n\t%-9s  %-40s"  "2.1.5"    "Add BDT score branch to root files (zh)"       
        printf "\n\t%-9s  %-40s"  "2.1.6"    "Merge bg root files (make it easier to add branch)"
        printf "\n\t%-9s  %-40s"  "2.1.7"    "Add BDT score branch to root files (bg)"        
}

usage_3_1() {  
        printf "\n\t%-9s  %-40s"  "3.1"      "[Run mumuHZZ sample]" 
        printf "\n\t%-9s  %-40s"  "3.1.1"    "Merge signal and background samples for training"
        printf "\n\t%-9s  %-40s"  "3.1.2"    "BDT training" 
        printf "\n\t%-9s  %-40s"  "3.1.3"    "Add BDT score branch to root files (signal)" 
        printf "\n\t%-9s  %-40s"  "3.1.4"    "Merge zh root files (make it easier to add branch)"
        printf "\n\t%-9s  %-40s"  "3.1.5"    "Add BDT score branch to root files (zh)"       
        printf "\n\t%-9s  %-40s"  "3.1.6"    "Merge bg root files (make it easier to add branch)"
        printf "\n\t%-9s  %-40s"  "3.1.7"    "Add BDT score branch to root files (bg)"        
}

if [[ $# -eq 0 ]]; then
    usage
    echo "Please enter your option: "
    read option
else
    option=$1    
fi

sel_signal=0
sel_zh=1
sel_bg=2
channel_opt_ll=2  #1 for hvvjj, 2 for hjjvv
channel_opt_nn=2  #1 for hmmjj, 2 for hjjmm
channel_opt_qq=2  #1 for hvvmm, 2 for hmmvv
llhzz=1
nnhzz=2
qqhzz=3

    # --------------------------------------------------------------------------
    #  1.1 mmHZZ   
    # --------------------------------------------------------------------------

sub_1_1(){
case $option in 

    1.1) echo "Running on mumuHZZ sample..."
         ;;

    1.1.1) echo "Merge signal and background samples for training..."
	   rm -rf ./bdt_results/channel_ll_${channel_opt_ll}
	   mkdir -p ./bdt_results/channel_ll_${channel_opt_ll}
	   cd ./sample/channel_ll_${channel_opt_ll}/Before/
	   hadd signal.root llh2zz/beforeBDT/*.root
	   hadd bkg_all.root zh/beforeBDT/*/*.root bg/beforeBDT/*/*.root
	   cd ../../../
           ;;

    1.1.2) echo "BDT training..."
	   ./train.py ${llhzz} ${channel_opt_ll} 
	   echo "Training Finished!"
	   mv output_importance.txt bdt_results/channel_ll_${channel_opt_ll}/
           ;;

    1.1.3) echo "Add BDT score branch to root files (signal)..."
	   rm -rf ./sample/channel_ll_${channel_opt_ll}/After/llh2zz/afterBDT
	   mkdir -p  ./sample/channel_ll_${channel_opt_ll}/After/llh2zz/afterBDT
	   cd ./sample/channel_ll_${channel_opt_ll}/Before/llh2zz/beforeBDT
	   for file in *
	   do
	     ../../../../../python/add_BDTscore.py  $file  ../../../After/llh2zz/afterBDT/$file ../../../../../bdt_results/channel_ll_${channel_opt_ll}/bdt_model.pkl ${llhzz}
	   done
	   cd ../../../../../
	   ;;

    1.1.4) echo "Merge zh root files (make it easier to add branch)..."
	   cd ./sample/channel_ll_${channel_opt_ll}/Before/zh/beforeBDT
	   rm ./*/*merge*
	   for dir in *
	   do
	     hadd ./$dir/ana_File_merged_1.root ./$dir/*.root
	   done
	   cd ../../../../../
           ;;

    1.1.5) echo "Add BDT score branch to root files (zh) ..."
	   rm -rf ./sample/channel_ll_${channel_opt_ll}/After/zh/afterBDT
	   mkdir -p   ./sample//channel_ll_${channel_opt_ll}/After/zh/afterBDT/
	   cd ./sample/channel_ll_${channel_opt_ll}/Before/zh/beforeBDT
	   for dir in *
	   do
	     mkdir -p ../../../After/zh/afterBDT/$dir
	   done
	   for dir in *
	   do
	     cd $dir
	     echo "          "
	     echo "working on" $dir "..."
	     ../../../../../../python/add_BDTscore.py ana_File_merged_1.root  ../../../../After/zh/afterBDT/$dir/ana_File_merged_1.root  ../../../../../../bdt_results/channel_ll_${channel_opt_ll}/bdt_model.pkl ${llhzz}
	     cd ../
	   done
	   cd ../../../../../
	   ;;

    1.1.6) echo "Merge bg root files (make it easier to add branch)..."
           cd ./sample/channel_ll_${channel_opt_ll}/Before/bg/beforeBDT
           rm ./*/*merge*
           for dir in *
           do
             hadd ./$dir/ana_File_merged_1.root ./$dir/*.root
           done
           cd ../../../../../
           ;;

    1.1.7) echo "Add BDT score branch to root files (bg) ..."
           rm -rf ./sample/channel_ll_${channel_opt_ll}/After/bg/afterBDT
           mkdir -p   ./sample//channel_ll_${channel_opt_ll}/After/bg/afterBDT/
           cd ./sample/channel_ll_${channel_opt_ll}/Before/bg/beforeBDT
           for dir in *
           do
             mkdir -p ../../../After/bg/afterBDT/$dir
           done
           for dir in *
           do
             cd $dir
	     echo "          "
	     echo "working on" $dir "..."
             ../../../../../../python/add_BDTscore.py ana_File_merged_1.root  ../../../../After/bg/afterBDT/$dir/ana_File_merged_1.root  ../../../../../../bdt_results/channel_ll_${channel_opt_ll}/bdt_model.pkl ${llhzz}
             cd ../
           done
           cd ../../../../../
           ;;

    esac
}

    # --------------------------------------------------------------------------
    #  2.1 nnHZZ   
    # --------------------------------------------------------------------------

sub_2_1(){
case $option in 

    2.1) echo "Running on nunuHZZ sample..."
         ;;

    2.1.1) echo "Merge signal and background samples for training..."
	   rm -rf ./bdt_results/channel_nn_${channel_opt_nn}
	   mkdir -p ./bdt_results/channel_nn_${channel_opt_nn}
	   cd ./sample/channel_nn_${channel_opt_nn}/Before/
	   hadd signal.root nnh2zz/beforeBDT/*.root
	   hadd bkg_all.root zh/beforeBDT/*/*.root bg/beforeBDT/*/*.root
	   cd ../../../
           ;;

    2.1.2) echo "BDT training"
	   ./train.py ${nnhzz} ${channel_opt_nn} 
	   echo "Training Finished!"
           mv output_importance.txt bdt_results/channel_nn_${channel_opt_nn}/
           ;;

    2.1.3) echo "Add BDT score branch to root files (signal)..."
	   rm -rf ./sample/channel_nn_${channel_opt_nn}/After/nnh2zz/afterBDT
	   mkdir -p  ./sample/channel_nn_${channel_opt_nn}/After/nnh2zz/afterBDT
	   cd ./sample/channel_nn_${channel_opt_nn}/Before/nnh2zz/beforeBDT
	   for file in *
	   do
	     ../../../../../python/add_BDTscore.py  $file  ../../../After/nnh2zz/afterBDT/$file ../../../../../bdt_results/channel_nn_${channel_opt_nn}/bdt_model.pkl ${nnhzz}
	   done
	   cd ../../../../../
	   ;;

    2.1.4) echo "Merge zh root files (make it easier to add branch)..."
	   cd ./sample/channel_nn_${channel_opt_nn}/Before/zh/beforeBDT
	   rm ./*/*merge*
	   for dir in *
	   do
	     hadd ./$dir/ana_File_merged_1.root ./$dir/*.root
	   done
	   cd ../../../../../
           ;;

    2.1.5) echo "Add BDT score branch to root files (zh) ..."
	   rm -rf ./sample/channel_nn_${channel_opt_nn}/After/zh/afterBDT
	   mkdir -p   ./sample//channel_nn_${channel_opt_nn}/After/zh/afterBDT/
	   cd ./sample/channel_nn_${channel_opt_nn}/Before/zh/beforeBDT
	   for dir in *
	   do
	     mkdir -p ../../../After/zh/afterBDT/$dir
	   done
	   for dir in *
	   do
	     cd $dir
	     echo "          "
	     echo "working on" $dir "..."
	     ../../../../../../python/add_BDTscore.py ana_File_merged_1.root  ../../../../After/zh/afterBDT/$dir/ana_File_merged_1.root  ../../../../../../bdt_results/channel_nn_${channel_opt_nn}/bdt_model.pkl ${nnhzz}
	     cd ../
	   done
	   cd ../../../../../
	   ;;

    2.1.6) echo "Merge bg root files (make it easier to add branch)..."
           cd ./sample/channel_nn_${channel_opt_nn}/Before/bg/beforeBDT
           rm ./*/*merge*
           for dir in *
           do
             hadd ./$dir/ana_File_merged_1.root ./$dir/*.root
           done
           cd ../../../../../
           ;;

    2.1.7) echo "Add BDT score branch to root files (bg) ..."
           rm -rf ./sample/channel_nn_${channel_opt_nn}/After/bg/afterBDT
           mkdir -p   ./sample//channel_nn_${channel_opt_nn}/After/bg/afterBDT/
           cd ./sample/channel_nn_${channel_opt_nn}/Before/bg/beforeBDT
           for dir in *
           do
             mkdir -p ../../../After/bg/afterBDT/$dir
           done
           for dir in *
           do
             cd $dir
	     echo "          "
	     echo "working on" $dir "..."
             ../../../../../../python/add_BDTscore.py ana_File_merged_1.root  ../../../../After/bg/afterBDT/$dir/ana_File_merged_1.root  ../../../../../../bdt_results/channel_nn_${channel_opt_nn}/bdt_model.pkl ${nnhzz}
             cd ../
           done
           cd ../../../../../
           ;;

    esac
}


    # --------------------------------------------------------------------------
    #  3.1 qqHZZ   
    # --------------------------------------------------------------------------

sub_3_1(){
case $option in 

    3.1) echo "Running on qqHZZ sample..."
         ;;

    3.1.1) echo "Merge signal and background samples for training..."
	   rm -rf ./bdt_results/channel_qq_${channel_opt_qq}
	   mkdir -p ./bdt_results/channel_qq_${channel_opt_qq}
	   cd ./sample/channel_qq_${channel_opt_qq}/Before/
	   hadd signal.root qqh2zz/beforeBDT/*.root
	   hadd bkg_all.root zh/beforeBDT/*/*.root bg/beforeBDT/*/*.root
	   cd ../../../
           ;;

    3.1.2) echo "BDT training"
	   ./train.py ${qqhzz} ${channel_opt_qq} 
	   echo "Training Finished!"
           mv output_importance.txt bdt_results/channel_qq_${channel_opt_qq}/
           ;;

    3.1.3) echo "Add BDT score branch to root files (signal)..."
	   rm -rf ./sample/channel_qq_${channel_opt_qq}/After/qqh2zz/afterBDT
	   mkdir -p  ./sample/channel_qq_${channel_opt_qq}/After/qqh2zz/afterBDT
	   cd ./sample/channel_qq_${channel_opt_qq}/Before/qqh2zz/beforeBDT
	   for file in *
	   do
	     ../../../../../python/add_BDTscore.py  $file  ../../../After/qqh2zz/afterBDT/$file ../../../../../bdt_results/channel_qq_${channel_opt_qq}/bdt_model.pkl ${qqhzz}
	   done
	   cd ../../../../../
	   ;;

    3.1.4) echo "Merge zh root files (make it easier to add branch)..."
	   cd ./sample/channel_qq_${channel_opt_qq}/Before/zh/beforeBDT
	   rm ./*/*merge*
	   for dir in *
	   do
	     hadd ./$dir/ana_File_merged_1.root ./$dir/*.root
	   done
	   cd ../../../../../
           ;;

    3.1.5) echo "Add BDT score branch to root files (zh) ..."
	   rm -rf ./sample/channel_qq_${channel_opt_qq}/After/zh/afterBDT
	   mkdir -p   ./sample//channel_qq_${channel_opt_qq}/After/zh/afterBDT/
	   cd ./sample/channel_qq_${channel_opt_qq}/Before/zh/beforeBDT
	   for dir in *
	   do
	     mkdir -p ../../../After/zh/afterBDT/$dir
	   done
	   for dir in *
	   do
	     cd $dir
	     echo "          "
	     echo "working on" $dir "..."
	     ../../../../../../python/add_BDTscore.py ana_File_merged_1.root  ../../../../After/zh/afterBDT/$dir/ana_File_merged_1.root  ../../../../../../bdt_results/channel_qq_${channel_opt_qq}/bdt_model.pkl ${qqhzz}
	     cd ../
	   done
	   cd ../../../../../
	   ;;

    3.1.6) echo "Merge bg root files (make it easier to add branch)..."
           cd ./sample/channel_qq_${channel_opt_qq}/Before/bg/beforeBDT
           rm ./*/*merge*
           for dir in *
           do
             hadd ./$dir/ana_File_merged_1.root ./$dir/*.root
           done
           cd ../../../../../
           ;;

    3.1.7) echo "Add BDT score branch to root files (bg) ..."
           rm -rf ./sample/channel_qq_${channel_opt_qq}/After/bg/afterBDT
           mkdir -p   ./sample//channel_qq_${channel_opt_qq}/After/bg/afterBDT/
           cd ./sample/channel_qq_${channel_opt_qq}/Before/bg/beforeBDT
           for dir in *
           do
             mkdir -p ../../../After/bg/afterBDT/$dir
           done
           for dir in *
           do
             cd $dir
	     echo "          "
	     echo "working on" $dir "..."
             ../../../../../../python/add_BDTscore.py ana_File_merged_1.root  ../../../../After/bg/afterBDT/$dir/ana_File_merged_1.root  ../../../../../../bdt_results/channel_qq_${channel_opt_qq}/bdt_model.pkl ${qqhzz}
             cd ../
           done
           cd ../../../../../
           ;;

    esac
}

sub_1(){
case $option in 
# sample: 1.1 is print detail information about each step and then you can run the step you want.
#         1.1.* is directly running the step. 
    # --------------------------------------------------------------------------
    #  Data  
    # --------------------------------------------------------------------------

    1.1) echo "run mmHZZ (BDT training part)"
        usage_1_1
        echo "Please enter your option: " 
        read option 
        sub_1_1 option 
        ;;
    1.1.*) echo "run mmHZZ (BDT training part)"
        sub_1_1 option
        ;;
esac
}

sub_2(){
case $option in

    2.1) echo "run nnHZZ (BDT training part)"
        usage_2_1
        echo "Please enter your option: " 
        read option
        sub_2_1 option
        ;;
    2.1.*) echo "run nnHZZ (BDT training part)"
        sub_2_1 option
        ;;
esac
}

sub_3(){
case $option in

    3.1) echo "run qqHZZ (BDT training part)"
        usage_3_1
        echo "Please enter your option: " 
        read option
        sub_3_1 option
        ;;
    3.1.*) echo "run qqHZZ (BDT training part)"
        sub_3_1 option
        ;;
esac
}

case $option in
    1) echo "run mumuHzz"
       usage_1
       echo "Please enter your option: "
       read option
       sub_1 option
        ;;
    1.*) echo "run mumuHzz"
       sub_1 option
        ;;

    2) echo "run nnHzz"
       usage_2
       echo "Please enter your option: "
       read option
       sub_2 option
        ;;
    2.*) echo "run nnHzz"
       sub_2 option
        ;;

    3) echo "run qqHzz"
       usage_3
       echo "Please enter your option: "
       read option
       sub_3 option
        ;;
    3.*) echo "run qqHzz"
       sub_3 option
        ;;
esac
