import sys
import os

def main():

    tabs = sys.argv[1:]
    outname = './table/tex_bg.txt'
    
    fout_script = open(outname,'w')

    for t in tabs:
        fout_script.write('%-25s&%-25s&%-25s%-25s\n'%('Process','Cross section','Events expected',r'\\ \hline'))
        tab = open(t,'r')
        for s_line in tab :
            if not s_line.startswith('#'):
                l = [x.strip() for x in s_line.split(',')]
                dname = l[0].replace('_',r'\_')
                cs = float(l[2])
                event_exp = 1.11 * float(l[3])

                fout_script.write('%-25s&%-25s&%-25s%-25s\n'%(dname,cs,event_exp,r'\\'))

    fout_script.close()
    

if __name__ == '__main__':
    main()