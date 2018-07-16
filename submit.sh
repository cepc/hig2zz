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
#	printf "\n\t%-9s  %-40s"  "0.1.10"   "Plot histograms" 

	printf "\n" 
	printf "\n\t%-9s  %-40s"  "0.2"      "[run ZH inclusive sample]" 

	printf "\n" 
	printf "\n\t%-9s  %-40s"  "0.3"      "[run background sample]" 
	printf "\n\t%-9s  %-40s"  "0.3.1"    "Split background sample with each group 1G" 
	printf "\n\t%-9s  %-40s"  "0.3.2"    "Generate XML input files for Marlin job" 
	printf "\n\t%-9s  %-40s"  "0.3.3"    "Check the number files" 
	printf "\n\t%-9s  %-40s"  "0.3.4"    "Run with a few events" 
	printf "\n\t%-9s  %-40s"  "0.3.5"    "Generate Condor job scripts for pre-selection" 
	printf "\n\t%-9s  %-40s"  "0.3.6"    "Submit Condor jobs for pre-selection on Bg sample" 
	printf "\n\t%-9s  %-40s"  "0.3.7"    "Select events on background (with a small sample)"
	printf "\n\t%-9s  %-40s"  "0.3.8"    "Generate Condor job scripts for event selection" 	
	printf "\n\t%-9s  %-40s"  "0.3.9"    "Submit Condor jobs for event selection on Bg sample" 
	printf "\n\t%-9s  %-40s"  "0.3.10"    "Merge event root files" 
#	printf "\n\t%-9s  %-40s"  "0.3.11"   "Plot histograms" 
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
           ./python/gen_condorscripts.py  1  ./run/llh2zz/steers ./run/llh2zz/condor
           ;;

    0.1.5) echo "Submit Condor jobs for pre-selection on signal..."
           cd ./run/llh2zz/condor
	   mkdir -p log
	   ./condor_submit.sh
           ;;

    0.1.6) echo "Select events on signal (with a small sample)..."
	   mkdir -p   ./run/llh2zz/events/ana
           ./python/sel_events.py  ./run/llh2zz/ana/ana_File-1.root  ./run/llh2zz/events/ana/ana_File_events-1.root
           ;;

    0.1.7) echo "Generate Condor job scripts for event selection..."
	   mkdir -p   ./run/llh2zz/events/ana
           mkdir -p   ./run/llh2zz/condor/script/eventsel
	   ./python/gen_condorscripts.py  2  ./run/llh2zz/ana ./run/llh2zz/condor
           ;;

    0.1.8) echo "Submit Condor jobs for event selection on signal..."
           cd ./run/llh2zz/condor
	   mkdir -p log/events
	   ./condor_submit_eventsel.sh
           ;;

    0.1.9) echo  "Merge event root files..."
           mkdir -p   ./run/llh2zz/hist
           ./python/mrg_rootfiles.py  ./run/llh2zz/events/ana  ./run/llh2zz/hist 
           ;; 

#    0.1.10) echo  "Plot histograms..."
#           ./python/plt_summary.py    ./run/ll_h2zz/hist/ 
#           ;; 


    # --------------------------------------------------------------------------
    #  0.2 ZH Inclusive Sample   
    # --------------------------------------------------------------------------


    0.2) echo "Running on ZH inclusive sample..."
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
	   source setup.sh
	   ./build.sh
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
           ./python/gen_bg_condorscripts.py  1  ./run/bg/steers ./run/bg/condor
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

    0.3.7) echo "Select events on background (with a small sample)..."
	   mkdir -p   ./run/bg/events/ana
	   cd ./run/bg/ana
	   for dir in *
	   do
	       mkdir -p ../events/ana/$dir
	   done
	   cd ../../../

           ./python/sel_events.py  ./run/bg/ana/zz_sl0mu_up/ana_File-1.root  ./run/bg/events/ana/zz_sl0mu_up/ana_File_events-1.root
           ;;

    0.3.8) echo "Generate Condor job scripts for event selection..."
	   mkdir -p   ./run/bg/events/ana
	   cd ./run/bg/ana
	   for dir in *
	   do
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
	   ./python/gen_bg_condorscripts.py  2  ./run/bg/ana ./run/bg/condor
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
           mkdir -p   ./run/bg/hist
	   cd ./run/bg/events/ana
	   for dir in *
	   do
	       mkdir -p ../../hist/$dir
	       cd ../../../../

	       ./python/mrg_rootfiles.py  ./run/bg/events/ana/$dir  ./run/bg/hist/$dir
	       cd ./run/bg/events/ana	       
	   done
           ;; 


esac

