#ifndef SHAPE_H
#define SHAPE_H


bool is250=false;
bool isuseexistingpdf=false;
    // const int Nch = 58;
    const int Nch = 1;
    const TString m_CN[Nch] = {  
                                //  "mmyy", "qqyy", "vvyy",
                                //  "eemm", "mmmm", "qqmm", "vvmm",
                                //  "eweq", "ewmq", "ewlv",
                                //  "mweq", "mwmq", "mwlv",
                                //  "vvevev", "vvevmv", "vvmvmv",
                                //  "qw4q", "vw4q", 
                                //  "minc_mi", "minc_md", "einc_mi", "einc_md",
                                //  "vweq", "vwmq",
                                //  "vzej",
                                //   "vz",
                                //   "mzvj",           
                                //  "mmtt", "qqtt", "eett", "vvtt",
                                //  "eeqq", "mmqq", 
                                //  "qqqq", "vvqq", 
                                //  "vvhbb",                        
                                 
                                //  "qz4v", "ez4v", 
                                 
                                // "mzvj",  
                                // "mzjv"
                                // "vzjm"
                                 "qzvm",
                                // "qzmv"      
                                //  "eeqq_inv",
                                //  "qw4q_rec", "vw4q_rec", "qqqq_rec", "vvqq_rec",
                                //  "mcom",
                                  
                                //  "mmyy_rll", "mmyy_rec", "qqyy_rec", "vvyy_rec",
                                //  "eeqq_rec", "mmqq_rec", 
                                //  "mmtt_imp", "qqtt_imp", "eett_imp", "vvtt_imp",    
                                // //>56: for plot 
                                // //  "mz4v_jmq", 
                                // "qqzy",
                                // "einc_zhaoh", "minc_zhaoh",
                                // "vvyy_base",  
                                // "vvyy_simp",
                                // "vvmm_zhaoh",
                                // "vvbb_inv", "vvbb_rec",
                                // "vvcc_inv", "vvcc_rec",
                                // "vvgg_inv", "vvgg_rec",
                                // "zzbb_inv", "zzcc_inv", "zzgg_inv",
                                // "zzbb_rec", "zzcc_rec", "zzgg_rec",
                                 };
    // const int Nch = 4;
    // const TString m_CN[Nch] = {  
    //                             //  "mmtt", "qqtt", "eett", "vvtt",
    //                              "eeqq", "mmqq", 
    //                              "qqqq", "vvqq", 
    //                             //  "vvhbb",
    //                             //  "mmyy", "qqyy", "vvyy",
    //                             //  "eemm", "mmmm", "qqmm", "vvmm",
    //                             //  "eweq", "ewmq", "ewlv",
    //                             //  "mweq", "mwmq", "mwlv",
    //                             //  "vvevev", "vvevmv", "vvmvmv",
    //                             //  "qw4q", "vw4q", "vweq", "vwmq",
    //                             //  "vzej", "vzmj", "mzvj",
    //                             //  "qqzy", 
    //                             //  "qz4v", "ez4v", "mz4v",
    //                              };
    //36 channels for combination

typedef struct
{
    TString name;
    int nsig=1;
    int nbkg=1;
    Float_t mlow=120;
    Float_t mhigh=150;
    TString f_bkg;
    //vector<TString> name_sig;       
    TString name_sig[10];
    map<TString, TString> f_sig;    
} channel;

const channel c[150]=
{
    //  "mz4v_jmq", "einc_zhaoh"
    {   "mz4v_jmq", 1, 1, 120, 140,
        // "data/haa/qqyy_bkg_103.root",
        "data/hinvi/jingmq/mz4v_bkg.root",
        {"s"},
        {
            {"s",   "data/hinvi/jingmq/mz4v_sig.root"}
        }
    },
    {   "einc_zhaoh", 1, 0, 120, 200,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/einc_zhaoh.root"}
        }
    },
    {   "minc_zhaoh", 1, 0, 120, 170,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/minc_zhaoh.root"}
        }
    },
    {   "vvmm_zhaoh", 1, 0, 120, 130,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/v4_vvmm.root"}
        }
    },
    {   "vvyy_base", 1, 0, 80, 140,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/v4_vvyy.root"}
        }
    },
    {   "vvyy_simp", 1, 0, 80, 140,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/simp_vvyy.root"}
        }
    },
    {   "vvbb_inv", 1, 0, 60, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/bb.root"}
        }
    },
    {   "vvcc_inv", 1, 0, 60, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/cc.root"}
        }
    },
    {   "vvgg_inv", 1, 0, 60, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/gg.root"}
        }
    },
    {   "vvbb_rec", 1, 0, 60, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/bb.root"}
        }
    },
    {   "vvcc_rec", 1, 0, 60, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/cc.root"}
        }
    },
    {   "vvgg_rec", 1, 0, 60, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/gg.root"}
        }
    },
    {   "zzbb_inv", 1, 0, 60, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/lg_bb.root"}
        }
    },
    {   "zzcc_inv", 1, 0, 60, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/lg_cc.root"}
        }
    },
    {   "zzgg_inv", 1, 0, 60, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/lg_gg.root"}
        }
    },
    {   "zzbb_rec", 1, 0, 20, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/lg_bb.root"}
        }
    },
    {   "zzcc_rec", 1, 0, 20, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/lg_cc.root"}
        }
    },
    {   "zzgg_rec", 1, 0, 20, 160,
        // "data/haa/qqyy_bkg_103.root",
        // "data/einc_zhaoh.root",
        "",
        {"s"},
        {
            {"s",   "data/lg_gg.root"}
        }
    },
    {   "qqyy", 1, 1, 113, 140,
        // "data/haa/qqyy_bkg_103.root",
        "data/haa/3t/qqyy_bkg.root",
        {"s"},
        {
            {"s",   "data/haa/3t/qqyy_sig.root"}
        }
    },
    {   "qw4q", 5, 1, 
            // 75, 130,
            100,150,
        "data/WW/qqqqqq/sm_3.root",
        {"ww", "bb", "cc", "gg", "zz"},
        {
            {"ww",   "data/WW/qqqqqq/ww.root"},
            {"bb",  "data/WW/qqqqqq/bb.root"},
            {"cc",  "data/WW/qqqqqq/cc.root"},
            {"gg",  "data/WW/qqqqqq/gg.root"},
            {"zz",  "data/WW/qqqqqq/zz.root"},
        }
    },
    {   "qw4q_rec", 5, 1, 
            65, 115,
            // 100,150,
        "data/WW/qqqqqq/sm_3.root",
        {"ww", "bb", "cc", "gg", "zz"},
        {
            {"ww",   "data/WW/qqqqqq/ww.root"},
            {"bb",  "data/WW/qqqqqq/bb.root"},
            {"cc",  "data/WW/qqqqqq/cc.root"},
            {"gg",  "data/WW/qqqqqq/gg.root"},
            {"zz",  "data/WW/qqqqqq/zz.root"},
        }
    },
    {   "vw4q", 5, 1, 
            // 75, 130,
            100,150,
        "data/WW/nnH_new/sm.root",
        {"ww", "bb", "cc", "gg", "zz"},
        {
            {"ww",   "data/WW/nnH_new/ww.root"},
            {"bb",  "data/WW/nnH_new/bb.root"},
            {"cc",  "data/WW/nnH_new/cc.root"},
            {"gg",  "data/WW/nnH_new/gg.root"},
            {"zz",  "data/WW/nnH_new/zz.root"}
        }
    },
    {   "vw4q_rec", 5, 1, 
            75, 125,
            // 100,150,
        "data/WW/nnH_new/sm.root",
        {"ww", "bb", "cc", "gg", "zz"},
        {
            {"ww",   "data/WW/nnH_new/ww.root"},
            {"bb",  "data/WW/nnH_new/bb.root"},
            {"cc",  "data/WW/nnH_new/cc.root"},
            {"gg",  "data/WW/nnH_new/gg.root"},
            {"zz",  "data/WW/nnH_new/zz.root"}
        }
    },
    {   "qqzy", 0, 0,          //  n_bkg 被用于判断n_b， 为方便另qqzy的 n_bkg为0. 
        // 0, 100,             //  fit 时要求不能有空bin  拟合/作图两套
        20, 70,
        "data/zgamma.root",
        {"s"},
        {
            {"s",   "data/zgamma.root"}
        }
    },
    {   "minc_mi", 1, 1,                     
        120, 140,
        "data/inclusive/mm_mi_bkg.root",
        {"s"},
        {
            {"s",   "data/inclusive/mm_mi_signal.root"}
        }
    },
    {   "minc_md", 1, 1,                     
        120, 140,
        "data/inclusive/mm_md_bkg.root",
        {"s"},
        {
            {"s",   "data/inclusive/mm_md_signal.root"}
        }
    },
    {   "einc_mi", 1, 1,                     
        120, 140,
        "data/inclusive/ee_mi_bkg.root",
        {"s"},
        {
            {"s",   "data/inclusive/ee_mi_signal.root"}
        }
    },
    {   "einc_md", 1, 1,                     
        120, 140,
        "data/inclusive/ee_md_bkg.root",
        {"s"},
        {
            {"s",   "data/inclusive/ee_md_signal.root"}
        }
    },
    {   "mmyy", 1, 1, 115, 135,
        "data/haa/3t/mmyy_bkg_3tcut.root",
        {"s"},
        {
            {"s",   "data/haa/3t/mmyy_sig_3tcut.root"}
            // {"s",   "data/haa/llyy_sig.root"}
        }
    },
    {   "mmyy_rec", 1, 1, 86, 100,
        "data/haa/3t/mmyy_bkg_3tcut.root",
        {"s"},
        {
            {"s",   "data/haa/3t/mmyy_sig_3tcut.root"}
            // {"s",   "data/haa/llyy_sig.root"}
        }
    },
    {   "mmyy_rll", 1, 1, 105, 145,
        "data/haa/3t/mmyy_bkg_3tcut.root",
        {"s"},
        {
            {"s",   "data/haa/3t/mmyy_sig_3tcut.root"}
            // {"s",   "data/haa/llyy_sig.root"}
        }
    },
    {   "qqyy_rec", 1, 1, 70, 120,
        // "data/haa/qqyy_bkg_103.root",
        "data/haa/3t/qqyy_bkg.root",
        {"s"},
        {
            {"s",   "data/haa/3t/qqyy_sig.root"}
        }
    },
    {   "vvyy", 1, 1, 110, 140,
        "data/haa/3t/vvyy_bkg.root",    //bkg已经加倍
        {"s"},
        {
            {"s",   "data/haa/3t/vvyy_sig.root"}
            // {"s",   "data/haa/vvyy_sig.root"}
        }
    },
    {   "vvyy_rec", 1, 1, 70, 110,
        "data/haa/3t/vvyy_bkg.root",
        {"s"},
        {
            {"s",   "data/haa/3t/vvyy_sig.root"}
        }
    },
    {   "eeqq", 6, 1, 
        115, 140,//H
        // 50, 160,    //Z
        // "data/hqq/3d/ee/sm.root",
        "data/hqq/3d/ee/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            
            {"bb",  "data/hqq/3d/ee/bb.root"},
            {"cc",  "data/hqq/3d/ee/cc.root"},
            {"gg",  "data/hqq/3d/ee/gg.root"},
            {"ww",  "data/hqq/3d/ee/ww.root"},
            {"zz",  "data/hqq/3d/ee/zz.root"},
            {"tt",  "data/hqq/3d/ee/tt.root"}
        // 120,140,
        // "data/hqq/eeh/sm.root",
        // {"bb", "cc", "gg", "ww", "zz", "tt"},
        // {
            
        //     {"bb",  "data/hqq/eeh/bb.root"},
        //     {"cc",  "data/hqq/eeh/cc.root"},
        //     {"gg",  "data/hqq/eeh/gg.root"},
        //     {"ww",  "data/hqq/eeh/ww.root"},
        //     {"zz",  "data/hqq/eeh/zz.root"},
        //     {"tt",  "data/hqq/eeh/tt.root"}
        }
    },
    {   "mmqq", 6, 1, 
        120, 140,//H
        // 50, 160,    //Z
        "data/hqq/3d/mm/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            {"bb",  "data/hqq/3d/mm/bb.root"},
            {"cc",  "data/hqq/3d/mm/cc.root"},
            {"gg",  "data/hqq/3d/mm/gg.root"},
            {"ww",  "data/hqq/3d/mm/ww.root"},
            {"zz",  "data/hqq/3d/mm/zz.root"},
            {"tt",  "data/hqq/3d/mm/tt.root"}
        }

    },
    {   "qqqq", 6, 1, 
        // 120, 150, //H
        100,150,
        "data/hqq/qqh_cg/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            {"bb",  "data/hqq/qqh_cg/bb.root"},
            {"cc",  "data/hqq/qqh_cg/cc.root"},
            {"gg",  "data/hqq/qqh_cg/gg.root"},
            {"ww",  "data/hqq/qqh_cg/ww.root"},
            {"zz",  "data/hqq/qqh_cg/zz.root"},
            {"tt",  "data/hqq/qqh_cg/tt.root"}
        }
    },
    {   "vvqq", 6, 1, 
        // 120, 150, //H
        100, 140,     //Z
        "data/hqq/nnh/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            {"bb",  "data/hqq/nnh/bb.root"},
            {"cc",  "data/hqq/nnh/cc.root"},
            {"gg",  "data/hqq/nnh/gg.root"},
            {"ww",  "data/hqq/nnh/ww.root"},
            {"zz",  "data/hqq/nnh/zz.root"},
            {"tt",  "data/hqq/nnh/tt.root"}
        }
    },
    {   "eeqq_rec", 6, 1,  70,110,
        "data/hqq/3d/ee/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            {"bb",  "data/hqq/3d/ee/bb.root"},
            {"cc",  "data/hqq/3d/ee/cc.root"},
            {"gg",  "data/hqq/3d/ee/gg.root"},
            {"ww",  "data/hqq/3d/ee/ww.root"},
            {"zz",  "data/hqq/3d/ee/zz.root"},
            {"tt",  "data/hqq/3d/ee/tt.root"}
        }
    },
    {   "mmqq_rec", 6, 1,  70,110,
        "data/hqq/3d/mm/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            {"bb",  "data/hqq/3d/mm/bb.root"},
            {"cc",  "data/hqq/3d/mm/cc.root"},
            {"gg",  "data/hqq/3d/mm/gg.root"},
            {"ww",  "data/hqq/3d/mm/ww.root"},
            {"zz",  "data/hqq/3d/mm/zz.root"},
            {"tt",  "data/hqq/3d/mm/tt.root"}
        }
    },   
    {   "qqqq_rec", 6, 1, 
        // 70,125,
        70,125,
        "data/hqq/qqh_cg/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            {"bb",  "data/hqq/qqh_cg/bb.root"},
            {"cc",  "data/hqq/qqh_cg/cc.root"},
            {"gg",  "data/hqq/qqh_cg/gg.root"},
            {"ww",  "data/hqq/qqh_cg/ww.root"},
            {"zz",  "data/hqq/qqh_cg/zz.root"},
            {"tt",  "data/hqq/qqh_cg/tt.root"}
        }
    },
    {   "vvqq_rec", 6, 1,
        // 70,125,
        70,125,
        "data/hqq/nnh/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            {"bb",  "data/hqq/nnh/bb.root"},
            {"cc",  "data/hqq/nnh/cc.root"},
            {"gg",  "data/hqq/nnh/gg.root"},
            {"ww",  "data/hqq/nnh/ww.root"},
            {"zz",  "data/hqq/nnh/zz.root"},
            {"tt",  "data/hqq/nnh/tt.root"}
        }
    },
    {   "eeqq_inv", 6, 1,  
        // 115,140,
        120,140,
        "data/hqq/eeh/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            
            {"bb",  "data/hqq/eeh/bb.root"},
            {"cc",  "data/hqq/eeh/cc.root"},
            {"gg",  "data/hqq/eeh/gg.root"},
            {"ww",  "data/hqq/eeh/ww.root"},
            {"zz",  "data/hqq/eeh/zz.root"},
            {"tt",  "data/hqq/eeh/tt.root"}
        }
    },
    {   "mmqq_inv", 6, 1,  120,140,
        "data/hqq/3d/mm/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            {"bb",  "data/hqq/3d/mm/bb.root"},
            {"cc",  "data/hqq/3d/mm/cc.root"},
            {"gg",  "data/hqq/3d/mm/gg.root"},
            {"ww",  "data/hqq/3d/mm/ww.root"},
            {"zz",  "data/hqq/3d/mm/zz.root"},
            {"tt",  "data/hqq/3d/mm/tt.root"}
        }
    },   
    {   "qqqq_inv", 6, 1, 
        // 70,125,
        100,140,
        "data/hqq/qqh_cg/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            {"bb",  "data/hqq/qqh_cg/bb.root"},
            {"cc",  "data/hqq/qqh_cg/cc.root"},
            {"gg",  "data/hqq/qqh_cg/gg.root"},
            {"ww",  "data/hqq/qqh_cg/ww.root"},
            {"zz",  "data/hqq/qqh_cg/zz.root"},
            {"tt",  "data/hqq/qqh_cg/tt.root"}
        }
    },
    {   "vvqq_inv", 6, 1,
        // 70,125,
        100,140,
        "data/hqq/nnh/sm.root",
        {"bb", "cc", "gg", "ww", "zz", "tt"},
        {
            {"bb",  "data/hqq/nnh/bb.root"},
            {"cc",  "data/hqq/nnh/cc.root"},
            {"gg",  "data/hqq/nnh/gg.root"},
            {"ww",  "data/hqq/nnh/ww.root"},
            {"zz",  "data/hqq/nnh/zz.root"},
            {"tt",  "data/hqq/nnh/tt.root"}
        }
    },
    {   "eett", 7, 1, 120, 140,
        "data/htt/uutt/mmtt_bkg.root",
        {"tt", "bb", "cc", "gg", "ww", "zz", "zh"},
        {
            {"tt",  "data/htt/uutt/mmtt_sig.root"},
            {"bb",  "data/htt/uutt/mmtt_zh.root" },
            {"cc",  "data/htt/uutt/mmtt_zh.root" },
            {"gg",  "data/htt/uutt/mmtt_zh.root" },
            {"ww",  "data/htt/uutt/mmtt_zh.root" },
            {"zz",  "data/htt/uutt/mmtt_zh.root" },
            {"zh",  "data/htt/uutt/mmtt_zh.root" },
        }
    },
    {   "mmtt", 7, 1, 120, 140,
        "data/htt/uutt/mmtt_bkg.root",
        {"tt", "bb", "cc", "gg", "ww", "zz", "zh"},
        {
            {"tt",  "data/htt/uutt/mmtt_sig.root"},
            {"bb",  "data/htt/uutt/mmtt_zh.root" },
            {"cc",  "data/htt/uutt/mmtt_zh.root" },
            {"gg",  "data/htt/uutt/mmtt_zh.root" },
            {"ww",  "data/htt/uutt/mmtt_zh.root" },
            {"zz",  "data/htt/uutt/mmtt_zh.root" },
            {"zh",  "data/htt/uutt/mmtt_zh.root" },
        }
    },
    {   "vvtt", 7, 1, 20, 250,
        "data/htt/nntt/nntt_bkg.root",
        {"tt", "bb", "cc", "gg", "ww", "zz", "zh"},
        {
            {"tt",  "data/htt/nntt/nntt_sig.root"},
            {"bb",  "data/htt/nntt/nntt_zh.root" },
            {"cc",  "data/htt/nntt/nntt_zh.root" },
            {"gg",  "data/htt/nntt/nntt_zh.root" },
            {"ww",  "data/htt/nntt/nntt_zh.root" },
            {"zz",  "data/htt/nntt/nntt_zh.root" },
            {"zh",  "data/htt/nntt/nntt_zh.root" },
        }
    },
    {   "qqtt", 7, 1, 
        102, 170, //inv mass
        "data/htt/qqtt/qqtt_smbkg.root", //original shape
        {"tt", "bb", "cc", "gg", "ww", "zz", "zh"},
        {
            {"tt",  "data/htt/qqtt/qqtt_sig.root"},
            {"bb",  "data/htt/qqtt/qqtt_zh.root" },
            {"cc",  "data/htt/qqtt/qqtt_zh.root" },
            {"gg",  "data/htt/qqtt/qqtt_zh.root" },
            {"ww",  "data/htt/qqtt/qqtt_zh.root" },
            {"zz",  "data/htt/qqtt/qqtt_zh.root" },
            {"zh",  "data/htt/qqtt/qqtt_zh.root" }
        }
    },
    {   "eett_imp", 7, 1,           //impact parameter
        // 120, 140,
        -6, 5,
        "data/htt/uutt/mmtt_bkg.root",
        {"tt", "bb", "cc", "gg", "ww", "zz", "zh"},
        {
            {"tt",   "data/htt/uutt/mmtt_sig.root"},
            {"bb",  "data/htt/uutt/mmtt_zh.root" },
            {"cc",  "data/htt/uutt/mmtt_zh.root" },
            {"gg",  "data/htt/uutt/mmtt_zh.root" },
            {"ww",  "data/htt/uutt/mmtt_zh.root" },
            {"zz",  "data/htt/uutt/mmtt_zh.root" },
            {"zh",  "data/htt/uutt/mmtt_zh.root" },
        }
    },
    {   "mmtt_imp", 7, 1, 
        // 120, 140,
        -6, 5,
        "data/htt/uutt/mmtt_bkg.root",
        {"tt", "bb", "cc", "gg", "ww", "zz", "zh"},
        {
            {"tt",   "data/htt/uutt/mmtt_sig.root"},
            {"bb",  "data/htt/uutt/mmtt_zh.root" },
            {"cc",  "data/htt/uutt/mmtt_zh.root" },
            {"gg",  "data/htt/uutt/mmtt_zh.root" },
            {"ww",  "data/htt/uutt/mmtt_zh.root" },
            {"zz",  "data/htt/uutt/mmtt_zh.root" },
            {"zh",  "data/htt/uutt/mmtt_zh.root" },
        }
    },
    {   "vvtt_imp", 7, 1, 
        // 50, 250,
        -6, 5,
        "data/htt/nntt/nntt_bkg.root",
        {"tt", "bb", "cc", "gg", "ww", "zz", "zh"},
        {
            {"tt",   "data/htt/nntt/nntt_sig.root"},
            {"bb",  "data/htt/nntt/nntt_zh.root" },
            {"cc",  "data/htt/nntt/nntt_zh.root" },
            {"gg",  "data/htt/nntt/nntt_zh.root" },
            {"ww",  "data/htt/nntt/nntt_zh.root" },
            {"zz",  "data/htt/nntt/nntt_zh.root" },
            {"zh",  "data/htt/nntt/nntt_zh.root" },
        }
    },
    {   "qqtt_imp", 7, 1, 
        -6, 4,
        "data/htt/qqtt/qqtt_smbkg.root", //scale ww for smooth shape, a little bit better
        //not scaled one
        // "data/htt/qqtt/qqtt_smbkg.root", //original shape
        {"tt", "bb", "cc", "gg", "ww", "zz", "zh"},
        {
            {"tt",   "data/htt/qqtt/qqtt_sig.root"},
            {"bb",  "data/htt/qqtt/qqtt_zh.root" },
            {"cc",  "data/htt/qqtt/qqtt_zh.root" },
            {"gg",  "data/htt/qqtt/qqtt_zh.root" },
            {"ww",  "data/htt/qqtt/qqtt_zh.root" },
            {"zz",  "data/htt/qqtt/qqtt_zh.root" },
            {"zh",  "data/htt/qqtt/qqtt_zh.root" }
        }
    },
    {   "eemm", 1, 1, 122, 127,
        "data/hmumu/eemm_bkg2.root", //bkg rescale
        {"s"},
        {
            {"s",   "data/hmumu/eemm_sig.root"}
        }
    },
    {   "mmmm", 1, 1, 122, 127,
        "data/hmumu/mmmm_bkg2.root", //rescale
        {"s"},
        {
            {"s",   "data/hmumu/mmmm_sig.root"}
        }
    },
    {   "qqmm", 1, 1, 122, 127,
         "data/hmumu/qqmm_bkg.root",
        {"s","3"},
        {
            {"s", "data/hmumu/qqmm_sig.root"}
            //  {"s",   "data/hmumu/qqmm_624.root"}
            // {"s", "data/hmumu/qqmm_3t_2.root"}
            
        }
    },
    {   "vvmm", 1, 1, 122, 127,
        "data/hmumu/vvmm_bkg2.root",
        {"s"},
        {
            {"s",   "data/hmumu/vvmm_sig.root"}
        }
    },
    {   "mcom", 1, 1, 122, 127,
        "data/hmumu/combined_bkg.root",
        {"s"},
        {
            {"s",   "data/hmumu/combined_sig.root"}
        }
    },
    {   "vweq", 1, 1, 
        // 70, 180,
        80,    180,
        "data/WW/nnlvqq/evqq_bkg.root",
        {"s"},
        {
            {"s",   "data/WW/nnlvqq/evqq_sig.root"},
        }
    },
    {   "vwmq", 1, 1, 
        // 70, 180,
        80,    180,
        "data/WW/nnlvqq/mvqq_bkg.root",
        {"s"},
        {
            {"s",   "data/WW/nnlvqq/mvqq_sig.root"},
        }
    },
    {   "eweq", 2, 1, 120, 150,
        "data/WW/llH/eeevqq_b.root",
        {"s", "zh"},
        {
            {"s",   "data/WW/llH/eeevqq_sig.root"},
            {"zh",  "data/WW/llH/eeevqq_ZH.root"}
        }
    },
    {   "ewmq", 2, 1, 120, 150,
        "data/WW/llH/eeuvqq_b.root",
        {"s", "zh"},
        {
            {"s",   "data/WW/llH/eeuvqq_sig.root"},
            {"zh",  "data/WW/llH/eeuvqq_ZH.root"}
        }
    },
    {   "ewlv", 2, 1, 120, 150,
        "data/WW/llH/eelvlv_b.root",
        {"s", "zh"},
        {
            {"s",   "data/WW/llH/eelvlv_sig.root"},
            {"zh",  "data/WW/llH/eelvlv_zh.root"}
        }
    },
    {   "ewevev", 2, 1, 120, 150,
        "data/WW/llH/eeevev_SZ.root",
        {"s", "zh"},
        {
            {"s",   "data/WW/llH/eeevev_sig.root"},
            {"zh",  "data/WW/llH/eeevev_ZH.root"}
        }
    },
    {   "ewmvev", 2, 1, 120, 150,
        "data/WW/llH/eeuvev_SZ.root",
        {"s", "zh"},
        {
            {"s",   "data/WW/llH/eeuvev_sig.root"},
            {"zh",  "data/WW/llH/eeuvev_ZH.root"}
        }
    },
    {   "ewmvmv", 2, 1, 120, 150,
        "data/WW/llH/eeuvuv_SZ.root",
        {"s", "zh"},
        {
            {"s",   "data/WW/llH/eeuvuv_sig.root"},
            {"zh",  "data/WW/llH/eeuvuv_ZH.root"}
        }
    },
    {   "mweq", 2, 1, 120, 150,
        "data/WW/llH/uuevqq_b.root",
        {"s", "zh"},
        {
            {"s",   "data/WW/llH/uuevqq_sig.root"},
            {"zh",  "data/WW/llH/uuevqq_ZH.root"}
        }
    },
    {   "mwmq", 2, 1, 120, 150,
        "data/WW/llH/uuuvqq_b.root",
        {"s", "zh"},
        {
            {"s",   "data/WW/llH/uuuvqq_sig.root"},
            {"zh",  "data/WW/llH/uuuvqq_ZH.root"}
        }
    },
    {   "mwlv", 2, 1, 120, 150,
        "data/WW/llH/uulvlv_b.root",
        {"s", "zh"},
        {
            {"s",   "data/WW/llH/uulvlv_sig.root"},
            {"zh",  "data/WW/llH/uulvlv_zh.root"}
        }
    },
    {   "mwevev", 2, 0, 120, 150,
        "",
        {"s", "zh"},
        {
            {"s",   "data/WW/llH/uuevev_sig.root"},
            {"zh",  "data/WW/llH/uuevev_ZH.root"}
        }
    },
    {   "mwmvev", 1, 0, 120, 150,
        "",
        {"s"},
        {
            {"s",   "data/WW/llH/uuuvev_sig.root"}
        }
    },
    {   "mwmvmv", 2, 1, 120, 150,
        "data/WW/llH/uuuvuv_ZZ.root",
        {"s", "zh"},
        {
            {"s",   "data/WW/llH/uuuvuv_sig.root"},
            {"zh",  "data/WW/llH/uuuvuv_ZH.root"}
        }
    },
    {   "vzej", 2, 1, 115, 135,
        "data/new_zz/vveejj/sm.root",
        {"s", "zh"},
        {
            {"s",   "data/new_zz/vveejj/sig.root"},
            {"zh",  "data/new_zz/vveejj/ZH_bkg.root"}
        }
    },

    {   "ezej", 1, 1, 120, 140,
        "data/new_zz/eeeejj/bkg.root",
        {"s", "zh"},
        {
            {"s",   "data/new_zz/eeeejj/sig.root"}
        }
    },
    {   "mzej", 1, 1, 120, 140,
        "data/new_zz/eemmjj/bkg.root",
        {"s", "zh"},
        {
            {"s",   "data/new_zz/eemmjj/sig.root"}
        }
    },
    // {   "mzvj", 2, 1, 120, 140,
    //     "data/new_zz/mmvvjj/sm.root",
    //     {"s", "zh"},
    //     {
    //         {"s",   "data/new_zz/mmvvjj/sig.root"},
    //         {"zh",  "data/new_zz/mmvvjj/ZH_bkg.root"}
    //     }
    // },
        {   "mzvj", 5, 1, 120, 140,
        "data/new_zz/mzvj/new_mzvj_sm.root",
        {"s", "zz", "ww", "tt", "zy"},
        {
            {"s",   "data/new_zz/mzvj/new_mzvj_sig.root"},
            {"zz",  "data/new_zz/mzvj/new_mzvj_zz.root"},
            {"ww",  "data/new_zz/mzvj/new_mzvj_ww.root"},
            {"tt",  "data/new_zz/mzvj/new_mzvj_tt.root"},
            {"zy",  "data/new_zz/mzvj/new_mzvj_az.root"}
        }
    },
    
    {   "mzjv", 8, 1, 120, 140,
        "data/new_zz/mzjv/new_mzjv_sm.root",
        {"s", "zz", "ww", "tt", "zy","bb", "cc", "gg"},
        {
            {"s",   "data/new_zz/mzjv/new_mzjv_sig.root"},
            {"zz",  "data/new_zz/mzjv/new_mzjv_zz.root"},
            {"ww",  "data/new_zz/mzjv/new_mzjv_ww.root"},
            {"tt",  "data/new_zz/mzjv/new_mzjv_tt.root"},
            {"zy",  "data/new_zz/mzjv/new_mzjv_az.root"},
            {"bb",  "data/new_zz/mzjv/new_mzjv_bb.root"},
            {"cc",  "data/new_zz/mzjv/new_mzjv_cc.root"},
            {"gg",  "data/new_zz/mzjv/new_mzjv_gg.root"}
        }
    },

    {   "vzjm", 5, 1, 120, 140,
        "data/new_zz/vzjm/new_vzjm_sm.root",
        {"s", "zz", "ww", "tt", "bb"},
        {
            {"s",   "data/new_zz/vzjm/new_vzjm_sig.root"},
            {"zz",  "data/new_zz/vzjm/new_vzjm_zz.root"},
            {"ww",  "data/new_zz/vzjm/new_vzjm_ww.root"},
            {"tt",  "data/new_zz/vzjm/new_vzjm_tt.root"},
            {"bb",  "data/new_zz/vzjm/new_vzjm_bb.root"}
        }
    },

    {   "qzvm", 5, 1, 120, 140,
        "data/new_zz/qzvm/new_qzvm_sm.root",
        {"s", "zz", "ww", "tt", "bb"},
        {   
            {"s",   "data/new_zz/qzvm/new_qzvm_sig.root"},
            {"zz",  "data/new_zz/qzvm/new_qzvm_zz.root"},
            {"ww",  "data/new_zz/qzvm/new_qzvm_ww.root"},
            {"tt",  "data/new_zz/qzvm/new_qzvm_tt.root"},
            {"bb",  "data/new_zz/qzvm/new_qzvm_bb.root"}
        }
    },

    {   "qzmv", 6, 1, 120, 140,
        "data/new_zz/qzmv/new_qzmv_sm.root",
        {"s", "zz", "ww", "tt", "bb", "cc"},
        {
            {"s",   "data/new_zz/qzmv/new_qzmv_sig.root"},
            {"zz",  "data/new_zz/qzmv/new_qzmv_zz.root"},
            {"ww",  "data/new_zz/qzmv/new_qzmv_ww.root"},
            {"tt",  "data/new_zz/qzmv/new_qzmv_tt.root"},
            {"bb",  "data/new_zz/qzmv/new_qzmv_bb.root"},
            {"cc",  "data/new_zz/qzmv/new_qzmv_cc.root"},
        }
    },
    
    {   "vvhbb", 2, 1, 60, 125,
        "data/vvbb/vvbb_sm.root",
        {"s", "zh"},
        {
            {"s",   "data/vvbb/vvbb_sig.root"},
            {"zh",  "data/vvbb/vvbb_zh.root"}
        }
    },
    {   "vvhbb_rec", 2, 1, 60, 125,
        "data/vvbb/vvbb_sm.root",
        {"s", "zh"},
        {
            {"s",   "data/vvbb/vvbb_sig.root"},
            {"zh",  "data/vvbb/vvbb_zh.root"}
        }
    },
    {   "vvhbb_cos", 2, 1, -1, 1,
        "data/vvbb/vvbb_sm.root",
        {"s", "zh"},
        {
            {"s",   "data/vvbb/vvhbb_sig_cos.root"},
            {"zh",  "data/vvbb/vvhbb_zh_cos.root"}
        }
    },
    {   "vvlvlv", 1, 1, 
        // 23.69, 26540,
        // 2130, 1670,     //mmtt
        // 279.41, 594492,
        // 100000, 150000,
        100, 300,
        "data/qqww_fake.root",
        {"s"},
        {
            {"s",   "data/qqww_fake.root"}
        }
    },
    {   "nnlvlv", 1, 1, 
        // -1, 1,
        -0.0222, 0.18,
        "data/WW/nnlvqq/vvlvlv_bkg.root",
        {"s"},
        {
            {"s",   "data/WW/nnlvqq/vvlvlv_sig.root"}
        }
    },
    {   "onebintest", 1, 1, 100, 100,
        "data/qqww_fake.root",
        {"s"},
        {
            {"s",   "data/qqww_fake.root"}
        }
    },
    {   "vvevev", 1, 1, 185.753, 3036.92,
        "data/qqww_fake.root",
        {"s"},
        {
            {"s",   "data/qqww_fake.root"}
        }
    },
    {   "vvevmv", 1, 1, 379.764, 2541.68,
        "data/qqww_fake.root",
        {"s"},
        {
            {"s",   "data/qqww_fake.root"}
        }
    },
    {   "vvmvmv", 1, 1, 205.45, 2157.07,
        "data/qqww_fake.root",
        {"s"},
        {
            {"s",   "data/qqww_fake.root"}
        }
    },
    {   "qz4v", 1, 1, 100, 150,
        "data/hinvi/invi_qq_bkg.root",
        {"s"},
        {
            {"s",   "data/hinvi/invi_qq_sig.root"}
        }
    },
    {   "ez4v", 1, 1, 120, 150,
        "data/hinvi/invi_ee_bkg.root",
        {"s"},
        {
            {"s",   "data/hinvi/invi_ee_sig.root"}
        }
    },
    {   "mz4v", 1, 1, 120, 140,
        // "data/hinvi/invi_mm_bkg.root",
        "data/hinvi/mz4v_bkg.root",
        {"s"},
        {
            // {"s",   "data/hinvi/invi_mm_sig.root"}
             {"s",   "data/hinvi/mz4v_sig.root"}
        }
    },
};
int indexbyname(TString cname)
{
    for (int i=0; i<100; i++)
        if (c[i].name==cname) return i;
    return 0;
}
channel channelbyname(TString cname)
{
    for (int i=0; i<100; i++)
        if (c[i].name==cname) return c[i];
    return c[0];
}
//如果pdf没选好 大概率在拟合信号强度时崩
TString funcsetting(TString cname, TString proc, Int_t index=1)
{
    TString f="";
if (index==1)
{
    if (proc=="b")
    {
        if ( 
            cname.Contains("llyy")        
            || cname.Contains("4v") 
            || cname.Contains("inc_mi") 
            || cname.Contains("inc_md") 
            || cname=="qqtt"
            || cname=="qqqq_rec"   
            )
        f="cheb";  
        if  (  cname.Contains("mz4v_jmq")) f="keys";
        if  (  cname.Contains("vw4q_rec")) f="cheb";
        if  (  cname.Contains("eeqq_rec")
            || cname.Contains("mmqq_rec") 
            || cname.Contains("qqqq")
            || cname.Contains("mz4v")
            || cname.Contains("yy_r")
            || cname=="vvtt"
            || cname.Contains("vvqq"))
        f="keys";

    }
    else
    {           //signal
        if (   cname=="vvtt"  
            // || cname.Contains("inv")   
            || cname=="qqtt"  
            // || cname.Contains("vzmj")  
            || cname.Contains("vzej")  
            || cname.Contains("vw")    
            || cname.Contains("eeqq_rec")    
            || cname.Contains("vvqq")  
            || cname.Contains("qqqq")      
         )
            f="keys";
        if (cname.Contains("vzmj") ) f="Voigtian";
        if (cname.Contains("qz4v") ) f="BifurGuassian";
        // if (cname.Contains("yy") )   f="Voigtian";      //currently yy is Symmetrical.
        if (cname.Contains("yy") )   f="DSCB";      //currently yy is Symmetrical.
    }
        // if (cname.Contains("Voigtian")) f="cheb";
    if (    //both s and b; 
            cname.Contains("vweq") || cname.Contains("vwmq") || cname.Contains("vzej") 
         || cname.Contains("vw4q") || cname.Contains("qw4q") || cname.Contains("imp"))
            f="keys";
    if (cname.Contains("vw4q_rec") && proc=="b") f="cheb";
}
else 
{ // for 2d fit
    // if ()
    if (cname.Contains("tt") ) f= "binned";
    if (cname.Contains("w4q")) f= "keys";
    if (cname.Contains("vw4q") && proc=="b") f="cheb";
    if (cname.Contains("yy") && proc=="s")   f="DSCB";
    if (cname.Contains("yy") && proc=="b")   f="keys";
}
 return f;
}

// Float_t lum=1;
Float_t lum=1; // 5 ab-1 to 5.6 ab-1

Float_t weightsetting(TString cname, TString proc)
{
    Float_t w=1;
    if (proc!="b")
    {
        if (cname.Contains("qz4v"))     w = 0.001083239; // important!
        if (cname.Contains("ez4v"))     w = 0.000376329;
        // if (cname=="mz4v")              w = 0.00037632;
        // if (cname=="mz4v")  w*=0.00106;
        if (cname.Contains("eemm")||cname.Contains("mmmm")||cname.Contains("qqmm")||cname.Contains("vvmm")||cname.Contains("mcom"))        
                                        w = 0.0023;
        if (cname.Contains("einc_zhaoh"))     w = 1/ 41105. ;
        if (cname.Contains("minc_zhaoh"))     w = 1/ 40810. ;
    }
    return w;
}
Float_t weightscale  (TString cname, TString proc)
{
    Float_t w=1;
    if (proc=="b")
    {
        if (cname.Contains("eett")) w*=4.045891;
        // (4075+4072+256892+561237+5278241)/(122674+223691+86568+1075886)
        // w*=1.03;
        if (!is250)
        {
            if      (cname.Contains("vvhbb")) w*=1.052864;
            else if (cname.Contains("qqqq"))  w*=1.04;
            else if (cname.Contains("vvqq"))  w*=1.04;
            else if (cname.Contains("qz4v"))  w*=1.04;
            // else if (cname.Contains("qqyy"))  w*=1.08;
            // else if (cname.Contains("mmyy"))  w*=1.068;
            // else if (cname.Contains("vvyy"))  w*=1.009;
            else if (cname.Contains("qqmm"))  w*=1.06;
            else if (cname.Contains("vvmm"))  w*=1.06;
            else if (cname.Contains("mmmm"))  w*=1.07;
            else if (cname.Contains("qqyy"))  w*=1.08;
            else                              w*=1.03;     
        }
        else
        {
            if (cname.Contains("qqyy"))  w*=1/1.08;
            if (cname.Contains("mmyy"))  w*=1/1.068;
            if (cname.Contains("vvyy"))  w*=1/1.009;
        }
    }
    else
    {
        if (cname.Contains("eett"))    w *= 7.6/7.1;             // eeH: 7.6; mmH: 7.1
        if (cname.Contains("mmtt")||cname.Contains("eett")||cname.Contains("qqtt"))   
        {
            if (proc.Contains("bb"))   w *= 130 / 1915.;
            if (proc.Contains("cc"))   w *= 21  / 1915.;
            if (proc.Contains("gg"))   w *= 10  / 1915.;
            if (proc.Contains("ww"))   w *= 1470/ 1915.;
            if (proc.Contains("zz"))   w *= 209 / 1915.;
            if (proc.Contains("zh"))   w *= 74  / 1915.;
        }
        else if (cname.Contains("vvtt"))   
        {
            if (proc.Contains("bb"))   w = 8  / 675. ;
            if (proc.Contains("cc"))   w = 4  / 675. ;
            if (proc.Contains("gg"))   w = 7  / 675. ;
            if (proc.Contains("ww"))   w = 518/ 675. ;
            if (proc.Contains("zz"))   w = 92 / 675. ;
            if (proc.Contains("zh"))   w = 46 / 675. ;
        }
        if (!is250)
        {
        if (cname.Contains("vvhbb"))
        {
            if ( proc.Contains("s"))  w*=0.971537;
            if ( proc.Contains("zh")) w*=1.013535;
        }
        else 
        {
            // w*=0.96; 
            if ( cname.Contains("ew")  || cname.Contains("ez") || cname.Contains("eett") || cname.Contains("eeqq") || cname.Contains("eemm") || cname.Contains("einc")) w*= 0.928;
            if ( cname.Contains("mw")  || cname.Contains("mz") || cname.Contains("mmtt") || cname.Contains("mmqq") || cname.Contains("mmmm") || cname.Contains("minc")) w*= 0.954;
            if ( cname.Contains("qw")  || cname.Contains("qz") || cname.Contains("qqtt") || cname.Contains("qqqq") || cname.Contains("qqmm") ) w*= 0.954;
            if ( cname.Contains("vw")  || cname.Contains("vz") || cname.Contains("vvtt") || cname.Contains("vvqq") || cname.Contains("vvmm") || cname.Contains("vv")) w*= 0.946;
            // if ( cname.Contains("qqzy") ) w*= 0.950; // (946+950)/2
            if ( cname.Contains("qqzy") ) w*= 0.950;
        }
        }
        else 
        {
            if (cname.Contains("mmyy")) w*= 1/0.954;
            if (cname.Contains("qqyy")) w*= 1/0.954;
            if (cname.Contains("vvyy")) w*= 1/0.946;
        }
    }
    // return w*1.12;
    return w;
}

bool isonebin =false;
bool isbinned =false;
bool isforplot=false;
bool useexisting=false;
bool is2d =false;

bool isbcg=false;
bool istautau=false;
bool isyy=false;
bool isw=false;
bool isz=false;
bool isinvi=false;
bool ismuon=false;

void checkcname(TString cname)
{
    isonebin=false;
    isbinned=false;
    isforplot=false;
    useexisting=false;
    is2d =false;

    isbcg=false;
    istautau=false;
    isyy=false;
    isw =false;
    isz =false;
    isinvi=false;
    ismuon=false;


    if ((cname.Contains("eett") ||cname.Contains("mmtt") ||cname.Contains("vvtt")||cname.Contains("qqtt")) && !(cname.Contains("imp"))) 
        istautau=true;
    if (cname=="eeqq" ||cname=="mmqq" ||cname=="qqqq" ||cname=="vvqq") 
        isbcg=true;
    if (cname.Contains("yy"))
        isyy=true;
    if (cname.Contains("w") || cname.Contains("vvlvlv") || cname.Contains("vvevev") || cname.Contains("vvevmv") || cname.Contains("vvmvmv"))
        isw=true;
    if (cname.Contains("4v"))
        isinvi=true;
    if (!(cname.Contains("4v")) && !(cname.Contains("qqzy")) && cname.Contains("z") ) 
        isz=true;
    if (cname.Contains("qqmm")  || cname.Contains("eemm")||cname.Contains("mmmm")||cname.Contains("vvmm"))
        ismuon=true;
    int test= isbcg + istautau + isyy + isw + isz + isinvi + ismuon;
    if (cname.Contains("qqzy") || cname.Contains("vvhbb") || cname.Contains("mcom") || cname.Contains("inc") ) test+=1;
    if (test!=1 && !cname.Contains("_")) cerr<<"Check channels with error!"<<endl;

    if ( cname.Contains("incl") 
      || cname.Contains("qwlq")
      || cname.Contains("vvlvlv")
      || cname.Contains("vvevev") 
      || cname.Contains("vvevmv") 
      || cname.Contains("vvmvmv")
      || cname.Contains("onebintest")) 
        isonebin=true;
    if (cname.Contains("imp") )    isbinned =true;
    if (cname.Contains("nnlvlv") ) isbinned=true;
    if (cname.Contains("inv") || cname.Contains("rec") || cname.Contains("mcom") || cname.Contains("imp")  || cname.Contains("rll") || cname.Contains("inc") ) isforplot=true;    // Contains("_")
    if (( isyy || istautau || cname=="qw4q"|| cname=="vw4q")&& !(cname.Contains("_"))) is2d=true;
    // isforplot=true;
}

int templatebins=20;  
Float_t onebinrange=50000;

Float_t number[4]={0.1,0.4,1,2};
TString lu_n="5";
TString n[4]={"0.5","2","5","10"}; 

Float_t uncer_cx    = 0.005; // this is uncer of cx.
TString sigma_cx    ="0.005";
Float_t uncer_lumi  = 0.001;
TString sigma_lumi  ="0.001";

int     n_sig, n_bkg;
Float_t m_low, m_high;
Float_t v2_high, v2_low;
TString proc[10];

    RooRealVar mu_bb("mu_bb", "mu_bb", 1, -1, 5);
    RooRealVar mu_cc("mu_cc", "mu_cc", 1, -1, 5);
    RooRealVar mu_gg("mu_gg", "mu_gg", 1, -1, 5);
    RooRealVar mu_zz("mu_zz", "mu_zz", 1, -1, 5);
    RooRealVar mu_yy("mu_yy", "mu_yy", 1, -1, 5);
    RooRealVar mu_ww("mu_ww", "mu_ww", 1, -1, 5);
    RooRealVar mu_tt("mu_tt", "mu_tt", 1, -1, 5);
    RooRealVar mu_mu("mu_mu", "mu_mu", 1, -1, 5);
    RooRealVar mu_in("mu_in", "mu_in", 1, -1, 5);
    RooRealVar mu_zr("mu_zr", "mu_zr", 1, -1, 5);

    RooRealVar zhbb("zhbb", "zhbb", 1, -1, 5);
    RooRealVar vvbb("vvbb", "vvbb", 1, -1, 5);
    RooRealVar vvhbb("vvhbb", "vvhbb", 1, -1, 5);
// //https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHXSWG
// RooFormulaVar width_7k("width_7k","width_7k","1/(0.2137*k_w*k_w+0.02619*k_z*k_z+0.5824*k_b*k_b+0.08187*k_g*k_g+0.002270*k_y*k_y+(0.06272+0.0002176)*k_l*k_l+0.02891*k_c*k_c+0.0017224)",RooArgList(k_b,k_c,k_g,k_z,k_w,k_l,k_y));
// RooFormulaVar width_2k("width_2k","width_2k","1/(0.23989*k_V*k_V+0.76011*k_f*k_f)",RooArgList(k_V,k_f));
   
RooRealVar weight   ("weight", "weight", 1, -1, 10000.);
RooRealVar blikeness("blikeness", "blikeness", 0, 1);
RooRealVar clikeness("clikeness", "clikeness", 0, 1);
RooRealVar costheta("costheta","costheta", -1, 1);
RooRealVar invMass ("invMass", "invMass", 120, 150);
RooRealVar recMass ("recMass", "recMass", 70, 110);
RooRealVar logB("logB", "logB", 0, 2);
RooRealVar logC("logC", "logC", 0, 5);
RooRealVar wt("wt", "wt", 1);

// TString 2dname;
RooDataSet* d_tot;

        TString p0, p1, p2, p3, p4;
        TString tmH    ;
        TString tsigma ;
        TString tTalpha;
        TString tTn    ;
        TString tsigL  ;
        TString tsigR  ;
        TString tratio ;
        TString exps = "exp(@1*(@0-100)/100.0+@2*(@0-100)*(@0-100)/10000.0)";
        Float_t test_mass = 125.;

const map<TString, TString> name=
{
    {"eett",    "Z#rightarrowe^{+}e^{-}, H#rightarrow#tau^{+}#tau^{-}"     },
    {"mmtt",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrow#tau^{+}#tau^{-}"     },
    {"qqtt",    "Z#rightarrowq#bar{q}, H#rightarrow#tau^{+}#tau^{-}"     },
    {"vvtt",    "Z#rightarrow#nu#nu, H#rightarrow#tau^{+}#tau^{-}"     },
    {"eett_imp",    "Z#rightarrowe^{+}e^{-}, H#rightarrow#tau^{+}#tau^{-}"     },
    {"mmtt_imp",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrow#tau^{+}#tau^{-}"     },
    {"qqtt_imp",    "Z#rightarrowq#bar{q}, H#rightarrow#tau^{+}#tau^{-}"     },
    {"vvtt_imp",    "Z#rightarrow#nu#nu, H#rightarrow#tau^{+}#tau^{-}"     },
    {"llyy",    "Z#rightarrowl^{+}l^{-}(#mu,#tau), H#rightarrow#gamma#gamma"       },
    {"vvyy",    "Z#rightarrow#nu#nu, H#rightarrow#gamma#gamma"     },
    {"qqyy",    "Z#rightarrowq#bar{q}, H#rightarrow#gamma#gamma"     },
    {"llyy_rec",    "Z#rightarrowl^{+}l^{-}(#mu,#tau), H#rightarrow#gamma#gamma"       },
    {"mmyy_rec",    "Z#rightarrowl^{+}l^{-}(#mu,#tau), H#rightarrow#gamma#gamma"       },
    {"mmyy_rll",    "Z#rightarrowl^{+}l^{-}(#mu,#tau), H#rightarrow#gamma#gamma"       },
    {"vvyy_rec",    "Z#rightarrow#nu#nu, H#rightarrow#gamma#gamma"     },
    {"qqyy_rec",    "Z#rightarrowq#bar{q}, H#rightarrow#gamma#gamma"     },
    {"eemm",    "Z#rightarrowe^{+}e^{-}, H#rightarrow#mu^{+}#mu^{-}"       },
    {"mmmm",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrow#mu^{+}#mu^{-}"       },
    {"qqmm",    "Z#rightarrowq#bar{q}, H#rightarrow#mu^{+}#mu^{-}"       },
    // {"qqmm_h",    "Z#rightarrowq#bar{q}, H#rightarrow#mu^{+}#mu^{-}, 3T Fast"       },
    // {"qqmm_h2",    "Z#rightarrowq#bar{q}, H#rightarrow#mu^{+}#mu^{-}, 3T Fast"       },
    // {"qqmm_z",    "Z#rightarrowq#bar{q}, H#rightarrow#mu^{+}#mu^{-}, 3T Fast"       },
    // {"qqmm_z2",    "Z#rightarrowq#bar{q}, H#rightarrow#mu^{+}#mu^{-}, 3T Fast"       },
    {"vvmm",    "Z#rightarrow#nu#nu, H#rightarrow#mu^{+}#mu^{-}"       },
    // {"minc",    "Z#rightarrowInclusive, H#rightarrow#mu^{+}#mu^{-}"    },
    {"einc_mi",    "ZX#rightarrowe^{+}e^{-}X"    },
    {"einc_zhaoh",    "ZX#rightarrowe^{+}e^{-}X"    },
    {"minc_zhaoh",    "ZX#rightarrow#mu^{+}#mu^{-}X"    },
    {"minc_mi",    "ZX#rightarrow#mu^{+}#mu^{-}X"    },
    {"einc_md",    "ZX#rightarrowe^{+}e^{-}X"    },
    {"minc_md",    "ZX#rightarrow#mu^{+}#mu^{-}X"    },
    {"mcom",    "Z#rightarrowll,#nu#nu,qq, H#rightarrow#mu^{+}#mu^{-}"     },
    {"ewlv",    "Z#rightarrowe^{+}e^{-}, H#rightarrowWW*#rightarrowl#nul#nu"},
    {"eweq",    "Z#rightarrowe^{+}e^{-}, H#rightarrowWW*#rightarrowe#nuq#bar{q}"},
    {"ewmq",    "Z#rightarrowe^{+}e^{-}, H#rightarrowWW*#rightarrow#mu#nuq#bar{q}"},
    {"mwlv",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowWW*#rightarrowl#nul#nu"},
    {"mweq",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowWW*#rightarrowe#nuq#bar{q}"},
    {"mwmq",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowWW*#rightarrow#mu#nuq#bar{q}"},
    {"vw4q",    "Z#rightarrow#nu#nu, H#rightarrowWW*#rightarrowq#bar{q}q#bar{q}"},
    {"vw4q_rec",    "Z#rightarrow#nu#nu, H#rightarrowWW*#rightarrowq#bar{q}q#bar{q}"},
    {"qw4q",        "Z#rightarrowq#bar{q}, H#rightarrowWW*#rightarrowq#bar{q}q#bar{q}"},
    {"qw4q_rec",    "Z#rightarrowq#bar{q}, H#rightarrowWW*#rightarrowq#bar{q}q#bar{q}"},
    {"vweq",    "Z#rightarrow#nu#nu, H#rightarrowWW*#rightarrowe#nuq#bar{q}"},
    {"vwmq",    "Z#rightarrow#nu#nu, H#rightarrowWW*#rightarrow#mu#nuq#bar{q}"},
    {"vzej",    "Z#rightarrow#nu#nu, H#rightarrowZZ*#rightarrowe^{+}e^{-}q#bar{q}"},
    {"vzmj",    "Z#rightarrow#nu#nu, H#rightarrowZZ*#rightarrow#mu^{+}#mu^{-}q#bar{q}"},
    {"mzvj",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowZZ*#rightarrow#nu#nuq#bar{q}"},
    {"mzjv",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowZZ*#rightarrowq#bar{q}#nu#nu"},
    {"vzjm",    "Z#rightarrow#nu#nu, H#rightarrowZZ*#rightarrowq#bar{q}#mu^{+}#mu^{-}"},
    {"qzvm",    "Z#rightarrowq#bar{q}, H#rightarrowZZ*#rightarrow#nu#nu#mu^{+}#mu^{-}"},
    {"qzmv",    "Z#rightarrowq#bar{q}, H#rightarrowZZ*#rightarrow#mu^{+}#mu^{-}#nu#nu"},
    {"ezej",    "Z#rightarrowe^{+}e^{-}, H#rightarrowZZ*#rightarrowe^{+}e^{-}q#bar{q}"},
    // {"ezmj",    "Z#rightarrowe^{+}e^{-}, H#rightarrowZZ*#rightarrow#mu^{+}#mu^{-}q#bar{q}"},
    {"qz4v",    "Z#rightarrowq#bar{q}, H#rightarrowZZ*#rightarrow#nu#nu#nu#nu"},
    {"ez4v",    "Z#rightarrowe^{+}e^{-}, H#rightarrowZZ*#rightarrow#nu#nu#nu#nu"},
    {"mz4v",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowZZ*#rightarrow#nu#nu#nu#nu"},
    {"mz4v_jmq",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowZZ*#rightarrow#nu#nu#nu#nu"},
    {"eeqq" ,   "Z#rightarrowe^{+}e^{-}, H#rightarrowq#bar{q}"},
    {"mmqq" ,   "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowq#bar{q}"},
    {"qqqq" ,   "Z#rightarrowq#bar{q}, H#rightarrowq#bar{q}"},
    {"vvqq" ,   "Z#rightarrow#nu#nu, H#rightarrowq#bar{q}"},
    {"qqzy" ,   "ZH#rightarrowZZ#gamma#rightarrow#nu#nuq#bar{q}#gamma"},
    {"vvhbb",       "e^{+}e^{-}#rightarrow#nu#nuH, H#rightarrowb#bar{b}"},
    {"vvhbb_rec",   "e^{+}e^{-}#rightarrow#nu#nuH, H#rightarrowb#bar{b}"},
    {"vvhbb_cos",   "e^{+}e^{-}#rightarrow#nu#nuH, H#rightarrowb#bar{b}"},
    // {"eeqq_rec",    "Z mass, Z#rightarrowe^{+}e^{-}, H#rightarrowq#bar{q}"},
    // {"mmqq_rec",    "Z mass, Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowq#bar{q}"},
    // {"qqqq_rec",    "Z mass, Z#rightarrowq#bar{q}, H#rightarrowq#bar{q}"},
    // {"vvqq_rec",    "Z mass, Z#rightarrow#nu#nu, H#rightarrowq#bar{q}"},
    // {"eeqq_inv",    "H mass, Z#rightarrowe^{+}e^{-}, H#rightarrowq#bar{q}"},
    // {"mmqq_inv",    "H mass, Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowq#bar{q}"},
    // {"qqqq_inv",    "H mass, Z#rightarrowq#bar{q}, H#rightarrowq#bar{q}"},
    // {"vvqq_inv",    "H mass, Z#rightarrow#nu#nu, H#rightarrowq#bar{q}"},
    {"eeqq_rec",    "Z#rightarrowe^{+}e^{-}, H#rightarrowq#bar{q}"},
    {"mmqq_rec",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowq#bar{q}"},
    {"qqqq_rec",    "Z#rightarrowq#bar{q}, H#rightarrowq#bar{q}"},
    {"vvqq_rec",    "Z#rightarrow#nu#nu, H#rightarrowq#bar{q}"},
    {"eeqq_inv",    "Z#rightarrowe^{+}e^{-}, H#rightarrowq#bar{q}"},
    {"mmqq_inv",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowq#bar{q}"},
    {"qqqq_inv",    "Z#rightarrowq#bar{q}, H#rightarrowq#bar{q}"},
    {"vvqq_inv",    "Z#rightarrow#nu#nu, H#rightarrowq#bar{q}"},
    {"eeqq",    "Z#rightarrowe^{+}e^{-}, H#rightarrowq#bar{q}"},
    {"mmqq",    "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowq#bar{q}"},
    {"qqqq",    "Z#rightarrowq#bar{q}, H#rightarrowq#bar{q}"},
    {"vvqq",    "Z#rightarrow#nu#nu, H#rightarrowq#bar{q}"},
    {"mzej",     "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowZZ*#rightarrowe^{+}e^{-}q#bar{q}"},
    {"mzmj",     "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrowZZ*#rightarrow#mu^{+}#mu^{-}q#bar{q}"},
    {"mmyy",     "Z#rightarrow#mu^{+}#mu^{-}, H#rightarrow#gamma#gamma"},
    {"nnlvlv",   "Z#rightarrow#nu#nu, H#rightarrowWW*#rightarrowl#nul#nu, BDT value"},
};
const map<TString, TString> xrec=
{
    {"ewlv",        "Recoil"},  {"eett",        "Recoil"},  {"qz4v",        "Recoil"},    {"ezej",        "Recoil"},
    {"mwlv",        "Recoil"},  {"mmtt",        "Recoil"},  {"ez4v",        "Recoil"},    {"mzej",        "Recoil"},
    {"mweq",        "Recoil"},  {"qqtt",        "Recoil"},  {"mz4v",        "Recoil"},    {"mz4v_jmq",        "Recoil"}, 
    {"eweq",        "Recoil"},     
    {"mwmq",        "Recoil"},   
    {"ewmq",        "Recoil"},
    {"vw4q_rec",    "Recoil"},
    // {"qw4q_rec",    "Recoil"},
    {"vv4q_rec",    "Recoil"},
    {"eeqq_inv",    "Recoil"},
    {"mmqq_inv",    "Recoil"},
    {"eeqq",    "Recoil"},
    {"mmqq",    "Recoil"},
    {"mzvj",        "Recoil"},
    {"mzjv",        "Recoil"},
    {"vzjm",        "Recoil"},
    {"qzvm",        "Recoil"},
    {"qzmv",        "Recoil"},
    {"vvhbb_rec",       "Recoil"},
    {"vvhbb",       "Recoil"},
    {"mmyy_ryy",    "Recoil"},
    {"mmyy_rec",    "Recoil"},
    {"mmyy_rll",    "Recoil"},
    {"mmyy_ryy2",   "Reco,shifted"},
    {"mmyy_rll2",   "Reco,shifted"},
    // {"qqyy_rec",    "Reco,shifted"},
    {"qqyy_rec",    "Recoil"},
    {"llyy_rec",    "Recoil"},
    {"vvyy_rec",    "Recoil"},
    {"vvtt",        "Visible"}, 
    {"vweq",        "Visible"}, 
    {"vwmq",        "Visible"},
    // {"qqmm_h",    "Z#rightarrowqq, H#rightarrow#mu#mu, 3T Fast"       },
    {"qqmm_h2",    "Recoil"       },
    // {"qqmm_z",    "Z#rightarrowqq, H#rightarrow#mu#mu, 3T Fast"       },
    {"qqmm_z2",    "Recoil"       },
    {"einc_mi",    "Recoil"    },   {"einc_zhaoh",    "Recoil"    },
    {"minc_mi",    "Recoil"    },   {"minc_zhaoh",    "Recoil"    },
    {"einc_md",    "Recoil"    },
    {"minc_md",    "Recoil"    },
        
};
const map<TString, TString> xname=
{
    {"eett",    "ee"},          
    {"qqtt",    "qq"},          
    {"mmtt",    "#mu#mu"},      
    {"vvtt",    "#tau#tau"},
    {"eemm",    "#mu#mu"},          
    {"mmmm",    "#mu#mu"},              
    {"qqmm",    "#mu#mu"},              
    {"vvmm",    "#mu#mu"},              
    {"llyy",    "#gamma#gamma"},        
    {"vvyy",    "#gamma#gamma"},        
    {"qqyy",    "#gamma#gamma"},
    {"llyy_rec",    "#gamma#gamma"}, 
    {"vvyy_rec",    "#gamma#gamma"},
    {"qqyy_rec",    "#gamma#gamma"},      
    {"ewlv",    "ee"},            
    {"eweq",    "ee"},            
    {"ewmq",    "ee"},            
    {"mwlv",    "#mu#mu"},            
    {"mweq",    "#mu#mu"},            
    {"mwmq",    "#mu#mu"},
    {"vweq",    "e#nuqq"},
    {"vwmq",    "#mu#nuqq"},
    {"vw4q",    "qqqq"},
    {"qw4q",    "H"},
    {"qw4q_rec",    "Z"},
    {"vzej",    "eeq#bar{q}"},
    {"vzmj",    "#mu#muq#bar{q}"},
    {"mzvj",    "#mu#mu"},
    {"mzjv",    "#mu#mu"},
    {"vzjm",    "#nu#nu"},
    {"qzvm",    "q#bar{q}"},
    {"qzmv",    "q#bar{q}"},
    {"ezej",    "ee"},
    // {"ezmj",    "ee"},
    {"qz4v",    "qq"},
    {"ez4v",    "ee"},
    {"mz4v",    "#mu#mu"},
    {"mz4v_jmq",    "#mu#mu"},
    {"eeqq_inv",    "ee"},
    {"mmqq_inv",    "#mu#mu"},
    {"qqqq_inv",    "qq"},
    {"vvqq_inv",    "qq"},
    {"eeqq",    "ee"},
    {"mmqq",    "#mu#mu"},
    {"qqqq",    "qq"},
    {"vvqq",    "qq"},
    {"qqzy",    "Z#gamma-Z"},
    {"vvhbb_rec",   "bb"},
    {"vvhbb",   "bb"},
    {"vw4q_rec","qqqq"},
    {"vw4q_rec","qq"},
    {"eeqq_rec","ee"},
    {"mmqq_rec","#mu#mu"},
    {"qqqq_rec","qq"},
    {"vvqq_rec","qq"},    
    {"mzej",    "#mu#mu"},    
    {"mzmj",    "#mu#mu"},    
    {"mmyy"     ,"#gamma#gamma"},    
    {"mmyy_ryy" ,"#gamma#gamma"},
    {"mmyy_rec" ,"#gamma#gamma"},
    {"mmyy_ryy2","#gamma#gamma"},
    {"mmyy_ll"  ,"#mu#mu"},
    {"mmyy_rll" ,"#mu#mu"},
    {"mmyy_rll2","#mu#mu"},   
    {"qqmm_h",    "#mu#mu"       },
    {"qqmm_h2",    "qq"       },
    {"qqmm_z",    "qq"       },
    {"qqmm_z2",    "#mu#mu"       },
    {"mcom",    "#mu#mu"       },
    {"einc_mi",    "ee"    },
    {"einc_zhaoh",    "ee"    },
    {"minc_mi",    "#mu#mu"    },
    {"minc_zhaoh",    "#mu#mu"    },
    {"einc_md",    "ee"    },
    {"minc_md",    "#mu#mu"    },
};
const map<TString, TString> varname=
{
    {"vw4q_rec",        "Mass_missing"},  
    {"qw4q_rec",        "Mass_Z"},  
    // {"vw4q_rec",        "Mass_missing"},  
    {"qqyy_rec",        "r_yy" },   
    {"vvqq_rec",        "Mass_reco"}, 
    {"eeqq_rec",        "Mass_Z"   }, 
    {"mmqq_rec",        "Mass_Z"   }, 
    {"qqqq_rec",        "Mass_Z"   }, 
    {"mcom_rec",        "Mass_Z"   }, 
    {"mzej_rec",        "Mass_Z"   },
    {"llyy_rec",        "Mass_reco"},
    {"vvyy_rec",        "r_yy"},
    {"mmyy_ll"  ,       "m_ll"     },
    {"mmyy_rll" ,       "r_ll"     },
    {"mmyy_rll2",       "r_ll2"    },
    {"mmyy_ryy" ,       "r_yy"     },
    {"mmyy_rec" ,       "r_yy"     },
    {"mmyy_ryy2",       "r_yy2"    },
    {"eett_imp",        "impact"   },
    {"mmtt_imp",        "impact"   },
    {"qqtt_imp",        "impact"   },
    {"vvtt_imp",        "impact"   },
    {"qqmm_h2",         "m_h2"},
    {"qqmm_z2",         "m_z2"},
    {"qqmm_z",          "Mass_Z"},
    {"minc_mi",            "Mass_H"},
    {"minc_md",            "Mass_H"},
    {"einc_mi",            "Mass_H"},
    {"einc_md",            "Mass_H"},
    {"vvbb_inv",            "Mass_invar"},
    {"vvbb_rec",            "Mass_Z"},
    {"vvcc_inv",            "Mass_invar"},
    {"vvcc_rec",            "Mass_Z"},
    {"vvgg_inv",            "Mass_invar"},
    {"vvgg_rec",            "Mass_Z"},
    {"zzbb_inv",            "Mass_Z"},
    {"zzcc_inv",            "Mass_Z"},
    {"zzgg_inv",            "Mass_Z"},
    {"zzbb_rec",            "Mass_invar"},
    {"zzcc_rec",            "Mass_invar"},
    {"zzgg_rec",            "Mass_invar"},
     {"mzvj",            "Mass_H"},
     {"mzjv",            "Mass_H"},
     {"vzjm",            "Mass_H"},
     {"qzvm",            "Mass_H"},
     {"qzmv",            "Mass_H"},
    
};
const map<TString, Float_t> histomax=
{
    {"llyy",        240   },
    // {"qqyy",        2200  },
    {"qqyy",        1600  },
    {"vvyy",        400   },
    {"vvqq",        14000 },
    {"vvqq_rec",    11000 },
    {"vvtt",        17000 },
    {"qqtt",        10000 },
    {"eeqq",        4000 },
    {"eeqq_rec",        4000 },
    // {"mmqq_inv",        10000 },
    {"mmqq_rec",        10000 },
    {"qqqq_inv",        30000 },
    {"qqqq",        35000 },
    {"qqqq_rec",        50000 },
    {"vvqq_inv",        15000 },
    // {"vvqq_rec",        50000 },
    {"vvhbb_rec",       18000 },
    {"vvhbb_s",         18000 },
    // {"vvtt_imp",    2200  },
    // {"qqtt_imp",    1500   },
    // {"mmtt_imp",    16000 },
    // {"eett_imp",    240   },
    {"vw4q",        8000  },
    {"vw4q_rec",    8000  },
    {"qw4q",        25000  },
    {"qw4q_rec",    25000  },
    {"qqyy_rec",    7000  },
    {"qqzy",        300   },
    // {"mmyy"     ,   100   },
    // {"mmyy_ll"  ,   500   },
    // {"mmyy_rll" ,   150   },
    // {"mmyy_rll2",   150   },
    // {"mmyy_ryy" ,   100   },
    // {"mmyy_ryy2",   100   },
    {"mmyy"     ,   100   },
    {"mcom"     ,   100   },
    {"qqmm"     ,   80   },
    {"vvyy_rec"     ,   1200   },
    {"mmyy_ll"  ,   600   },
    {"mmyy_rll" ,   200   },
    {"mmyy_rll2",   200   },
    {"mmyy_ryy" ,   150   },
    {"mmyy_rec" ,   200   },
    {"mmyy_ryy2",   150   },
    {"vweq" ,   150   },
    {"vwmq",    150   },
    {"vzej",    80   },
    {"qz4v",    40000   },
    {"mz4v",    1200   },
    {"mz4v_jmq",    4000   },
    {"einc_zhaoh"  ,0.03   },
    {"minc_zhaoh"  ,0.07   },
    {"einc_mi"  ,   9000   },
    {"einc_md" ,    6000   },
    {"minc_mi",    14000   },
    {"minc_md" ,   12000   },
};

TString varnamesetting(TString cname)
{
    TString str="Mass_invar";
    if ( varname.count(cname)>0 )  str=varname.at(cname);
    return str;
}
TString namesetting(TString cname)
{
    TString str="";
    if ( name.count(cname)>0 )      str=name.at(cname);
    return str;
}
TString xnamesetting(TString cname)
{
    TString str="";
    if ( xname.count(cname)>0 )  str=xname.at(cname);
    return str;
}
TString xrecsetting(TString cname)
{
    TString str="";
    if ( xrec.count(cname)>0 )  str=xrec.at(cname);
    return str;
}

Float_t PlotMaximum=0;
bool SetPlotMaximum(TString cname )
{
    bool defined=false;
    if ( histomax.count(cname)>0 ) 
    {
        defined     = true;
        PlotMaximum = histomax.at(cname)*1.12;  // 5 to 5.6;
    }
    return defined;
}

RooWorkspace *makespace(TString cname, int index, Float_t lu);
// Float_t tempsetShape(RooWorkspace &ws,   channel c, TString proc);
Float_t zgammaShape (RooWorkspace &ws,   channel c, TString proc);
Float_t onebinShape (RooWorkspace &ws,   channel c, TString proc);
Float_t fusionShape (RooWorkspace &ws,   channel c, TString proc);
Float_t llh3dShape  (RooWorkspace &ws,   channel c, TString proc);
Float_t pdfShape    (RooWorkspace &ws,   channel c, TString proc, TString func);

RooAbsPdf* pdffit(TString cname, RooRealVar &var, RooDataSet &data, TString func);
// void pdffit(RooAbsPdf* pdf, TString func); 难以实现 因为需要factory写死参数
void plotFit    (RooWorkspace *wchannel,channel c, TString proc="s",TString lu_n="5");
void plotImport (RooWorkspace *wspace,  channel c, TString proc,    TString lu_n="5"); 
void FormatAxis(TAxis * axis, double offset);
void FormatLegend(TLegend *legend);
RooFitResult* Minimize(RooAbsPdf *&pdf, RooDataSet &data);

#endif
