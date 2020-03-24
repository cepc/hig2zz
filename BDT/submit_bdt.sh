#!/usr/bin/env bash

# Main driver to submit jobs 
# Author: Min Zhong <zmind@mails.ustc.edu.cn>
# Created [2019-12-18 Sat 15:08] 

usage() {
	printf "NAME\n\tsubmit_bdt.sh - Main driver to submit BDT jobs\n"
	printf "\nSYNOPSIS\n"
	printf "\n\t%-5s\n" "./submit_bdt.sh [OPTION]" 
	printf "\n\start event_sel in *.1.5 *.2.5 *.3.5\n" 
	printf "\nOPTIONS\n" 
        printf "\n\t%-9s  %-40s"  "1"      "[run Z(->ll)H(->ZZ*) channel]"
        printf "\n\t%-9s  %-40s"  "2"      "[run Z(->nn)H(->ZZ*) channel]"
        printf "\n\t%-9s  %-40s"  "3"      "[run Z(->qq)H(->ZZ*) channel]"
        printf "\n\n"
	printf "\nDATE\n"
	printf "\n\t%-5s\n" "December 2019" 
}

usage_1() {
        printf "\n\t%-9s  %-40s"  "1.1"      "[run Z(->mumu)H(->ZZ*->nnjj) sample]"
        printf "\n\t%-9s  %-40s"  "1.2"      "[run Z(->ll,qq,nn)H(->inclusive) background sample]"
        printf "\n\t%-9s  %-40s"  "1.3"      "[run background sample]"
        printf "\n\t%-9s  %-40s"  "1.4"      "[plot pictures and save results]"
}

usage_2() {
        printf "\n\t%-9s  %-40s"  "2.1"      "[run Z(->nn)H(->ZZ*->mumujj) sample]"
        printf "\n\t%-9s  %-40s"  "2.2"      "[run Z(->ll,qq,nn)H(->inclusive) background sample]"
        printf "\n\t%-9s  %-40s"  "2.3"      "[run background sample]"
        printf "\n\t%-9s  %-40s"  "2.4"      "[plot pictures and save results]"
}

usage_3() {
        printf "\n\t%-9s  %-40s"  "3.1"      "[run Z(->qq)H(->ZZ*->nnmumu) sample]"
        printf "\n\t%-9s  %-40s"  "3.2"      "[run Z(->ll,qq,nn)H(->inclusive) background sample]"
        printf "\n\t%-9s  %-40s"  "3.3"      "[run background sample]"
        printf "\n\t%-9s  %-40s"  "3.4"      "[plot pictures and save results]"
}

usage_1_1() { 
	printf "\n\t%-9s  %-40s"  "1.1"      "[run signal sample]" 
	printf "\n\t%-9s  %-40s"  "1.1.1"    "Copy signal samples from cut-based framework" 
	printf "\n\t%-9s  %-40s"  "1.1.2"    "Make several cuts before BDT" 
	printf "\n\t%-9s  %-40s"  "1.1.3"    "Copy the signal samples to another environment with sklearn, python3 and ROOT6" 
	printf "\n\t%-9s  %-40s"  "1.1.4"    "Copy the signal sample added with BDT score branch back" 
	printf "\n\t%-9s  %-40s"  "1.1.5"    "Select events on signal" 
	printf "\n\t%-9s  %-40s"  "1.1.6"    "Merge signal event root files" 
}

usage_2_1() {
        printf "\n\t%-9s  %-40s"  "2.1"      "[run signal sample]"
        printf "\n\t%-9s  %-40s"  "2.1.1"    "Copy signal samples from cut-based framework"
        printf "\n\t%-9s  %-40s"  "2.1.2"    "Make several cuts before BDT"
        printf "\n\t%-9s  %-40s"  "2.1.3"    "Copy the signal samples to another environment with sklearn, python3 and ROOT6"       
        printf "\n\t%-9s  %-40s"  "2.1.4"    "Copy the signal sample added with BDT score branch back"         
        printf "\n\t%-9s  %-40s"  "2.1.5"    "Select events on signal" 
        printf "\n\t%-9s  %-40s"  "2.1.6"    "Merge signal event root files"
}

usage_3_1() {
        printf "\n\t%-9s  %-40s"  "3.1"      "[run signal sample]"
        printf "\n\t%-9s  %-40s"  "3.1.1"    "Copy signal samples from cut-based framework"
        printf "\n\t%-9s  %-40s"  "3.1.2"    "Make several cuts before BDT"
        printf "\n\t%-9s  %-40s"  "3.1.3"    "Copy the signal samples to another environment with sklearn, python3 and ROOT6"
        printf "\n\t%-9s  %-40s"  "3.1.4"    "Copy the signal sample added with BDT score branch back"
        printf "\n\t%-9s  %-40s"  "3.1.5"    "Select events on signal"
        printf "\n\t%-9s  %-40s"  "3.1.6"    "Merge signal event root files"
}

usage_1_2() { 
	printf "\n\t%-9s  %-40s"  "1.2"      "[run Z(->ll,qq,nn)H(->inclusive) sample]" 
	printf "\n\t%-9s  %-40s"  "1.2.1"    "Copy zh samples from cut-based framework" 
	printf "\n\t%-9s  %-40s"  "1.2.2"    "Make several cuts before BDT" 
	printf "\n\t%-9s  %-40s"  "1.2.3"    "Copy the zh samples to another environment with sklearn, python3 and ROOT6" 
	printf "\n\t%-9s  %-40s"  "1.2.4"    "Copy the zh sample added with BDT score branch back" 
	printf "\n\t%-9s  %-40s"  "1.2.5"    "Select events on zh" 
	printf "\n\t%-9s  %-40s"  "1.2.6"    "Merge zh event root files" 
}

usage_2_2() {
        printf "\n\t%-9s  %-40s"  "2.2"      "[run Z(->ll,qq,nn)H(->inclusive) sample]"
        printf "\n\t%-9s  %-40s"  "2.2.1"    "Copy zh samples from cut-based framework"     
        printf "\n\t%-9s  %-40s"  "2.2.2"    "Make several cuts before BDT" 
        printf "\n\t%-9s  %-40s"  "2.2.3"    "Copy the zh samples to another environment with sklearn, python3 and ROOT6"    
        printf "\n\t%-9s  %-40s"  "2.2.4"    "Copy the zh sample added with BDT score branch back"    
        printf "\n\t%-9s  %-40s"  "2.2.5"    "Select events on zh"    
        printf "\n\t%-9s  %-40s"  "2.2.6"    "Merge zh event root files"    
}

usage_3_2() {
        printf "\n\t%-9s  %-40s"  "3.2"      "[run Z(->ll,qq,nn)H(->inclusive) sample]"
        printf "\n\t%-9s  %-40s"  "3.2.1"    "Copy zh samples from cut-based framework"     
        printf "\n\t%-9s  %-40s"  "3.2.2"    "Make several cuts before BDT" 
        printf "\n\t%-9s  %-40s"  "3.2.3"    "Copy the zh samples to another environment with sklearn, python3 and ROOT6"    
        printf "\n\t%-9s  %-40s"  "3.2.4"    "Copy the zh sample added with BDT score branch back"    
        printf "\n\t%-9s  %-40s"  "3.2.5"    "Select events on zh"    
        printf "\n\t%-9s  %-40s"  "3.2.6"    "Merge zh event root files"    
}

usage_1_3() {
        printf "\n\t%-9s  %-40s"  "1.3"      "[run background sample]"
        printf "\n\t%-9s  %-40s"  "1.3.1"    "Copy bg samples from cut-based framework"     
        printf "\n\t%-9s  %-40s"  "1.3.2"    "Make several cuts before BDT" 
        printf "\n\t%-9s  %-40s"  "1.3.3"    "Copy the bg samples to another environment with sklearn, python3 and ROOT6"    
        printf "\n\t%-9s  %-40s"  "1.3.4"    "Copy the bg sample added with BDT score branch back"    
        printf "\n\t%-9s  %-40s"  "1.3.5"    "Select events on bg"    
        printf "\n\t%-9s  %-40s"  "1.3.6"    "Merge bg event root files"    
}

usage_2_3() {
        printf "\n\t%-9s  %-40s"  "2.3"      "[run background sample]"
        printf "\n\t%-9s  %-40s"  "2.3.1"    "Copy bg samples from cut-based framework"
        printf "\n\t%-9s  %-40s"  "2.3.2"    "Make several cuts before BDT"
        printf "\n\t%-9s  %-40s"  "2.3.3"    "Copy the bg samples to another environment with sklearn, python3 and ROOT6"
        printf "\n\t%-9s  %-40s"  "2.3.4"    "Copy the bg sample added with BDT score branch back"
        printf "\n\t%-9s  %-40s"  "2.3.5"    "Select events on bg"
        printf "\n\t%-9s  %-40s"  "2.3.6"    "Merge bg event root files"
}

usage_3_3() {
        printf "\n\t%-9s  %-40s"  "3.3"      "[run background sample]"
        printf "\n\t%-9s  %-40s"  "3.3.1"    "Copy bg samples from cut-based framework"
        printf "\n\t%-9s  %-40s"  "3.3.2"    "Make several cuts before BDT"
        printf "\n\t%-9s  %-40s"  "3.3.3"    "Copy the bg samples to another environment with sklearn, python3 and ROOT6"
        printf "\n\t%-9s  %-40s"  "3.3.4"    "Copy the bg sample added with BDT score branch back"
        printf "\n\t%-9s  %-40s"  "3.3.5"    "Select events on bg"
        printf "\n\t%-9s  %-40s"  "3.3.6"    "Merge bg event root files"
}

usage_1_4() { 
	printf "\n" 
	printf "\n\t%-9s  %-40s"  "1.4"      "[plot pictures and save results]" 
	printf "\n\t%-9s  %-40s"  "1.4.1"    "Plot S/√(S+B) versus BDT score cut histogram" 
        printf "\n\t%-9s  %-40s"  "1.4.2"    "Plot signal-bg histograms" 
	printf "\n\t%-9s  %-40s"  "1.4.3"    "Plot information" 
	printf "\n\t%-9s  %-40s"  "1.4.4"    "Generate tables and LaTex tables"
	printf "\n\t%-9s  %-40s"  "1.4.5"    "Save results" 
}

usage_2_4() {  
        printf "\n"
        printf "\n\t%-9s  %-40s"  "2.4"      "[plot pictures and save results]"
        printf "\n\t%-9s  %-40s"  "2.4.1"    "Plot S/√(S+B) versus BDT score cut histogram"
        printf "\n\t%-9s  %-40s"  "2.4.2"    "Plot signal-bg histograms"          
        printf "\n\t%-9s  %-40s"  "2.4.3"    "Plot information" 
        printf "\n\t%-9s  %-40s"  "2.4.4"    "Generate tables and LaTex tables"
        printf "\n\t%-9s  %-40s"  "2.4.5"    "Save results" 
}

usage_3_4() {
        printf "\n"
	printf "\n\t%-9s  %-40s"  "3.4"      "[plot pictures and save results]"
	printf "\n\t%-9s  %-40s"  "3.4.1"    "Plot S/√(S+B) versus BDT score cut histogram"
	printf "\n\t%-9s  %-40s"  "3.4.2"    "Plot signal-bg histograms" 
        printf "\n\t%-9s  %-40s"  "3.4.3"    "Plot information"
        printf "\n\t%-9s  %-40s"  "3.4.4"    "Generate tables and LaTex tables"
        printf "\n\t%-9s  %-40s"  "3.4.5"    "Save results" 
        printf "\n\t%-9s  %-40s"  "3.4.6"    "fit results"
        printf "\n\t%-9s  %-40s"  "3.4.7"    "combined fitting"
}

if [[ $# -eq 0 ]]; then
    usage
    echo "Please enter your option: "
    read option
else
    option=$1    
fi

signal_slcio_dir_ll=/cefs/data/DstData/CEPC240/CEPC_v4/higgs/E240.Pe2e2h_zz.e0.p0.whizard195

signal_slcio_dir_nn=/cefs/data/DstData/CEPC240/CEPC_v4/higgs/E240.Pnnh_zz.e0.p0.whizard195

signal_slcio_dir_qq=/cefs/data/DstData/CEPC240/CEPC_v4/higgs/E240.Pqqh_zz.e0.p0.whizard195

sel_signal=0
sel_zh=1
sel_bg=2
channel_opt_ll=2  #1 for hvvjj, 2 for hjjvv
channel_opt_nn=1
channel_opt_qq=2  #1 for hvvmm, 2 for hmmvv
llhzz=1
nnhzz=2
qqhzz=3

    # --------------------------------------------------------------------------
    #  1.1 mmHZZ Signal   
    # --------------------------------------------------------------------------

sub_1_1(){
case $option in 

    1.1) echo "Running on signal sample..."
         ;;

    1.1.1) echo "Copy signal samples from cut-based framework..."
	   rm -rf  ./run/channel_ll_${channel_opt_ll}/llh2zz/ana
	   mkdir -p   ./run/channel_ll_${channel_opt_ll}/llh2zz/
           cp -r ../run/channel_ll/llh2zz/ana ./run/channel_ll_${channel_opt_ll}/llh2zz/
	   echo "Finished!"
           ;;

    1.1.2) echo "Make Several Cuts before BDT..."
	   source setup.sh
	   rm -rf ./run/channel_ll_${channel_opt_ll}/llh2zz/beforeBDT
	   mkdir -p   ./run/channel_ll_${channel_opt_ll}/llh2zz/beforeBDT 
	   cd ./run/channel_ll_${channel_opt_ll}/llh2zz/ana
	   for file in *
	   do 
	     ../../../../python/BDT_pre.py $file ../beforeBDT/$file ${llhzz} ${channel_opt_ll} ${sel_signal}
	   done
	   cd ../../../../
           ;;

    1.1.3) echo "Copy the signal samples to another environment with sklearn, python3 and ROOT6..."
           rm -rf ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/Before/llh2zz
	   mkdir -p ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/Before/llh2zz
	   cp -r ./run/channel_ll_${channel_opt_ll}/llh2zz/beforeBDT ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/Before/llh2zz/
	   echo "Finished!"
	   ;;
    
    1.1.4) echo "Copy the signal samples added with BDT score branch back..."
           rm -rf ./run/channel_ll_${channel_opt_ll}/llh2zz/afterBDT
           cp -r ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/After/llh2zz/afterBDT ./run/channel_ll_${channel_opt_ll}/llh2zz/
           echo "Finished!"
           ;;

    1.1.5) echo "Select events on signal..."
	   echo "### Make sure to source setupATLAS.sh before running this !"
	   rm -rf ./run/channel_ll_${channel_opt_ll}/llh2zz/events/ana
	   mkdir -p   ./run/channel_ll_${channel_opt_ll}/llh2zz/events/ana
	   cd ./run/channel_ll_${channel_opt_ll}/llh2zz/afterBDT/
	   for file in *
	   do
	     ../../../../python/sel_events.py $file ../beforeBDT/$file ../events/ana/$file ${llhzz} ${channel_opt_ll}
	   done
	   cd ../../../../ 
           ;;

    1.1.6) echo  "Merge signal event root files..."
	   rm -rf ./run/channel_ll_${channel_opt_ll}/llh2zz/hist
           mkdir -p ./run/channel_ll_${channel_opt_ll}/llh2zz/hist
	   cd ./run/channel_ll_${channel_opt_ll}/llh2zz/events/ana/
	     hadd ../../hist/ana_File_merged_1.root *.root
	   cd ../../../../../
           ;; 

    esac
}

    # --------------------------------------------------------------------------
    #  1.2 ZH Inclusive Sample   
    # --------------------------------------------------------------------------

sub_1_2(){
case $option in 

    1.2) echo "Running on ZH inclusive sample..."
         ;;

    1.2.1) echo "Copy zh samples from cut-based framework..."
           rm -rf  ./run/channel_ll_${channel_opt_ll}/zh/ana
           mkdir -p   ./run/channel_ll_${channel_opt_ll}/zh/
           cp -r ../run/channel_ll/zh/ana ./run/channel_ll_${channel_opt_ll}/zh/
           echo "Finished!"
           ;;

    1.2.2) echo "Make Several Cuts before BDT..."
           source setup.sh
           rm -rf ./run/channel_ll_${channel_opt_ll}/zh/beforeBDT
           mkdir -p   ./run/channel_ll_${channel_opt_ll}/zh/beforeBDT
           cd ./run/channel_ll_${channel_opt_ll}/zh/ana
	   for dir in *
	   do 
	     mkdir -p ../beforeBDT/$dir
	   done 
	   for dir in *
	   do 
	     cd $dir
             for file in *
             do
               ../../../../../python/BDT_pre.py $file ../../beforeBDT/$dir/$file ${llhzz} ${channel_opt_ll} ${sel_zh}
	     done
	     cd ../
           done
           cd ../../../../../
           ;;

    1.2.3) echo "Copy the zh samples to another environment with sklearn, python3, pandas and ROOT6..."
           rm -rf ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/Before/zh
           mkdir -p ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/Before/zh
           cp -r ./run/channel_ll_${channel_opt_ll}/zh/beforeBDT ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/Before/zh/
           echo "Finished!"
           ;;

    1.2.4) echo "Copy the zh samples added with BDT score branch back..."
           rm -rf ./run/channel_ll_${channel_opt_ll}/zh/afterBDT
           cp -r ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/After/zh/afterBDT ./run/channel_ll_${channel_opt_ll}/zh/
           echo "Finished!"
           ;;

    1.2.5) echo "Select events on zh..."
           echo "### Make sure to source setupATLAS.sh before running this !"
           rm -rf ./run/channel_ll_${channel_opt_ll}/zh/events/ana
           mkdir -p   ./run/channel_ll_${channel_opt_ll}/zh/events/ana
           cd ./run/channel_ll_${channel_opt_ll}/zh/afterBDT/
	   for dir in *
	   do 
	     mkdir -p ../events/ana/$dir
	   done
	   for dir in *
	   do
	     cd $dir
	     for file in *
	     do 
	       rm ../../beforeBDT/$dir/merged_temp.root
	       hadd ../../beforeBDT/$dir/merged_temp.root ../../beforeBDT/$dir/*.root
	       wait
               ../../../../../python/sel_events.py $file ../../beforeBDT/$dir/merged_temp.root ../../events/ana/$dir/$file ${llhzz} ${channel_opt_ll}
	       wait
	       rm ../../beforeBDT/$dir/merged_temp.root
	     done
	     cd ../
           done
           cd ../../../../
           ;;

    1.2.6) echo  "Merge zh event root files..."
           rm -rf ./run/channel_ll_${channel_opt_ll}/zh/hist
           cp -r ./run/channel_ll_${channel_opt_ll}/zh/events/ana ./run/channel_ll_${channel_opt_ll}/zh/hist
	   ;;

    esac
}

    # --------------------------------------------------------------------------
    #  1.3 Background Sample   
    # --------------------------------------------------------------------------

sub_1_3(){
case $option in 

    1.3) echo "Running on background sample..."
         ;;

    1.3.1) echo "Copy bg samples from cut-based framework..."
           rm -rf  ./run/channel_ll_${channel_opt_ll}/bg/ana
           mkdir -p   ./run/channel_ll_${channel_opt_ll}/bg/
           cp -r ../run/channel_ll/bg/ana ./run/channel_ll_${channel_opt_ll}/bg/
           echo "Finished!"
           ;;

    1.3.2) echo "Make Several Cuts before BDT..."
           source setup.sh
           rm -rf ./run/channel_ll_${channel_opt_ll}/bg/beforeBDT
           mkdir -p   ./run/channel_ll_${channel_opt_ll}/bg/beforeBDT
           cd ./run/channel_ll_${channel_opt_ll}/bg/ana
           for dir in *
           do
             mkdir -p ../beforeBDT/$dir
           done
           for dir in *
           do
             cd $dir
             for file in *
             do
               ../../../../../python/BDT_pre.py $file ../../beforeBDT/$dir/$file ${llhzz} ${channel_opt_ll} ${sel_bg}
             done
             cd ../
           done
           cd ../../../../../
           ;;

    1.3.3) echo "Copy the bg samples to another environment with sklearn, python3, pandas and ROOT6..."
           rm -rf ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/Before/bg
           mkdir -p ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/Before/bg
           cp -r ./run/channel_ll_${channel_opt_ll}/bg/beforeBDT ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/Before/bg/
           echo "Finished!"
           ;;

    1.3.4) echo "Copy the bg samples added with BDT score branch back..."
           rm -rf ./run/channel_ll_${channel_opt_ll}/bg/afterBDT
           cp -r ./Train_AddBDTscore/sample/channel_ll_${channel_opt_ll}/After/bg/afterBDT ./run/channel_ll_${channel_opt_ll}/bg/
           echo "Finished!"
           ;;

    1.3.5) echo "Select events on bg..."
           echo "### Make sure to source setupATLAS.sh before running this !"
           rm -rf ./run/channel_ll_${channel_opt_ll}/bg/events/ana
           mkdir -p   ./run/channel_ll_${channel_opt_ll}/bg/events/ana
           cd ./run/channel_ll_${channel_opt_ll}/bg/afterBDT/
           for dir in *
           do
             mkdir -p ../events/ana/$dir
           done
           for dir in *
           do
             cd $dir
	     for file in *
	     do
               rm ../../beforeBDT/$dir/merged_temp.root
               hadd ../../beforeBDT/$dir/merged_temp.root ../../beforeBDT/$dir/*.root
               wait
               ../../../../../python/sel_events.py $file ../../beforeBDT/$dir/merged_temp.root ../../events/ana/$dir/$file ${llhzz} ${channel_opt_ll}
               wait
               rm ../../beforeBDT/$dir/merged_temp.root
	     done
             cd ../
           done
           cd ../../../../
	   ;;
    1.3.6) echo  "Merge bg event root files..."
           rm -rf ./run/channel_ll_${channel_opt_ll}/bg/hist
           cp -r ./run/channel_ll_${channel_opt_ll}/bg/events/ana ./run/channel_ll_${channel_opt_ll}/bg/hist
           ;;

    esac
}

    # --------------------------------------------------------------------------
    #  1.4 plot pictures and save results  
    # --------------------------------------------------------------------------

sub_1_4(){
case $option in 

    1.4) echo "plot pictures and save results..."
         ;;

    1.4.1) echo  "Plot S/√(S+B) versus BDT score cut histogram..."
           mkdir -p ./fig/channel_ll_${channel_opt_ll}
           python ./python/bdt_score_sel.py  ${llhzz}  ${channel_opt_ll} ./table/bg_2f.txt  ./table/bg_4f.txt  ./table/zh_sample_list.txt
	   ;;

    1.4.2) echo  "Plot signal-bg histograms..."
	   mkdir -p ./fig/channel_ll_${channel_opt_ll}
           python ./python/plt_bg.py  ${llhzz}  ${channel_opt_ll} ./table/bg_2f.txt  ./table/bg_4f.txt  ./table/zh_sample_list.txt 
           ;; 

    1.4.3) echo  "Plot information..."  # Meantime, it will generate table for LaTeX
	   rm -rf ./table/channel_ll_${channel_opt_ll}
           mkdir -p ./table/channel_ll_${channel_opt_ll}
           python ./python/plt_info.py  ${llhzz} ${channel_opt_ll} ./table/zh_sample_list.txt  ./table/bg_2f.txt  ./table/bg_4f.txt 
           ;; 


    1.4.4) echo  "Generate tables and LaTex tables..."
           python ./python/gen_tex.py  ${llhzz} ${channel_opt_ll} ./table/zh_sample_list.txt ./table/bg_2f.txt  ./table/bg_4f.txt 
	   ;; 
			
    1.4.5) echo  "Save results..."
	   rm -rf ./root/channel_ll_${channel_opt_ll}
	   mkdir -p   ./root/channel_ll_${channel_opt_ll}/merge
	   python ./python/save_root.py  ${llhzz} ${channel_opt_ll} ./table/bg_2f.txt  ./table/bg_4f.txt  ./table/zh_sample_list.txt 

	   cd ./root/channel_ll_${channel_opt_ll}

	   if [ ${channel_opt_ll} = 1 ]; then
               cp sig.root ./merge/mzvj_sig.root
               hadd ./merge/mzvj_az.root bkg_e2e2h_az.root 
               hadd ./merge/mzvj_zz.root bkg_e2e2h_zz.root bkg_e3e3h_zz.root bkg_nnh_zz.root
               hadd ./merge/mzvj_ww.root bkg_e2e2h_ww.root bkg_e3e3h_ww.root
               hadd ./merge/mzvj_tt.root bkg_e2e2h_e3e3.root bkg_e3e3h_e3e3.root
               hadd ./merge/mzvj_sm.root bkg_e2e2.root bkg_sze_l0mu.root bkg_zz_sl0tau_up.root

		cd ../../
		cp -r root/channel_ll_1/merge/. calculate/workspace/data/new_zz/mzvj/
		# cd calculate/workspace/data/new_zz/mzvj/
		# root -l -q mzvj.cxx
           else
		cp sig.root ./merge/mzjv_sig.root
		hadd ./merge/mzjv_zz.root bkg_e2e2h_zz.root bkg_e3e3h_zz.root bkg_nnh_zz.root bkg_qqh_zz.root
		hadd ./merge/mzjv_ww.root bkg_e2e2h_ww.root bkg_e3e3h_ww.root bkg_qqh_ww.root
		hadd ./merge/mzjv_tt.root bkg_e2e2h_e3e3.root bkg_qqh_e3e3.root
		hadd ./merge/mzjv_az.root bkg_e1e1h_az.root bkg_e2e2h_aa.root bkg_e2e2h_az.root bkg_e3e3h_az.root bkg_qqh_az.root
		hadd ./merge/mzjv_bb.root bkg_e2e2h_bb.root
		hadd ./merge/mzjv_cc.root bkg_e2e2h_cc.root
		hadd ./merge/mzjv_gg.root bkg_e2e2h_gg.root
		hadd ./merge/mzjv_sm.root bkg_e2e2.root bkg_zz_sl0mu_up.root bkg_zz_sl0mu_down.root bkg_zz_sl0tau_down.root bkg_zz_l0taumu.root bkg_ww_sl0muq.root bkg_ww_sl0tauq.root bkg_sze_l0mu.root
		
		cd ../..
		cp -r root/channel_ll_2/merge/. calculate/workspace/data/new_zz/mzjv/
		# cd calculate/workspace/data/new_zz/mzjv/
		# root -l -q mzjv.cxx
            fi
            ;;

    esac
}


    # --------------------------------------------------------------------------
    #  2.1 nnHZZ Signal   
    # --------------------------------------------------------------------------

sub_2_1(){
case $option in 

    2.1) echo "Running on signal sample..."
         ;;

    2.1.1) echo "Copy signal samples from cut-based framework..."
	   rm -rf  ./run/channel_nn_${channel_opt_nn}/nnh2zz/ana
	   mkdir -p   ./run/channel_nn_${channel_opt_nn}/nnh2zz/
	   cp -r ../run/channel_nn/nnh2zz/ana ./run/channel_nn_${channel_opt_nn}/nnh2zz/
	   echo "Finished!"
           ;;

    2.1.2) echo "Make Several Cuts before BDT..."
	   source setup.sh
	   rm -rf ./run/channel_nn_${channel_opt_nn}/nnh2zz/beforeBDT
	   mkdir -p   ./run/channel_nn_${channel_opt_nn}/nnh2zz/beforeBDT 
	   cd ./run/channel_nn_${channel_opt_nn}/nnh2zz/ana
	   for file in *
	   do 
	     ../../../../python/BDT_pre.py $file ../beforeBDT/$file ${nnhzz} ${channel_opt_nn} ${sel_signal}
	   done
	   cd ../../../../
           ;;

    2.1.3) echo "Copy the signal samples to another environment with sklearn, python3 and ROOT6..."
           rm -rf ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/Before/nnh2zz
	   mkdir -p ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/Before/nnh2zz
	   cp -r ./run/channel_nn_${channel_opt_nn}/nnh2zz/beforeBDT ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/Before/nnh2zz/
	   echo "Finished!"
	   ;;
    
    2.1.4) echo "Copy the signal samples added with BDT score branch back..."
           rm -rf ./run/channel_nn_${channel_opt_nn}/nnh2zz/afterBDT
           cp -r ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/After/nnh2zz/afterBDT ./run/channel_nn_${channel_opt_nn}/nnh2zz/
           echo "Finished!"
           ;;

    2.1.5) echo "Select events on signal..."
	   echo "### Make sure to source setupATLAS.sh before running this !"
	   rm -rf ./run/channel_nn_${channel_opt_nn}/nnh2zz/events/ana
	   mkdir -p   ./run/channel_nn_${channel_opt_nn}/nnh2zz/events/ana
	   cd ./run/channel_nn_${channel_opt_nn}/nnh2zz/afterBDT/
	   for file in *
	   do
	     ../../../../python/sel_events.py $file ../beforeBDT/$file ../events/ana/$file ${nnhzz} ${channel_opt_nn}
	   done
	   cd ../../../../ 
           ;;

    2.1.6) echo  "Merge signal event root files..."
	   rm -rf ./run/channel_nn_${channel_opt_nn}/nnh2zz/hist
           mkdir -p ./run/channel_nn_${channel_opt_nn}/nnh2zz/hist
	   cd ./run/channel_nn_${channel_opt_nn}/nnh2zz/events/ana/
	     hadd ../../hist/ana_File_merged_1.root *.root
	   cd ../../../../../
           ;; 

    esac
}

    # --------------------------------------------------------------------------
    #  2.2 ZH Inclusive Sample   
    # --------------------------------------------------------------------------

sub_2_2(){
case $option in 

    2.2) echo "Running on ZH inclusive sample..."
         ;;

    2.2.1) echo "Copy zh samples from cut-based framework..."
           rm -rf  ./run/channel_nn_${channel_opt_nn}/zh/ana
           mkdir -p   ./run/channel_nn_${channel_opt_nn}/zh/
           cp -r ../run/channel_nn/zh/ana ./run/channel_nn_${channel_opt_nn}/zh/
           echo "Finished!"
           ;;

    2.2.2) echo "Make Several Cuts before BDT..."
           source setup.sh
           rm -rf ./run/channel_nn_${channel_opt_nn}/zh/beforeBDT
           mkdir -p   ./run/channel_nn_${channel_opt_nn}/zh/beforeBDT
           cd ./run/channel_nn_${channel_opt_nn}/zh/ana
	   for dir in *
	   do 
	     mkdir -p ../beforeBDT/$dir
	   done 
	   for dir in *
	   do 
	     cd $dir
             for file in *
             do
               ../../../../../python/BDT_pre.py $file ../../beforeBDT/$dir/$file ${nnhzz} ${channel_opt_nn} ${sel_zh}
	     done
	     cd ../
           done
           cd ../../../../../
           ;;

    2.2.3) echo "Copy the zh samples to another environment with sklearn, python3, pandas and ROOT6..."
           rm -rf ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/Before/zh
           mkdir -p ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/Before/zh
           cp -r ./run/channel_nn_${channel_opt_nn}/zh/beforeBDT ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/Before/zh/
           echo "Finished!"
           ;;

    2.2.4) echo "Copy the zh samples added with BDT score branch back..."
           rm -rf ./run/channel_nn_${channel_opt_nn}/zh/afterBDT
           cp -r ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/After/zh/afterBDT ./run/channel_nn_${channel_opt_nn}/zh/
           echo "Finished!"
           ;;

    2.2.5) echo "Select events on zh..."
           echo "### Make sure to source setupATLAS.sh before running this !"
           rm -rf ./run/channel_nn_${channel_opt_nn}/zh/events/ana
           mkdir -p   ./run/channel_nn_${channel_opt_nn}/zh/events/ana
           cd ./run/channel_nn_${channel_opt_nn}/zh/afterBDT/
	   for dir in *
	   do 
	     mkdir -p ../events/ana/$dir
	   done
	   for dir in *
	   do
	     cd $dir
	     for file in *
	     do 
	       rm ../../beforeBDT/$dir/merged_temp.root
	       hadd ../../beforeBDT/$dir/merged_temp.root ../../beforeBDT/$dir/*.root
	       wait
               ../../../../../python/sel_events.py $file ../../beforeBDT/$dir/merged_temp.root ../../events/ana/$dir/$file ${nnhzz} ${channel_opt_nn}
	       wait
	       rm ../../beforeBDT/$dir/merged_temp.root
	     done
	     cd ../
           done
           cd ../../../../
           ;;

    2.2.6) echo  "Merge zh event root files..."
           rm -rf ./run/channel_nn_${channel_opt_nn}/zh/hist
           cp -r ./run/channel_nn_${channel_opt_nn}/zh/events/ana ./run/channel_nn_${channel_opt_nn}/zh/hist
	   ;;

    esac
}

    # --------------------------------------------------------------------------
    #  2.3 Background Sample   
    # --------------------------------------------------------------------------

sub_2_3(){
case $option in 

    2.3) echo "Running on background sample..."
         ;;

    2.3.1) echo "Copy bg samples from cut-based framework..."
           rm -rf  ./run/channel_nn_${channel_opt_nn}/bg/ana
           mkdir -p   ./run/channel_nn_${channel_opt_nn}/bg/
           cp -r ../run/channel_nn/bg/ana ./run/channel_nn_${channel_opt_nn}/bg/
           echo "Finished!"
           ;;

    2.3.2) echo "Make Several Cuts before BDT..."
           source setup.sh
           rm -rf ./run/channel_nn_${channel_opt_nn}/bg/beforeBDT
           mkdir -p   ./run/channel_nn_${channel_opt_nn}/bg/beforeBDT
           cd ./run/channel_nn_${channel_opt_nn}/bg/ana
           for dir in *
           do
             mkdir -p ../beforeBDT/$dir
           done
           for dir in *
           do
             cd $dir
             for file in *
             do
               ../../../../../python/BDT_pre.py $file ../../beforeBDT/$dir/$file ${nnhzz} ${channel_opt_nn} ${sel_bg}
             done
             cd ../
           done
           cd ../../../../../
           ;;

    2.3.3) echo "Copy the bg samples to another environment with sklearn, python3, pandas and ROOT6..."
           rm -rf ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/Before/bg
           mkdir -p ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/Before/bg
           cp -r ./run/channel_nn_${channel_opt_nn}/bg/beforeBDT ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/Before/bg/
           echo "Finished!"
           ;;

    2.3.4) echo "Copy the bg samples added with BDT score branch back..."
           rm -rf ./run/channel_nn_${channel_opt_nn}/bg/afterBDT
           cp -r ./Train_AddBDTscore/sample/channel_nn_${channel_opt_nn}/After/bg/afterBDT ./run/channel_nn_${channel_opt_nn}/bg/
           echo "Finished!"
           ;;

    2.3.5) echo "Select events on bg..."
           echo "### Make sure to source setupATLAS.sh before running this !"
           rm -rf ./run/channel_nn_${channel_opt_nn}/bg/events/ana
           mkdir -p   ./run/channel_nn_${channel_opt_nn}/bg/events/ana
           cd ./run/channel_nn_${channel_opt_nn}/bg/afterBDT/
           for dir in *
           do
             mkdir -p ../events/ana/$dir
           done
           for dir in *
           do
             cd $dir
	     for file in *
	     do
               rm ../../beforeBDT/$dir/merged_temp.root
               hadd ../../beforeBDT/$dir/merged_temp.root ../../beforeBDT/$dir/*.root
               wait
               ../../../../../python/sel_events.py $file ../../beforeBDT/$dir/merged_temp.root ../../events/ana/$dir/$file ${nnhzz} ${channel_opt_nn}
               wait
               rm ../../beforeBDT/$dir/merged_temp.root
	     done
             cd ../
           done
           cd ../../../../
	   ;;
    2.3.6) echo  "Merge bg event root files..."
           rm -rf ./run/channel_nn_${channel_opt_nn}/bg/hist
           cp -r ./run/channel_nn_${channel_opt_nn}/bg/events/ana ./run/channel_nn_${channel_opt_nn}/bg/hist
           ;;

    esac
}

    # --------------------------------------------------------------------------
    #  2.4 plot pictures and save results  
    # --------------------------------------------------------------------------

sub_2_4(){
case $option in 

    2.4) echo "plot pictures and save results..."
         ;;

    2.4.1) echo  "Plot S/√(S+B) versus BDT score cut histogram..."
           mkdir -p ./fig/channel_nn_${channel_opt_nn}
           python ./python/bdt_score_sel.py  ${nnhzz}  ${channel_opt_nn} ./table/bg_2f.txt  ./table/bg_4f.txt  ./table/zh_sample_list.txt
	   ;;

    2.4.2) echo  "Plot signal-bg histograms..."
	   mkdir -p ./fig/channel_nn_${channel_opt_nn}
           python ./python/plt_bg.py  ${nnhzz}  ${channel_opt_nn} ./table/bg_2f.txt  ./table/bg_4f.txt  ./table/zh_sample_list.txt 
           ;; 

    2.4.3) echo  "Plot information..."  # Meantime, it winn generate table for LaTeX
	   rm -rf ./table/channel_nn_${channel_opt_nn}
           mkdir -p ./table/channel_nn_${channel_opt_nn}
           python ./python/plt_info.py  ${nnhzz} ${channel_opt_nn} ./table/zh_sample_list.txt  ./table/bg_2f.txt  ./table/bg_4f.txt 
           ;; 


    2.4.4) echo  "Generate tables and LaTex tables..."
           python ./python/gen_tex.py  ${nnhzz} ${channel_opt_nn} ./table/zh_sample_list.txt ./table/bg_2f.txt  ./table/bg_4f.txt 
	   ;; 
			
    2.4.5) echo  "Save results..."
	   rm -rf ./root/channel_nn_${channel_opt_nn}
	   mkdir -p   ./root/channel_nn_${channel_opt_nn}/merge
	   python ./python/save_root.py  ${nnhzz} ${channel_opt_nn} ./table/bg_2f.txt  ./table/bg_4f.txt  ./table/zh_sample_list.txt 

	   cd ./root/channel_nn_${channel_opt_nn}

           if [ ${channel_opt_nn} = 1 ]; then
                cp sig.root ./merge/vzmj_sig.root
                hadd ./merge/vzmj_zz.root bkg_e2e2h_zz.root bkg_e3e3h_zz.root bkg_qqh_zz.root
                hadd ./merge/vzmj_ww.root bkg_e2e2h_ww.root bkg_e3e3h_ww.root bkg_qqh_ww.root
                hadd ./merge/vzmj_tt.root bkg_e2e2h_e3e3.root bkg_e3e3h_e3e3.root bkg_qqh_e3e3.root
                hadd ./merge/vzmj_az.root bkg_e2e2h_az.root
                hadd ./merge/vzmj_bb.root bkg_e3e3h_bb.root
                hadd ./merge/vzmj_cc.root bkg_e2e2h_cc.root
                hadd ./merge/vzmj_gg.root bkg_e2e2h_gg.root
                hadd ./merge/vzmj_sm.root bkg_zz_sl0mu_down.root bkg_zz_sl0tau_up.root bkg_zz_sl0tau_down.root bkg_zz_l0taumu.root bkg_ww_sl0muq.root bkg_ww_sl0tauq.root bkg_ww_l0ll.root bkg_zzorww_l0mumu.root

                cd ../..
                cp -r root/channel_nn_1/merge/. calculate/workspace/data/new_zz/vzmj/
                #root -l -q vzmj.cxx
            fi
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

    1.1) echo "run signal sample"
        usage_1_1
        echo "Please enter your option: " 
        read option 
        sub_1_1 option 
        ;;
    1.1.*) echo "run signal sample"
        sub_1_1 option
        ;;
        
    1.2) echo "run Z(->ff)H(->inclusive) sample"
        usage_1_2
        echo "Please enter your option: " 
        read option  
        sub_1_2 option 
        ;;
    1.2.*) echo "run Z(->ff)H(->inclusive) sample"
        sub_1_2 option 
        ;;

    1.3) echo "run background sample." 
        usage_1_3
        echo "Please enter your option: " 
        read option 
        sub_1_3 option 
        ;;
    1.3.*) echo "run background sample"
        sub_1_3 option 
        ;;

    1.4) echo "plot pictures and save results"
        usage_1_4
        echo "Please enter your option: " 
        read option
        sub_1_4 option 
        ;;        
    1.4.*) echo "plot pictures and save results"
        sub_1_4 option 
        ;; 
esac
}

sub_2(){
case $option in

    2.1) echo "run signal sample"
        usage_2_1
        echo "Please enter your option: " 
        read option
        sub_2_1 option
        ;;
    2.1.*) echo "run signal sample"
        sub_2_1 option
        ;;

    2.2) echo "run Z(->ll,qq,nn)H(->inclusive) sample"
        usage_2_2
        echo "Please enter your option: " 
        read option
        sub_2_2 option
        ;;
    2.2.*) echo "run Z(->ll,qq,nn)H(->inclusive) background sample"
        sub_2_2 option
        ;;

    2.3) echo "run background sample." 
        usage_2_3
        echo "Please enter your option: " 
        read option
        sub_2_3 option
        ;;
    2.3.*) echo "run background sample"
        sub_2_3 option
        ;;

    2.4) echo "plot pictures and save results"
        usage_2_4
        echo "Please enter your option: " 
        read option
        sub_2_4 option
        ;;
    2.4.*) echo "plot pictures and save results"
        sub_2_4 option
        ;;
esac
}


    # --------------------------------------------------------------------------
    #  3.1 qqHZZ Signal   
    # --------------------------------------------------------------------------

sub_3_1(){
case $option in 

    3.1) echo "Running on signal sample..."
         ;;

    3.1.1) echo "Copy signal samples from cut-based framework..."
	   rm -rf  ./run/channel_qq_${channel_opt_qq}/qqh2zz/ana
	   mkdir -p   ./run/channel_qq_${channel_opt_qq}/qqh2zz/
	   cp -r ../run/channel_qq/qqh2zz/ana ./run/channel_qq_${channel_opt_qq}/qqh2zz/
	   echo "Finished!"
           ;;

    3.1.2) echo "Make Several Cuts before BDT..."
	   source setup.sh
	   rm -rf ./run/channel_qq_${channel_opt_qq}/qqh2zz/beforeBDT
	   mkdir -p   ./run/channel_qq_${channel_opt_qq}/qqh2zz/beforeBDT 
	   cd ./run/channel_qq_${channel_opt_qq}/qqh2zz/ana
	   for file in *
	   do 
	     ../../../../python/BDT_pre.py $file ../beforeBDT/$file ${qqhzz} ${channel_opt_qq} ${sel_signal}
	   done
	   cd ../../../../
           ;;

    3.1.3) echo "Copy the signal samples to another environment with sklearn, python3 and ROOT6..."
           rm -rf ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/Before/qqh2zz
	   mkdir -p ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/Before/qqh2zz
	   cp -r ./run/channel_qq_${channel_opt_qq}/qqh2zz/beforeBDT ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/Before/qqh2zz/
	   echo "Finished!"
	   ;;
    
    3.1.4) echo "Copy the signal samples added with BDT score branch back..."
           rm -rf ./run/channel_qq_${channel_opt_qq}/qqh2zz/afterBDT
           cp -r ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/After/qqh2zz/afterBDT ./run/channel_qq_${channel_opt_qq}/qqh2zz/
           echo "Finished!"
           ;;

    3.1.5) echo "Select events on signal..."
	   echo "### Make sure to source setupATLAS.sh before running this !"
	   rm -rf ./run/channel_qq_${channel_opt_qq}/qqh2zz/events/ana
	   mkdir -p   ./run/channel_qq_${channel_opt_qq}/qqh2zz/events/ana
	   cd ./run/channel_qq_${channel_opt_qq}/qqh2zz/afterBDT/
	   for file in *
	   do
	     ../../../../python/sel_events.py $file ../beforeBDT/$file ../events/ana/$file ${qqhzz} ${channel_opt_qq}
	   done
	   cd ../../../../ 
           ;;

    3.1.6) echo  "Merge signal event root files..."
	   rm -rf ./run/channel_qq_${channel_opt_qq}/qqh2zz/hist
           mkdir -p ./run/channel_qq_${channel_opt_qq}/qqh2zz/hist
	   cd ./run/channel_qq_${channel_opt_qq}/qqh2zz/events/ana/
	     hadd ../../hist/ana_File_merged_1.root *.root
	   cd ../../../../../
           ;; 

    esac
}

    # --------------------------------------------------------------------------
    #  3.2 ZH Inclusive Sample   
    # --------------------------------------------------------------------------

sub_3_2(){
case $option in 

    3.2) echo "Running on ZH inclusive sample..."
         ;;

    3.2.1) echo "Copy zh samples from cut-based framework..."
           rm -rf  ./run/channel_qq_${channel_opt_qq}/zh/ana
           mkdir -p   ./run/channel_qq_${channel_opt_qq}/zh/
           cp -r ../run/channel_qq/zh/ana ./run/channel_qq_${channel_opt_qq}/zh/
           echo "Finished!"
           ;;

    3.2.2) echo "Make Several Cuts before BDT..."
           source setup.sh
           rm -rf ./run/channel_qq_${channel_opt_qq}/zh/beforeBDT
           mkdir -p   ./run/channel_qq_${channel_opt_qq}/zh/beforeBDT
           cd ./run/channel_qq_${channel_opt_qq}/zh/ana
	   for dir in *
	   do 
	     mkdir -p ../beforeBDT/$dir
	   done 
	   for dir in *
	   do 
	     cd $dir
             for file in *
             do
               ../../../../../python/BDT_pre.py $file ../../beforeBDT/$dir/$file ${qqhzz} ${channel_opt_qq} ${sel_zh}
	     done
	     cd ../
           done
           cd ../../../../../
           ;;

    3.2.3) echo "Copy the zh samples to another environment with sklearn, python3, pandas and ROOT6..."
           rm -rf ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/Before/zh
           mkdir -p ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/Before/zh
           cp -r ./run/channel_qq_${channel_opt_qq}/zh/beforeBDT ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/Before/zh/
           echo "Finished!"
           ;;

    3.2.4) echo "Copy the zh samples added with BDT score branch back..."
           rm -rf ./run/channel_qq_${channel_opt_qq}/zh/afterBDT
           cp -r ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/After/zh/afterBDT ./run/channel_qq_${channel_opt_qq}/zh/
           echo "Finished!"
           ;;

    3.2.5) echo "Select events on zh..."
           echo "### Make sure to source setupATLAS.sh before running this !"
           rm -rf ./run/channel_qq_${channel_opt_qq}/zh/events/ana
           mkdir -p   ./run/channel_qq_${channel_opt_qq}/zh/events/ana
           cd ./run/channel_qq_${channel_opt_qq}/zh/afterBDT/
	   for dir in *
	   do 
	     mkdir -p ../events/ana/$dir
	   done
	   for dir in *
	   do
	     cd $dir
	     for file in *
	     do 
	       rm ../../beforeBDT/$dir/merged_temp.root
	       hadd ../../beforeBDT/$dir/merged_temp.root ../../beforeBDT/$dir/*.root
	       wait
               ../../../../../python/sel_events.py $file ../../beforeBDT/$dir/merged_temp.root ../../events/ana/$dir/$file ${qqhzz} ${channel_opt_qq}
	       wait
	       rm ../../beforeBDT/$dir/merged_temp.root
	     done
	     cd ../
           done
           cd ../../../../
           ;;

    3.2.6) echo  "Merge zh event root files..."
           rm -rf ./run/channel_qq_${channel_opt_qq}/zh/hist
           cp -r ./run/channel_qq_${channel_opt_qq}/zh/events/ana ./run/channel_qq_${channel_opt_qq}/zh/hist
	   ;;

    esac
}

    # --------------------------------------------------------------------------
    #  3.3 Background Sample   
    # --------------------------------------------------------------------------

sub_3_3(){
case $option in 

    3.3) echo "Running on background sample..."
         ;;

    3.3.1) echo "Copy bg samples from cut-based framework..."
           rm -rf  ./run/channel_qq_${channel_opt_qq}/bg/ana
           mkdir -p   ./run/channel_qq_${channel_opt_qq}/bg/
           cp -r ../run/channel_qq/bg/ana ./run/channel_qq_${channel_opt_qq}/bg/
           echo "Finished!"
           ;;

    3.3.2) echo "Make Several Cuts before BDT..."
           source setup.sh
           rm -rf ./run/channel_qq_${channel_opt_qq}/bg/beforeBDT
           mkdir -p   ./run/channel_qq_${channel_opt_qq}/bg/beforeBDT
           cd ./run/channel_qq_${channel_opt_qq}/bg/ana
           for dir in *
           do
             mkdir -p ../beforeBDT/$dir
           done
           for dir in *
           do
             cd $dir
             for file in *
             do
               ../../../../../python/BDT_pre.py $file ../../beforeBDT/$dir/$file ${qqhzz} ${channel_opt_qq} ${sel_bg}
             done
             cd ../
           done
           cd ../../../../../
           ;;

    3.3.3) echo "Copy the bg samples to another environment with sklearn, python3, pandas and ROOT6..."
           rm -rf ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/Before/bg
           mkdir -p ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/Before/bg
           cp -r ./run/channel_qq_${channel_opt_qq}/bg/beforeBDT ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/Before/bg/
           echo "Finished!"
           ;;

    3.3.4) echo "Copy the bg samples added with BDT score branch back..."
           rm -rf ./run/channel_qq_${channel_opt_qq}/bg/afterBDT
           cp -r ./Train_AddBDTscore/sample/channel_qq_${channel_opt_qq}/After/bg/afterBDT ./run/channel_qq_${channel_opt_qq}/bg/
           echo "Finished!"
           ;;

    3.3.5) echo "Select events on bg..."
           echo "### Make sure to source setupATLAS.sh before running this !"
           rm -rf ./run/channel_qq_${channel_opt_qq}/bg/events/ana
           mkdir -p   ./run/channel_qq_${channel_opt_qq}/bg/events/ana
           cd ./run/channel_qq_${channel_opt_qq}/bg/afterBDT/
           for dir in *
           do
             mkdir -p ../events/ana/$dir
           done
           for dir in *
           do
             cd $dir
	     for file in *
	     do
               rm ../../beforeBDT/$dir/merged_temp.root
               hadd ../../beforeBDT/$dir/merged_temp.root ../../beforeBDT/$dir/*.root
               wait
               ../../../../../python/sel_events.py $file ../../beforeBDT/$dir/merged_temp.root ../../events/ana/$dir/$file ${qqhzz} ${channel_opt_qq}
               wait
               rm ../../beforeBDT/$dir/merged_temp.root
	     done
             cd ../
           done
           cd ../../../../
	   ;;
    3.3.6) echo  "Merge bg event root files..."
           rm -rf ./run/channel_qq_${channel_opt_qq}/bg/hist
           cp -r ./run/channel_qq_${channel_opt_qq}/bg/events/ana ./run/channel_qq_${channel_opt_qq}/bg/hist
           ;;

    esac
}

    # --------------------------------------------------------------------------
    #  3.4 plot pictures and save results  
    # --------------------------------------------------------------------------

sub_3_4(){
case $option in 

    3.4) echo "plot pictures and save results..."
         ;;

    3.4.1) echo  "Plot S/√(S+B) versus BDT score cut histogram..."
           mkdir -p ./fig/channel_qq_${channel_opt_qq}
           python ./python/bdt_score_sel.py  ${qqhzz}  ${channel_opt_qq} ./table/bg_2f.txt  ./table/bg_4f.txt  ./table/zh_sample_list.txt
	   ;;

    3.4.2) echo  "Plot signal-bg histograms..."
	   mkdir -p ./fig/channel_qq_${channel_opt_qq}
           python ./python/plt_bg.py  ${qqhzz}  ${channel_opt_qq} ./table/bg_2f.txt  ./table/bg_4f.txt  ./table/zh_sample_list.txt 
           ;; 

    3.4.3) echo  "Plot information..."  # Meantime, it wiqq generate table for LaTeX
	   rm -rf ./table/channel_qq_${channel_opt_qq}
           mkdir -p ./table/channel_qq_${channel_opt_qq}
           python ./python/plt_info.py  ${qqhzz} ${channel_opt_qq} ./table/zh_sample_list.txt  ./table/bg_2f.txt  ./table/bg_4f.txt 
           ;; 


    3.4.4) echo  "Generate tables and LaTex tables..."
           python ./python/gen_tex.py  ${qqhzz} ${channel_opt_qq} ./table/zh_sample_list.txt ./table/bg_2f.txt  ./table/bg_4f.txt 
	   ;; 
			
    3.4.5) echo  "Save results..."
	   rm -rf ./root/channel_qq_${channel_opt_qq}
	   mkdir -p   ./root/channel_qq_${channel_opt_qq}/merge
	   python ./python/save_root.py  ${qqhzz} ${channel_opt_qq} ./table/bg_2f.txt  ./table/bg_4f.txt  ./table/zh_sample_list.txt 

	   cd ./root/channel_qq_${channel_opt_qq}

           if [ ${channel_opt_qq} = 1 ]; then
                cp sig.root ./merge/qzvm_sig.root
                hadd ./merge/qzvm_zz.root bkg_e2e2h_zz.root bkg_e3e3h_zz.root bkg_nnh_zz.root
                hadd ./merge/qzvm_ww.root bkg_e2e2h_ww.root bkg_e3e3h_ww.root bkg_nnh_ww.root bkg_qqh_ww.root
                hadd ./merge/qzvm_tt.root bkg_e2e2h_e3e3.root bkg_e3e3h_e3e3.root bkg_qqh_e3e3.root 
		hadd ./merge/qzvm_mm.root bkg_qqh_e2e2.root
                hadd ./merge/qzvm_az.root bkg_e2e2h_az.root bkg_e3e3h_az.root bkg_qqh_az.root
                hadd ./merge/qzvm_bb.root bkg_e2e2h_bb.root bkg_e3e3h_bb.root 
	        hadd ./merge/qzvm_cc.root bkg_e2e2h_cc.root bkg_e3e3h_cc.root
		hadd ./merge/qzvm_gg.root bkg_e2e2h_gg.root bkg_e3e3h_gg.root
                hadd ./merge/qzvm_sm.root bkg_zz_sl0mu_up.root bkg_zz_sl0mu_down.root bkg_zz_sl0tau_up.root bkg_zz_sl0tau_down.root bkg_zz_l04tau.root bkg_sze_l0mu.root
                cd ../..
                cp -r root/channel_qq_1/merge/. calculate/workspace/data/new_zz/qzvm/
                # cd calculate/workspace/data/new_zz/qzvm/
                # root -l -q qzvm.cxx
           else
                cp sig.root ./merge/qzmv_sig.root
                hadd ./merge/qzmv_zz.root bkg_e2e2h_zz.root bkg_e3e3h_zz.root bkg_qqh_zz.root
                hadd ./merge/qzmv_ww.root bkg_e2e2h_ww.root bkg_e3e3h_ww.root bkg_qqh_ww.root
                hadd ./merge/qzmv_tt.root bkg_e2e2h_e3e3.root bkg_qqh_e3e3.root
                hadd ./merge/qzmv_mm.root bkg_qqh_e2e2.root
                hadd ./merge/qzmv_az.root bkg_e2e2h_az.root bkg_qqh_az.root
                hadd ./merge/qzmv_bb.root bkg_e2e2h_bb.root bkg_e3e3h_bb.root
                hadd ./merge/qzmv_cc.root bkg_e2e2h_cc.root bkg_e3e3h_cc.root
                hadd ./merge/qzmv_gg.root bkg_e2e2h_gg.root bkg_e3e3h_gg.root
                hadd ./merge/qzmv_sm.root bkg_zz_sl0mu_up.root bkg_zz_sl0mu_down.root bkg_zz_sl0tau_up.root bkg_zz_sl0tau_down.root
                cd ../..
                cp -r root/channel_qq_2/merge/. calculate/workspace/data/new_zz/qzmv/

                # cd calculate/workspace/data/new_zz/qzmv/
                # root -l -q qzmv.cxx
            fi
            ;;
    3.4.6) echo  "fit results..." #source setupATLAS.sh first
           echo "Need to source ./calculate/setupATLAS.sh first"      
           echo "If it is not, please do so" 
           echo "Ready to go next ? Please type ENTER or stop now (Ctrl-C)" 
           read flag

           cd ./calculate/workspace/
           mkdir -p ./bin
           mkdir -p ./lib
           make clean
           ./job/run.sh
           ./job/plot.sh
           echo "Please check the output under ./calculate/workspace/out/ " 
           cd ../../
           ;;
    3.4.7) echo "combined fit..."
           cd ./calculate/cepcFit
           source ./jobs/new_zz.sh
           cd ../../
           ;;

    esac
}

sub_3(){
case $option in

    3.1) echo "run signal sample"
        usage_3_1
        echo "Please enter your option: " 
        read option
        sub_3_1 option
        ;;
    3.1.*) echo "run signal sample"
        sub_3_1 option
        ;;

    3.2) echo "run Z(->ll,qq,nn)H(->inclusive) sample"
        usage_3_2
        echo "Please enter your option: " 
        read option
        sub_3_2 option
        ;;
    3.2.*) echo "run Z(->ll,qq,nn)H(->inclusive) background sample"
        sub_3_2 option
        ;;

    3.3) echo "run background sample." 
        usage_3_3
        echo "Please enter your option: " 
        read option
        sub_3_3 option
        ;;
    3.3.*) echo "run background sample"
        sub_3_3 option
        ;;

    3.4) echo "plot pictures and save results"
        usage_3_4
        echo "Please enter your option: " 
        read option
        sub_3_4 option
        ;;
    3.4.*) echo "plot pictures and save results"
        sub_3_4 option
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
