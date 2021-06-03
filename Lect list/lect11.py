# работа с командной строкой

import sys
import getopt

# print('Number of argument', len(sys.argv))
# print('Arguments', sys.argv)


def parse(argv):
    inputfile = ''
    outputfile = ''

    # обработка исключений
    try:
        opts, args = getopt.getopt(argv, 'hi:o:', ['ifile=', 'ofile='])
    except getopt.GetoptError:
        print('Usage: lect11.py -i <inputfile> -o <outputfile>\nUsage: lect11.py --ifile <inputfile> --ofile <outputfile>')
        return
        
    for opt, arg in opts:
        if opt == '-h':
            print('Usage lect11.py -i <inputfile> -o <outputfile>')
            return
        elif opt in ['-i', '--ifile']:
            inputfile = arg
        elif opt in ['-o', '--ofile']:
            outputfile = arg
            
    if inputfile == '' or outputfile == '':
        print('Usage: lect11.py -i <inputfile> -o <outputfile>\nUsage: lect11.py --ifile <inputfile> --ofile <outputfile>')
    else:
        print(inputfile, outputfile)


parse(sys.argv[1:])