import sys
import os

def main():

    tabs = sys.argv[3:]
    combine_opt = int(sys.argv[1])
    flag_zz = sys.argv[2]
	
    if (combine_opt==1):
        outname = './table/channel_ll_' + flag_zz + '/tex_bg.txt'
    if (combine_opt==2):
        outname = './table/channel_nn_' + flag_zz + '/tex_bg.txt'    
    if (combine_opt==3):
        outname = './table/channel_qq_' + flag_zz + '/tex_bg.txt'

    fout_script = open(outname,'w')

    for t in tabs:
        fout_script.write('%-25s&%-25s&%-25s%-25s\n'%('Process','Cross section','Events expected',r'\\ \hline'))
        tab = open(t,'r')
        for s_line in tab :
            if not s_line.startswith('#'):
                l = [x.strip() for x in s_line.split(',')]
                dname = l[0].replace('_',r'\_')
                cs = float(l[2])
                event_exp = 5600.0/5050.0 * float(l[3])

                fout_script.write('%-25s&%-25s&%-25s%-25s\n'%(dname,cs,event_exp,r'\\'))

    fout_script.close()
    

if __name__ == '__main__':
    main()
