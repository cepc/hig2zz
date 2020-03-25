make mu


./bin/mu cepc mubr              > out/log/mubr
./bin/mu cepc mubr,noSys        > out/log/mubr_noSys
# ./bin/mu cepc individual        > out/log/individual
# ./bin/mu cepc individual,noSys  > out/log/individual_noSys
# ./bin/mu cepc k9,noSys          > out/log/k9
# ./bin/mu cepc k8,noSys          > out/log/k8
# ./bin/mu cepc k7,noSys          > out/log/k7
# ./bin/mu cepc k2,noSys          > out/log/k2
# ./bin/mu cepc inclusive,noSys   > out/log/inclusive_noSys
# ./bin/mu cepc inclusive         > out/log/inclusive


echo "mubr_cepc"                                >cepc_summary.log
tail -25 out/log/mubr                           >>cepc_summary.log
echo "mubr_cepc_noSys"                          >>cepc_summary.log
tail -20 out/log/mubr_noSys                     >>cepc_summary.log