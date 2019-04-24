source setup.sh
make

fitScan -f ../workspace/out/workspace/cepc_5.root  -n nuis* -p mu_zz=1_-5_5  --hesse 1 --minos 1 -o outs/singleFit/singleFit_CEPC-mzjv.root
