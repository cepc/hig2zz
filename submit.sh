#!/usr/bin/env bash

# Main driver to submit jobs 
# Author Ryuta Kiuchi <kiuchi@ihep.ac.cn>
# Created [2018-06-16 Sat 16:00] 

usage() {
	printf "NAME\n\tsubmit.sh - Main driver to submit jobs\n"
	printf "\nSYNOPSIS\n"
	printf "\n\t%-5s\n" "./submit.sh [OPTION]" 
	printf "\nOPTIONS\n" 
	printf "\n\t%-9s  %-40s"  "0.1"      "[run signal sample]" 
	printf "\n\t%-9s  %-40s"  "0.1.1"    "Split signal sample with each group 0.5G" 
	printf "\n\t%-9s  %-40s"  "0.1.2"    "Generate XML input files for Marlin job" 
	printf "\n\t%-9s  %-40s"  "0.1.3"    "Run with a few events" 
	printf "\n\t%-9s  %-40s"  "0.1.4"    "Generate Condor job scripts for pre-selection" 
	printf "\n\t%-9s  %-40s"  "0.1.5"    "Submit Condor jobs for pre-selection on signal" 
	printf "\n\t%-9s  %-40s"  "0.1.6"    "Select events on signal (with a small sample)" 
	printf "\n\t%-9s  %-40s"  "0.1.7"    "Generate Condor job scripts for event selection" 	
	printf "\n\t%-9s  %-40s"  "0.1.8"    "Submit Condor jobs for event selection on signal" 
	printf "\n\t%-9s  %-40s"  "0.1.9"    "Merge event root files" 

	printf "\n" 
	printf "\n\t%-9s  %-40s"  "0.2"      "[run Z(->ff)H(->inclusive) sample]" 
	printf "\n\t%-9s  %-40s"  "0.2.1"    "Split ZH sample with each group 1G" 
	printf "\n\t%-9s  %-40s"  "0.2.2"    "Generate XML input files for Marlin job" 
	printf "\n\t%-9s  %-40s"  "0.2.3"    "Check the number files" 
	printf "\n\t%-9s  %-40s"  "0.2.4"    "Run with a few events" 
	printf "\n\t%-9s  %-40s"  "0.2.5"    "Generate Condor job scripts for pre-selection" 
	printf "\n\t%-9s  %-40s"  "0.2.6"    "Submit Condor jobs for pre-selection on ZH sample" 
	printf "\n\t%-9s  %-40s"  "0.2.7"    "Select events on ZH sample (with a small sample)"
	printf "\n\t%-9s  %-40s"  "0.2.8"    "Generate Condor job scripts for event selection" 	
	printf "\n\t%-9s  %-40s"  "0.2.9"    "Submit Condor jobs for event selection on ZH sample" 
	printf "\n\t%-9s  %-40s"  "0.2.10"   "Merge event root files" 
	printf "\n\t%-9s  %-40s"  "0.2.11"    "Plot signal-zh histograms..."


	printf "\n" 
	printf "\n\t%-9s  %-40s"  "0.3"      "[run background sample]" 
	printf "\n\t%-9s  %-40s"  "0.3.1"    "Split background sample with each group 20G" 
	printf "\n\t%-9s  %-40s"  "0.3.2"    "Generate XML input files for Marlin job" 
	printf "\n\t%-9s  %-40s"  "0.3.3"    "Check the number files" 
	printf "\n\t%-9s  %-40s"  "0.3.4"    "Run with a few events" 
	printf "\n\t%-9s  %-40s"  "0.3.5"    "Generate Condor job scripts for pre-selection" 
	printf "\n\t%-9s  %-40s"  "0.3.6"    "Submit Condor jobs for pre-selection on Bg sample" 
	printf "\n\t%-9s  %-40s"  "0.3.7"    "Select events on background (with a small sample)"
	printf "\n\t%-9s  %-40s"  "0.3.8"    "Generate Condor job scripts for event selection" 	
	printf "\n\t%-9s  %-40s"  "0.3.9"    "Submit Condor jobs for event selection on Bg sample" 
	printf "\n\t%-9s  %-40s"  "0.3.10"    "Merge event root files" 
	printf "\n\t%-9s  %-40s"  "0.3.11"    "Plot signal-bg histograms..."


	printf "\n" 
	printf "\n\t%-9s  %-40s"  "0.4"      "[run nnHiggs sample]" 
	printf "\n\t%-9s  %-40s"  "0.4.1"    "Split nnHiggs sample with each group 1G" 
	printf "\n\t%-9s  %-40s"  "0.4.2"    "Generate XML input files for Marlin job" 
	printf "\n\t%-9s  %-40s"  "0.4.3"    "Run with a few events" 
	printf "\n\t%-9s  %-40s"  "0.4.4"    "Generate Condor job scripts for pre-selection" 
	printf "\n\t%-9s  %-40s"  "0.4.5"    "Submit Condor jobs for pre-selection on nnHiggs sample" 
	printf "\n\t%-9s  %-40s"  "0.4.6"    "Select events on nnHiggs sample (with a small sample)" 
	printf "\n\t%-9s  %-40s"  "0.4.7"    "Generate Condor job scripts for event selection" 	
	printf "\n\t%-9s  %-40s"  "0.4.8"    "Submit Condor jobs for event selection on nnHiggs sample" 
	printf "\n\t%-9s  %-40s"  "0.4.9"    "Merge event root files" 


	printf "\n" 
	printf "\n\t%-9s  %-40s"  "0.5"      "[run mmHWW sample]" 
	printf "\n\t%-9s  %-40s"  "0.5.1"    "Split mmHWW sample with each group 1G" 
	printf "\n\t%-9s  %-40s"  "0.5.2"    "Generate XML input files for Marlin job" 
	printf "\n\t%-9s  %-40s"  "0.5.3"    "Run with a few events" 
	printf "\n\t%-9s  %-40s"  "0.5.4"    "Generate Condor job scripts for pre-selection" 
	printf "\n\t%-9s  %-40s"  "0.5.5"    "Submit Condor jobs for pre-selection on mmHWW sample" 
	printf "\n\t%-9s  %-40s"  "0.5.6"    "Select events on mmHWW sample (with a small sample)" 
	printf "\n\t%-9s  %-40s"  "0.5.7"    "Generate Condor job scripts for event selection" 	
	printf "\n\t%-9s  %-40s"  "0.5.8"    "Submit Condor jobs for event selection on mmHWW sample" 
	printf "\n\t%-9s  %-40s"  "0.5.9"    "Merge event root files" 

	printf "\n" 
	printf "\n\t%-9s  %-40s"  "0.6"      "[run mmHZZ sample]" 
	printf "\n\t%-9s  %-40s"  "0.6.1"    "Split mmHZZ sample with each group 1G" 
	printf "\n\t%-9s  %-40s"  "0.6.2"    "Generate XML input files for Marlin job" 
	printf "\n\t%-9s  %-40s"  "0.6.3"    "Run with a few events" 
	printf "\n\t%-9s  %-40s"  "0.6.4"    "Generate Condor job scripts for pre-selection" 
	printf "\n\t%-9s  %-40s"  "0.6.5"    "Submit Condor jobs for pre-selection on mmHZZ sample" 
	printf "\n\t%-9s  %-40s"  "0.6.6"    "Select events on mmHZZ sample (with a small sample)" 
	printf "\n\t%-9s  %-40s"  "0.6.7"    "Generate Condor job scripts for event selection" 	
	printf "\n\t%-9s  %-40s"  "0.6.8"    "Submit Condor jobs for event selection on mmHZZ sample" 
	printf "\n\t%-9s  %-40s"  "0.6.9"    "Merge event root files" 

	printf "\n" 
	printf "\n\t%-9s  %-40s"  "0.7"      "[run mmHe3e3 sample]" 
	printf "\n\t%-9s  %-40s"  "0.7.1"    "Split mmHtautau sample with each group 1G" 
	printf "\n\t%-9s  %-40s"  "0.7.2"    "Generate XML input files for Marlin job" 
	printf "\n\t%-9s  %-40s"  "0.7.3"    "Run with a few events" 
	printf "\n\t%-9s  %-40s"  "0.7.4"    "Generate Condor job scripts for pre-selection" 
	printf "\n\t%-9s  %-40s"  "0.7.5"    "Submit Condor jobs for pre-selection on mmHtautau sample" 
	printf "\n\t%-9s  %-40s"  "0.7.6"    "Select events on mmHtautau sample (with a small sample)" 
	printf "\n\t%-9s  %-40s"  "0.7.7"    "Generate Condor job scripts for event selection" 	
	printf "\n\t%-9s  %-40s"  "0.7.8"    "Submit Condor jobs for event selection on mmHtautau sample" 
	printf "\n\t%-9s  %-40s"  "0.7.9"    "Merge event root files" 


	printf "\nDATE\n"
	printf "\n\t%-5s\n" "JUNE 2018"     
}


if [[ $# -eq 0 ]]; then
    usage
    echo "Please enter your option: "
    read option
else
    option=$1    
fi

signal_slcio_dir=/besfs/groups/higgs/data/SimReco/wo_BS/CEPC_v4/higgs/smart_final_states/E240.Pllh_zz.e0.p0.whizard195/
nnhzz_slcio_dir=/besfs/groups/higgs/data/SimReco/wo_BS/CEPC_v4/higgs/smart_final_states/E240.Pnnh_zz.e0.p0.whizard195/

sel_all=0
sel_signal=1
sel_bg=2

mmh2ww_slcio_dir=/afs/ihep.ac.cn/users/k/kiuchi/h2zz/TestFullSim/reconstruction/output/e2e2h_ww/
mmh2zz_slcio_dir=/afs/ihep.ac.cn/users/k/kiuchi/h2zz/TestFullSim/reconstruction/output/e2e2h_zz/
mmh2tt_slcio_dir=/afs/ihep.ac.cn/users/k/kiuchi/h2zz/TestFullSim/reconstruction/output/e2e2h_e3e3/

case $option in 

    # --------------------------------------------------------------------------
    #  0.1 Signal   
    # --------------------------------------------------------------------------

    0.1) echo "Running on signal sample..."
         ;;

    0.1.1) echo "Split signal sample with each group 0.5G..."
	   mkdir -p   ./run/llh2zz/samples
           ./python/get_samples.py  ${signal_slcio_dir} ./run/llh2zz/samples/E240_Pllh_zz.txt 0.5G
           ;;

    0.1.2) echo "Generate XML input files for Marlin job..."
	   mkdir -p   ./run/llh2zz/steers 
	   mkdir -p   ./run/llh2zz/steers/test 
	   mkdir -p   ./run/llh2zz/ana
           ./python/gen_steerfiles.py ./table/template_jobfile.xml ./run/llh2zz/samples ./run/llh2zz/steers ./run/llh2zz/ana/ana_File.root
           ;;

    0.1.3) echo "Run with a few events ..."
	   source setup.sh
	   ./build.sh
	   Marlin ./run/llh2zz/steers/test/sample-1.xml
           ;;
    
    0.1.4) echo "Generate Condor job scripts..."
	   mkdir -p   ./run/llh2zz/condor/script/marlin
           ./python/gen_condorscripts.py  1  ./run/llh2zz/steers ./run/llh2zz/condor  ${sel_signal}
           ;;

    0.1.5) echo "Submit Condor jobs for pre-selection on signal..."
           cd ./run/llh2zz/condor
	   mkdir -p log
	   ./condor_submit.sh
           ;;

    0.1.6) echo "Select events on signal (with a small sample)..."
	   mkdir -p   ./run/llh2zz/events/ana
           ./python/sel_events.py  ./run/llh2zz/ana/ana_File-1.root  ./run/llh2zz/events/ana/ana_File-1_event.root ${sel_signal}
           ;;

    0.1.7) echo "Generate Condor job scripts for event selection..."
		rm -rf ./run/llh2zz/events/ana
		rm -rf ./run/llh2zz/condor/script/eventsel
	   mkdir -p   ./run/llh2zz/events/ana
           mkdir -p   ./run/llh2zz/condor/script/eventsel
	   ./python/gen_condorscripts.py  2  ./run/llh2zz/ana ./run/llh2zz/condor  ${sel_signal}
           ;;

    0.1.8) echo "Submit Condor jobs for event selection on signal..."
           cd ./run/llh2zz/condor
		   rm -rf log/events
	   mkdir -p log/events
	   ./condor_submit_eventsel.sh
           ;;

    0.1.9) echo  "Merge event root files..."
			rm -rf ./run/llh2zz/hist
           mkdir -p   ./run/llh2zz/hist
           ./python/mrg_rootfiles.py  ./run/llh2zz/events/ana  ./run/llh2zz/hist 
           ;; 


    # --------------------------------------------------------------------------
    #  0.2 ZH Inclusive Sample   
    # --------------------------------------------------------------------------


    0.2) echo "Running on ZH inclusive sample..."
         ;;

    0.2.1) echo "Split background sample with each group 1G..."
	   mkdir -p   ./run/zh/samples
	   ./python/get_bg_samples.py ./table/zh_sample_list.txt ./run/zh/samples 1G
           ;;

    0.2.2) echo "Generate XML input files for Marlin job..."
	   mkdir -p   ./run/zh/steers 
	   mkdir -p   ./run/zh/ana

           ./python/gen_bg_steerfiles.py ./table/zh_sample_list.txt ./table/template_jobfile.xml  ./run/zh/samples  ./run/zh/steers  ./run/zh/ana
           ;;

    0.2.3) echo "Check statistics : print the number of files..."
	   ./python/check_stat.py  ./table/zh_sample_list.txt ./run/zh/samples 
	   ;;
	   
    0.2.4) echo "Run with a few events ..."
	   source setup.sh
	   ./build.sh
	   cd ./run/zh/steers/

	   #array=("e1e1h_X" "e2e2h_X" "e3e3h_X" "nnh_X" "qqh_X")
	   array=("nnh_X" "qqh_X")
	   for dir in "${array[@]}"
	   do
	       cd ${dir}/test
	       Marlin sample-1.xml
	       cd ../../
	   done
           ;;

    0.2.5) echo "Generate Condor job scripts..."
	   mkdir -p   ./run/zh/condor

	   cd ./run/zh/ana/
	   for dir in *
	   do
	       mkdir -p ../condor/$dir
	   done

	   cd ../condor/
	   for dir in *
	   do
	       cd $dir
	       rm -rf log/marlin
	       rm -rf script/marlin
	       mkdir -p log/marlin
	       mkdir -p script/marlin
	       cd ../
	   done

	   cd ../../../
           ./python/gen_bg_condorscripts.py  1  ./run/zh/steers ./run/zh/condor  ${sel_signal}
           ;;

    0.2.6) echo "Submit Condor jobs for pre-selection on background sample..."
	   echo " ---- "
	   echo "Please enter the number of jobs for each ZH sample (default: 60)" 
	   read njob
	   if [ -z $njob ]; then
	       njob=60
	   fi
	   
           cd ./run/zh/condor
	   for dir in *
	   do
	       cd $dir
	       echo `pwd`
	       ./condor_submit.sh $njob
	       echo "Sleep 5 sec."
	       sleep 5
	       cd ../
	   done
           ;;

    0.2.7) echo "Select events on background (with a small sample)..."
	   mkdir -p   ./run/zh/events/ana
	   cd ./run/zh/ana
	   for dir in *
	   do
	       mkdir -p ../events/ana/$dir
	   done
	   cd ../../../

           ./python/sel_events.py  ./run/zh/ana/e2e2h_X/ana_File-1.root  ./run/zh/events/ana/e2e2h_X/ana_File-1_event.root ${sel_bg}
           ;;

    0.2.8) echo "Generate Condor job scripts for event selection..."
		rm -rf ./run/zh/events/ana
	   mkdir -p   ./run/zh/events/ana
	   cd ./run/zh/ana
	   for dir in *
	   do
	   	   rm -rf ../events/ana/$dir
	       mkdir -p ../events/ana/$dir
	   done

	   cd ../condor/
	   for dir in *
	   do
	       cd $dir
	       rm -rf log/events
	       rm -rf script/eventsel
	       mkdir -p log/events
	       mkdir -p script/eventsel
	       cd ../
	   done
	   
	   cd ../../../
	   ./python/gen_bg_condorscripts.py  2  ./run/zh/ana ./run/zh/condor  ${sel_bg}
           ;;

    0.2.9) echo "Submit Condor jobs for pre-selection on ZH sample..."
           cd ./run/zh/condor
	   for dir in *
	   do
	       cd $dir
	       echo `pwd`
	       ./condor_submit_eventsel.sh 
	       cd ../
	   done
           ;;

    0.2.10) echo  "Merge event root files..."
			rm -rf ./run/zh/hist
           mkdir -p   ./run/zh/hist
	   cd ./run/zh/events/ana
	   for dir in *
	   do
	       rm -rf ../../hist/$dir
	       mkdir -p ../../hist/$dir
	       cd ../../../../

	       ./python/mrg_rootfiles.py  ./run/zh/events/ana/$dir  ./run/zh/hist/$dir
	       cd ./run/zh/events/ana	       
	   done
           ;; 

    0.2.11) echo  "Plot signal-zh histograms..."
           	mkdir -p   ./doc/fig
           ./python/plt_bg.py  ./table/zh_sample_list.txt  zh
           ;; 



    # --------------------------------------------------------------------------
    #  0.3 Background Sample   
    # --------------------------------------------------------------------------

    
    0.3) echo "Running on background sample..."
         ;;

    0.3.1) echo "Split background sample with each group 20G..."
	   mkdir -p   ./run/bg/samples
	   ./python/get_bg_samples.py ./table/bg_sample_list.txt ./run/bg/samples 20G
           ;;

    0.3.2) echo "Generate XML input files for Marlin job..."
	   mkdir -p   ./run/bg/steers 
	   mkdir -p   ./run/bg/ana

           ./python/gen_bg_steerfiles.py ./table/bg_sample_list.txt ./table/template_jobfile.xml  ./run/bg/samples  ./run/bg/steers  ./run/bg/ana
           ;;

    0.3.3) echo "Check statistics : print the number of files..."
	   ./python/check_stat.py  ./table/bg_sample_list.txt ./run/bg/samples 
	   ;;
	   
    0.3.4) echo "Run with a few events ..."
	#    source setup.sh
	#    ./build.sh
	   cd ./run/bg/steers/

	   array=("e3e3" "qq" "sznu_sl0nu_down" "sze_sl0uu" "ww_sl0muq" "zz_sl0mu_down")
	   for dir in "${array[@]}"
	   do
	       cd ${dir}/test
	       Marlin sample-1.xml
	       cd ../../
	   done
           ;;

    0.3.5) echo "Generate Condor job scripts..."
	   mkdir -p   ./run/bg/condor

	   cd ./run/bg/ana/
	   for dir in *
	   do
	       mkdir -p ../condor/$dir
	   done

	   cd ../condor/
	   for dir in *
	   do
	       cd $dir
	       rm -rf log/marlin
	       rm -rf script/marlin
	       mkdir -p log/marlin
	       mkdir -p script/marlin
	       cd ../
	   done

	   cd ../../../
           ./python/gen_bg_condorscripts.py  1  ./run/bg/steers ./run/bg/condor  ${sel_signal} #1
           ;;

    0.3.6) echo "Submit Condor jobs for pre-selection on background sample..."
	   echo " ---- "
	   echo "Please enter the number of jobs for each backgrond (default: 20)" 
	   read njob
	   if [ -z $njob ]; then
	       njob=20
	   fi
	   
           cd ./run/bg/condor
	   for dir in *
	   do
	       cd $dir
	       echo `pwd`
	       ./condor_submit.sh $njob
	       cd ../
	   done
           ;;

    0.3.7) echo "Select events on background (with a small sample)..."  #only one sample
	   mkdir -p   ./run/bg/events/ana
	   cd ./run/bg/ana
	   for dir in *
	   do
	       mkdir -p ../events/ana/$dir
	   done
	   cd ../../../

           ./python/sel_events.py  ./run/bg/ana/zz_sl0mu_up/ana_File-1.root  ./run/bg/events/ana/zz_sl0mu_up/ana_File-1_event.root  ${sel_all}  #0
           ;;

    0.3.8) echo "Generate Condor job scripts for event selection..."
		rm -rf ./run/bg/events/ana
	   mkdir -p   ./run/bg/events/ana
	   cd ./run/bg/ana
	   for dir in *
	   do
	       rm -rf ../events/ana/$dir
	       mkdir -p ../events/ana/$dir
	   done

	   cd ../condor/
	   for dir in *
	   do
	       cd $dir
	       rm -rf log/events
	       rm -rf script/eventsel
	       mkdir -p log/events
	       mkdir -p script/eventsel
	       cd ../
	   done
	   
	   cd ../../../
	   ./python/gen_bg_condorscripts.py  2  ./run/bg/ana ./run/bg/condor  ${sel_all}
           ;;

    0.3.9) echo "Submit Condor jobs for pre-selection on background sample..."
           cd ./run/bg/condor
	   for dir in *
	   do
	       cd $dir
	       echo `pwd`
	       ./condor_submit_eventsel.sh 
	       cd ../
	   done
           ;;

    0.3.10) echo  "Merge event root files..."
		   rm -rf ./run/bg/hist
           mkdir -p   ./run/bg/hist
	   cd ./run/bg/events/ana
	   for dir in *
	   do
	       rm -rf ../../hist/$dir
	       mkdir -p ../../hist/$dir
	       cd ../../../../

	       ./python/mrg_rootfiles.py  ./run/bg/events/ana/$dir  ./run/bg/hist/$dir
	       cd ./run/bg/events/ana	       
	   done
           ;; 


    0.3.11) echo  "Plot signal-bg histograms..."
           	mkdir -p   ./doc/fig
           ./python/plt_bg.py  ./table/bg_sample_list.txt  bg
           ;; 

    # --------------------------------------------------------------------------
    #  0.4 nnHiggs Sample   
    # --------------------------------------------------------------------------

    0.4) echo "Running on signal sample..."
         ;;

    0.4.1) echo "Split signal sample with each group 1G..."
	   mkdir -p   ./run/nnh2zz/samples
           ./python/get_samples.py  ${nnhzz_slcio_dir} ./run/nnh2zz/samples/E240_Pnnh_zz.txt 1G
           ;;

    0.4.2) echo "Generate XML input files for Marlin job..."
	   mkdir -p   ./run/nnh2zz/steers 
	   mkdir -p   ./run/nnh2zz/steers/test 
	   mkdir -p   ./run/nnh2zz/ana
           ./python/gen_steerfiles.py ./table/template_jobfile.xml ./run/nnh2zz/samples ./run/nnh2zz/steers ./run/nnh2zz/ana/ana_File.root
           ;;

    0.4.3) echo "Run with a few events ..."
	   source setup.sh
	   ./build.sh
	   Marlin ./run/nnh2zz/steers/test/sample-1.xml
           ;;
    
    0.4.4) echo "Generate Condor job scripts..."
	   mkdir -p   ./run/nnh2zz/condor/script/marlin
           ./python/gen_condorscripts.py  1  ./run/nnh2zz/steers ./run/nnh2zz/condor  ${sel_signal}
           ;;

    0.4.5) echo "Submit Condor jobs for pre-selection on signal..."
           cd ./run/nnh2zz/condor
	   mkdir -p log
	   ./condor_submit.sh
           ;;

    0.4.6) echo "Select events on signal (with a small sample)..."
	   mkdir -p   ./run/nnh2zz/events/ana
           ./python/sel_events.py  ./run/nnh2zz/ana/ana_File-1.root  ./run/nnh2zz/events/ana/ana_File-1_event.root  ${sel_all}
           ;;

    0.4.7) echo "Generate Condor job scripts for event selection..."
	   mkdir -p   ./run/nnh2zz/events/ana
           mkdir -p   ./run/nnh2zz/condor/script/eventsel
	   ./python/gen_condorscripts.py  2  ./run/nnh2zz/ana ./run/nnh2zz/condor  ${sel_all}
           ;;

    0.4.8) echo "Submit Condor jobs for event selection on signal..."
           cd ./run/nnh2zz/condor
	   mkdir -p log/events
	   ./condor_submit_eventsel.sh
           ;;

    0.4.9) echo  "Merge event root files..."
           mkdir -p   ./run/nnh2zz/hist
           ./python/mrg_rootfiles.py  ./run/nnh2zz/events/ana  ./run/nnh2zz/hist 
           ;; 


    # --------------------------------------------------------------------------
    #  0.5 mmHWW Sample   
    # --------------------------------------------------------------------------

    0.5) echo "Running on mmHWW sample..."
         ;;

    0.5.1) echo "Split mmHWW sample with each group 1G..."
	   mkdir -p   ./run/mmh2ww/samples
           ./python/get_samples.py  ${mmh2ww_slcio_dir} ./run/mmh2ww/samples/E240_Pnnh_zz.txt 1G
           ;;

    0.5.2) echo "Generate XML input files for Marlin job..."
	   mkdir -p   ./run/mmh2ww/steers 
	   mkdir -p   ./run/mmh2ww/steers/test 
	   mkdir -p   ./run/mmh2ww/ana
           ./python/gen_steerfiles.py ./table/template_jobfile.xml ./run/mmh2ww/samples ./run/mmh2ww/steers ./run/mmh2ww/ana/ana_File.root
           ;;

    0.5.3) echo "Run with a few events ..."
	   source setup.sh
	   ./build.sh
	   Marlin ./run/mmh2ww/steers/test/sample-1.xml
           ;;
    
    0.5.4) echo "Generate Condor job scripts..."
	   mkdir -p   ./run/mmh2ww/condor/script/marlin
           ./python/gen_condorscripts.py  1  ./run/mmh2ww/steers ./run/mmh2ww/condor  ${sel_signal}
           ;;

    0.5.5) echo "Submit Condor jobs for pre-selection on mmHWW sample..."
           cd ./run/mmh2ww/condor
	   mkdir -p log
	   ./condor_submit.sh
           ;;

    0.5.6) echo "Select events on mmHWW sample (with a small sample)..."
	   mkdir -p   ./run/mmh2ww/events/ana
           ./python/sel_events.py  ./run/mmh2ww/ana/ana_File-1.root  ./run/mmh2ww/events/ana/ana_File-1_event.root  ${sel_all}
           ;;

    0.5.7) echo "Generate Condor job scripts for event selection..."
	   mkdir -p   ./run/mmh2ww/events/ana
           mkdir -p   ./run/mmh2ww/condor/script/eventsel
	   ./python/gen_condorscripts.py  2  ./run/mmh2ww/ana ./run/mmh2ww/condor  ${sel_all}
           ;;

    0.5.8) echo "Submit Condor jobs for event selection on mmHWW sample..."
           cd ./run/mmh2ww/condor
	   mkdir -p log/events
	   ./condor_submit_eventsel.sh
           ;;

    0.5.9) echo  "Merge event root files..."
           mkdir -p   ./run/mmh2ww/hist
           ./python/mrg_rootfiles.py  ./run/mmh2ww/events/ana  ./run/mmh2ww/hist 
           ;; 


    # --------------------------------------------------------------------------
    #  0.6 mmHZZ Sample   
    # --------------------------------------------------------------------------

    0.6) echo "Running on mmHZZ sample..."
         ;;

    0.6.1) echo "Split mmHZZ sample with each group 1G..."
	   mkdir -p   ./run/mmh2zz/samples
           ./python/get_samples.py  ${mmh2zz_slcio_dir} ./run/mmh2zz/samples/E240_Pnnh_zz.txt 1G
           ;;

    0.6.2) echo "Generate XML input files for Marlin job..."
	   mkdir -p   ./run/mmh2zz/steers 
	   mkdir -p   ./run/mmh2zz/steers/test 
	   mkdir -p   ./run/mmh2zz/ana
           ./python/gen_steerfiles.py ./table/template_jobfile.xml ./run/mmh2zz/samples ./run/mmh2zz/steers ./run/mmh2zz/ana/ana_File.root
           ;;

    0.6.3) echo "Run with a few events ..."
	   source setup.sh
	   ./build.sh
	   Marlin ./run/mmh2zz/steers/test/sample-1.xml
           ;;
    
    0.6.4) echo "Generate Condor job scripts..."
	   mkdir -p   ./run/mmh2zz/condor/script/marlin
           ./python/gen_condorscripts.py  1  ./run/mmh2zz/steers ./run/mmh2zz/condor  ${sel_signal}
           ;;

    0.6.5) echo "Submit Condor jobs for pre-selection on signal..."
           cd ./run/mmh2zz/condor
	   mkdir -p log
	   ./condor_submit.sh
           ;;

    0.6.6) echo "Select events on mmHZZ sample (with a small sample)..."
	   mkdir -p   ./run/mmh2zz/events/ana
           ./python/sel_events.py  ./run/mmh2zz/ana/ana_File-1.root  ./run/mmh2zz/events/ana/ana_File-1_event.root  ${sel_all}
           ;;

    0.6.7) echo "Generate Condor job scripts for event selection..."
	   mkdir -p   ./run/mmh2zz/events/ana
           mkdir -p   ./run/mmh2zz/condor/script/eventsel
	   ./python/gen_condorscripts.py  2  ./run/mmh2zz/ana ./run/mmh2zz/condor  ${sel_all}
           ;;

    0.6.8) echo "Submit Condor jobs for event selection on mmHZZ sample..."
           cd ./run/mmh2zz/condor
	   mkdir -p log/events
	   ./condor_submit_eventsel.sh
           ;;

    0.6.9) echo  "Merge event root files..."
           mkdir -p   ./run/mmh2zz/hist
           ./python/mrg_rootfiles.py  ./run/mmh2zz/events/ana  ./run/mmh2zz/hist 
           ;; 


    # --------------------------------------------------------------------------
    #  0.7 mmHtautau Sample   
    # --------------------------------------------------------------------------

    0.7) echo "Running on mmHtautau sample..."
         ;;

    0.7.1) echo "Split signal sample with each group 1G..."
	   mkdir -p   ./run/mmh2tt/samples
           ./python/get_samples.py  ${mmh2tt_slcio_dir} ./run/mmh2tt/samples/E240_Pnnh_zz.txt 1G
           ;;

    0.7.2) echo "Generate XML input files for Marlin job..."
	   mkdir -p   ./run/mmh2tt/steers 
	   mkdir -p   ./run/mmh2tt/steers/test 
	   mkdir -p   ./run/mmh2tt/ana
           ./python/gen_steerfiles.py ./table/template_jobfile.xml ./run/mmh2tt/samples ./run/mmh2tt/steers ./run/mmh2tt/ana/ana_File.root
           ;;

    0.7.3) echo "Run with a few events ..."
	   source setup.sh
	   ./build.sh
	   Marlin ./run/mmh2tt/steers/test/sample-1.xml
           ;;
    
    0.7.4) echo "Generate Condor job scripts..."
	   mkdir -p   ./run/mmh2tt/condor/script/marlin
           ./python/gen_condorscripts.py  1  ./run/mmh2tt/steers ./run/mmh2tt/condor  ${sel_signal}
           ;;

    0.7.5) echo "Submit Condor jobs for pre-selection on mmHtautau sample..."
           cd ./run/mmh2tt/condor
	   mkdir -p log
	   ./condor_submit.sh
           ;;

    0.7.6) echo "Select events on mmHtautau (with a small sample)..."
	   mkdir -p   ./run/mmh2tt/events/ana
           ./python/sel_events.py  ./run/mmh2tt/ana/ana_File-1.root  ./run/mmh2tt/events/ana/ana_File-1_event.root  ${sel_all}
           ;;

    0.7.7) echo "Generate Condor job scripts for event selection..."
	   mkdir -p   ./run/mmh2tt/events/ana
           mkdir -p   ./run/mmh2tt/condor/script/eventsel
	   ./python/gen_condorscripts.py  2  ./run/mmh2tt/ana ./run/mmh2tt/condor  ${sel_all}
           ;;

    0.7.8) echo "Submit Condor jobs for event selection on mmHtautau sample..."
           cd ./run/mmh2tt/condor
	   mkdir -p log/events
	   ./condor_submit_eventsel.sh
           ;;

    0.7.9) echo  "Merge event root files..."
           mkdir -p   ./run/mmh2tt/hist
           ./python/mrg_rootfiles.py  ./run/mmh2tt/events/ana  ./run/mmh2tt/hist 
           ;; 


esac

