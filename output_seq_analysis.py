from Bio import SeqIO
import sys
import getopt

argv = sys.argv[1:]

score_file_path = None
num = None

try:
    opts, args = getopt.getopt(argv, "hf:n:")  # 短选项模式
    print("Reading file")
    for opt, arg in opts:
        if opt == "-h":
            print('main.py -f <score_file_path> -n <number_of_output_sorted_seqs>')
            sys.exit()
        elif opt in ['-f']:
            score_file_path = arg
            print("Path=%s"%score_file_path)
        elif opt in ['-n']:
            num = arg
            print("Number=%s" % num)

except:
    print('main.py -f <score_file_path> -n <number_of_output_sorted_seqs>')



class proteins:
    def __init__(self, id, seq):
        self.T, self.sample, self.score, self.global_score, self.seq_recovery = id
        self.preference = float(self.score[-6:])*0.6 + float(self.global_score[-6:])*0.6 - float(self.seq_recovery[-6:])*0.2
        self.seq = seq

    def __display__(self):
        print(self.score+"\t"+self.global_score+"\t"+self.seq_recovery)
        print("Preference=%f"%self.preference)
        print(self.seq)

def preprocess(path):
    fd = open(path, "r+")
    content = fd.read()
    fd.close()
    fd = open(path, "w+")
    fd.write(content.replace(' ', ''))
    fd.close()
    fd = open(path, "r+")
    content = fd.readlines()
    fd.close()
    fd = open(path, "w+")
    fd.write(''.join(content[2:]))
    fd.close()

def sort_key(proteins):
    return proteins.preference

preprocess(score_file_path)

protein_candidates = []

for seq_record in SeqIO.parse(score_file_path, "fasta"):
    protein_candidates.append(proteins(seq_record.id.split(','),seq_record.seq))

protein_candidates.sort(key=sort_key, reverse=True)
for i in range(int(num)):
    protein_candidates[i].__display__()

