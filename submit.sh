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
	printf "\nDATE\n"
	printf "\n\t%-5s\n" "AUGUST 2016"     
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

    0.1.1) echo "Split signal sample with each group 1G..."
	   mkdir -p   ./run/llh2zz/samples
           ./python/get_samples.py  ${signal_slcio_dir} ./run/llh2zz/samples/E240_Pllh_zz.txt 0.5G
           ;;

    0.1.2) echo "Generate XML input files for Marlin job..."
	   mkdir -p   ./run/llh2zz/steers 
	   mkdir -p   ./run/llh2zz/steers/test 
	   mkdir -p   ./run/llh2zz/ana
           ./python/gen_steerfiles.py ./steer/template_job_20180605.xml ./run/llh2zz/samples ./run/llh2zz/steers ./run/llh2zz/ana/ana_File.root
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

esac

