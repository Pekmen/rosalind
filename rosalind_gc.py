import sys

dna = sys.argv[1]


def calc_gc(s):
    g = s.count('G')
    c = s.count('C')
    return ((float(g) + c) / len(s)) * 100


def complementary_dna():
    gc_dict = {}
    with open(dna, 'r') as f:
        dna_id = ''
        dna_seq = ''
        for line in f.readlines():
            if line[0] == '>':
                if dna_seq != '':
                    gc_dict[dna_id] = calc_gc(dna_seq)
                    dna_seq = ''
                dna_id = line.strip()
            else:
                dna_seq += line.strip()
        gc_dict[dna_id] = calc_gc(dna_seq)
    gc_max = max(gc_dict, key=gc_dict.get)
    print gc_max[1:]
    print gc_dict[gc_max]

#print calc_gc('')
complementary_dna()
