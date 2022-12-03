import re
import sys
import getopt

argv = sys.argv[1:]

input_file_path = None
output_file_name = None

try:
    opts, args = getopt.getopt(argv, "hi:o:")  # 短选项模式
    print("Reading file")
    for opt, arg in opts:
        if opt == "-h":
            print('reverse_pdb.py -i <input_file_path> -o <output_file_name>')
            sys.exit()
        elif opt in ['-i']:
            input_file_path = arg
            print("Inputfile=%s"%input_file_path)
        elif opt in ['-o']:
            output_file_name = arg
            print("Outputfile=%s" % output_file_name)

except:
    print('reverse_pdb.py -i <input_file_path> -o <output_file_name>')


def revese_coord(strings):
    coordinate = float(strings.replace(' ', ''))*(-1)
    coordinate_string = str(coordinate).rjust(len(strings))
    return coordinate_string


#file_path = "lacI_tru_mono.pdb"
protein = open(input_file_path,"r+")
#pdb_analysis = re.match("ATOM   1913  CA  LEU B  62      12.989   6.097   2.391  1.00 34.55           C")
pattern_pdb = r"ATOM...........................(.......).(.......).(.......).*? "
content = protein.readlines()
protein.close()
fb_rev_pdb = open(output_file_name,"w+")
for line in content:
    #print(line,end='')
    try:
        temp = re.match(pattern_pdb,line)
        fb_rev_pdb.write(line[:31] + temp.group(1) + ' ' + revese_coord(temp.group(2)) + ' ' + temp.group(3) + line[54:])
    except AttributeError:
        fb_rev_pdb.write(line)
fb_rev_pdb.close()

    #print(temp.group(1))
    #print(temp.group(2))
    #print(temp.group(3))
