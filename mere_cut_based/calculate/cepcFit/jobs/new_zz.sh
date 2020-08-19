# setup root
source setup.sh

# make
make


#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzvj_s=1_-5_5,mzvj_zz=1_-5_5,mzvj_ww=1_-5_5,mzvj_tt=1_-5_5,mzjv_s=1_-5_5,mzjv_zz=1_-5_5,mzjv_ww=1_-5_5,mzjv_tt=1_-5_5,mzjv_bb=1_-5_5,mzjv_cc=1_-5_5,mzjv_gg=1_-5_5,vzmj_s=1_-5_5,vzmj_zz=1_-5_5,vzmj_ww=1_-5_5,vzjm_s=1_-5_5,vzjm_zz=1_-5_5,vzjm_ww=1_-5_5,vzjm_tt=1_-5_5,vzjm_bb=1_-5_5,qzvm_s=1_-5_5,qzvm_zz=1_-5_5,qzvm_ww=1_-5_5,qzvm_tt=1_-5_5,qzvm_bb=1_-5_5,qzmv_s=1_-5_5,qzmv_zz=1_-5_5,qzmv_ww=1_-5_5,qzmv_tt=1_-5_5,qzmv_bb=1_-5_5,qzmv_cc=1_-5_5  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root
#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mu_s=1_-5_5,mu_zz=1_-5_5,mu_ww=1_-5_5,mu_tt=1_-5_5,mu_bb=1_-5_5,mu_cc=1_-5_5  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-mu_s.root

fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzvj_s=1_-5_5,mzjv_s=1_-5_5,vzmj_s=1_-5_5,vzjm_s=1_-5_5,qzmv_s=1_-5_5,qzvm_s=1_-5_5  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root

#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzvj_s=1_-5_5,mzjv_s=1_-5_5,vzmj_s=1_-5_5,vzjm_s=1_-5_5,qzmv_s=1_-5_5,qzvm_s=1_-5_5,mzvj_so=1_-10_10,mzjv_so=1_-10_10,vzmj_so=1_-10_10,vzjm_so=1_-10_10,qzmv_so=1_-50_50,qzvm_so=1_-10_10  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root

#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mu_s=1_-5_5,mu_zz=1_-2_2,mu_ww=1_-2_2,mu_tt=1_-2_2,mu_bb=1_-2_2  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-mu_s.root

fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mu_s=1_-5_5  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-mu_s.root
