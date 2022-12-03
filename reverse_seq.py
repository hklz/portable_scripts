from Bio import SeqIO
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
            print('reverse_seq.py -i <input_file_path> -o <output_file>')
            sys.exit()
        elif opt in ['-i']:
            input_file_path = arg
            print("Inputfile=%s"%input_file_path)
        elif opt in ['-o']:
            output_file_name = arg
            print("Outputfile=%s" % output_file_name)


except TypeError:
    print('reverse_seq.py -i <input_file_path> -o <output_file_name>')



fb_rev_pdb = open(output_file_name+".fasta","w+")
for seq_record in SeqIO.parse(input_file_path, "fasta"):
    fb_rev_pdb.write(">"+seq_record.id+"_revesed\n")
    #print(seq_record.id)
    fb_rev_pdb.write(str(seq_record.seq[::-1]))
    print("Seq:         %s" % seq_record.seq)
    print("revesed_seq: %s" % str(seq_record.seq)[::-1])
fb_rev_pdb.close()
