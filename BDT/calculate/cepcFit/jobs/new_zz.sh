# setup root
source setup.sh

# make
make

#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzvj_s=1_-10_10  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root
#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzjv_s=1_-10_10  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root

#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzvj_so=1_-10_10  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root
#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzjv_so=1_-10_10  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root

#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzvj_s=1_-10_10,mzvj_so=1_-10_10  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root
#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzvj_s=1_-5_5,mzjv_s=1_-5_5,vzmj_s=1_-5_5,vzjm_s=1_-5_5,qzmv_s=1_-5_5,qzvm_s=1_-5_5  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root

#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzvj_s=1_-5_5,mzjv_s=1_-5_5,vzmj_s=1_-5_5,vzjm_s=1_-5_5,qzmv_s=1_-5_5,qzvm_s=1_-5_5,mzvj_so=1_-10_10,mzjv_so=1_-10_10,vzmj_so=1_-10_10,vzjm_so=1_-10_10,qzmv_so=1_-50_50,qzvm_so=1_-10_10  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root

#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzvj_s=1_-5_5,mzjv_s=1_-5_5  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root
fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mu_s=1_-5_5  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-mu_s.root
#fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mu_s=1_-5_5,mu_zz=1_-5_5,mu_ww=1_-5_5,mu_bb=1_-5_5,mu_tt=1_-5_5  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-mu_s.root
