import sys
import os

def main():

    inname = './table/zh.txt'
    outname = './table/bg_zh.txt'
    
    fin_script = open(inname,'r')
    fout_script = open(outname,'w')
    fout_script.write('%-25s,%-25s,%-25s,%-25s,%-80s,%-25s,%-25s\n'%('# Process','Final state','Cross section','Events expected','Path','Configuration','Filename tag'))

    for s_line in fin_script :
        l = [x.strip() for x in s_line.split()]

        dname = l[0]
        cs = float(l[1])
        exp = 5050 * cs
        path = '/cefs/data/DstData/CEPC240/CEPC_v4/higgs/E240.P%s.e0.p0.whizard195'%dname
        conf = 'CEPC_V4'
        tag = '%s.%s.%s'%(dname,'e0','p0')

        if dname.split('_')[1] == 'X' :
            fout_script.write('#%-25s,%-25s,%-25s,%-25s,%-80s,%-25s,%-25s\n'%(dname,dname,cs,exp,path,conf,tag))
            continue
        
        fout_script.write('%-25s,%-25s,%-25s,%-25s,%-80s,%-25s,%-25s\n'%(dname,dname,cs,exp,path,conf,tag))

    fin_script.close()
    fout_script.close()
    

if __name__ == '__main__':
    main()