import sys
import os

def main():

    path = '/cefs/data/DstData/CEPC240/CEPC_v4/higgs/'

    outname = './table/1zh_sample_list.txt'
    
    fout_script = open(outname,'w')
    fout_script.write('%-25s,%-25s,%-25s,%-25s,%-80s,%-25s,%-25s\n'%('# Process','Final state','Cross section [fb]','Events expected','Path','Configuration','Filename tag'))

    for root, dirs, files in os.walk(path):
        for d in dirs:
            if root.split('/')[-1] != 'smart_final_states':
                if len(d.split('.')) > 1:
                    s = d.split('.')[1]
                    dname = s.lstrip('P')
                    final = dname
                    cs = 1
                    exp = 5050 * cs
                    Pat = root + d
                    Config = 'CEPC_V4'
                    tag = '%s.%s.%s'%(dname,'e0','p0')
                    fout_script.write('%-25s,%-25s,%-25s,%-25s,%-80s,%-25s,%-25s\n'%(dname,final,cs,exp,Pat,Config,tag))

    fout_script.close()
    

if __name__ == '__main__':
    main()