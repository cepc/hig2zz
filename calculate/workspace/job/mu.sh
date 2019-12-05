make mu


./bin/mu cepc_5 mubr                > out/log/mubr
./bin/mu cepc_5 mubr,noSys          > out/log/mubr_noSys
./bin/mu cepc_5 individual,noSys    > out/log/individual_noSys
# ./bin/mu cepc individual         > out/log/individual

./bin/mu cepc_0.5 k7,noSys            > out/log/k7_0.5
./bin/mu cepc_2 k7,noSys              > out/log/k7_2
./bin/mu cepc_10 k7,noSys             > out/log/k7_10
./bin/mu cepc_5 k7,noSys              > out/log/k7

./bin/mu cepc_0.5 k8,noSys            > out/log/k8_0.5
./bin/mu cepc_2 k8,noSys              > out/log/k8_2
./bin/mu cepc_10 k8,noSys             > out/log/k8_10
./bin/mu cepc_5 k8,noSys              > out/log/k8


echo "mubr_cepc"                                >cepc_summary.log
tail -25 out/log/mubr                           >>cepc_summary.log
echo "mubr_cepc_noSys"                          >>cepc_summary.log
tail -20 out/log/mubr_noSys                     >>cepc_summary.log
# echo "individual_cepc"                          >>cepc_summary.log
# tail -40 out/log/individual                     >>cepc_summary.log
echo "individual_cepc_noSys"                    >>cepc_summary.log
tail -40 out/log/individual_noSys               >>cepc_summary.log
echo "k7_5"                                       >>cepc_summary.log
tail -20 out/log/k7                             >>cepc_summary.log
echo "k7_0.5"                                       >>cepc_summary.log
tail -20 out/log/k7_0.5                             >>cepc_summary.log
echo "k7_2"                                       >>cepc_summary.log
tail -20 out/log/k7_2                             >>cepc_summary.log
echo "k7_10"                                       >>cepc_summary.log
tail -20 out/log/k7_10                             >>cepc_summary.log

echo "k8_5"                                       >>cepc_summary.log
tail -20 out/log/k8                             >>cepc_summary.log
echo "k8_0.5"                                       >>cepc_summary.log
tail -20 out/log/k8_0.5                             >>cepc_summary.log
echo "k8_2"                                       >>cepc_summary.log
tail -20 out/log/k8_2                             >>cepc_summary.log
echo "k8_10"                                       >>cepc_summary.log
tail -20 out/log/k8_10                             >>cepc_summary.log