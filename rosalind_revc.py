import sys

dna = sys.argv[1]
complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def complementary_dna():
    with open(dna, 'r') as f:
        dna_rev = list(f.read()[::-1])[1:]
        for n, sym in enumerate(dna_rev):
        	dna_rev[n] = complements[sym]
        print ''.join(dna_rev)

complementary_dna()
