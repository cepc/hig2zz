# setup root
source setup.sh

# make
make


fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mzvj_s=1_-5_5,mzjv_s=1_-5_5,vzmj_s=1_-5_5,vzjm_s=1_-5_5,qzmv_s=1_-5_5,qzvm_s=1_-5_5  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-zz.root
fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mu_s=1_-5_5  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-mu_s.root

