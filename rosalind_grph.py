data_dict = {}
pairs = []
def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.strip()
        if line.startswith(">"):
            if name: yield(name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

with open('rosalind_test.txt') as fp:
    for name, seq in read_fasta(fp):
        pairs.append((name[1:], seq))

for name1, data1 in pairs:
    for name2, data2 in pairs:
        if data1[-3:] == data2[:3] and name1 != name2:
            print name1, name2
    