import sys

dna = sys.argv[1]


def rna_transcribe():
    with open(dna, 'r+') as f:
        rna = f.read().replace('T', 'U')
        print rna

rna_transcribe()
