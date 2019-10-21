g++ `root-config --cflags --ldflags --glibs` -Wall -g  -fPIC -c src/RooGaussExp.cxx -o lib/RooGaussExp.o -lRooFitCore -lRooFit -lRooStats -I inc -std=c++14
g++ `root-config --cflags --ldflags --glibs` -shared lib/RooGaussExp.o -o lib/libRooGaussExp.so -lRooFitCore -lRooFit -lRooStats -I inc -std=c++14
g++ `root-config --cflags --ldflags --glibs` -Wall -g  -fPIC -c src/RooGaussDoubleSidedExp.cxx -o lib/RooGaussDoubleSidedExp.o -lRooFitCore -lRooFit -lRooStats -I inc -std=c++14
g++ `root-config --cflags --ldflags --glibs` -shared lib/RooGaussDoubleSidedExp.o -o lib/libRooGaussDoubleSidedExp.so -lRooFitCore -lRooFit -lRooStats -I inc -std=c++14
g++ `root-config --cflags --ldflags --glibs` -Wall -g  -fPIC -c src/HggTwoSidedCBPdf.cxx -o lib/HggTwoSidedCBPdf.o -lRooFitCore -lRooFit -lRooStats -I inc -std=c++14
g++ `root-config --cflags --ldflags --glibs` -shared lib/HggTwoSidedCBPdf.o -o lib/libHggTwoSidedCBPdf.so -lRooFitCore -lRooFit -lRooStats -I inc -std=c++14
