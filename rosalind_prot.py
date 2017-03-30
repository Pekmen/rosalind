import sys

script, rna = sys.argv
rna_codon = { 
'UUU': 'F',     'CUU': 'L',    'AUU': 'I',    'GUU': 'V',
'UUC': 'F',     'CUC': 'L',    'AUC': 'I',    'GUC': 'V',
'UUA': 'L',     'CUA': 'L',    'AUA': 'I',    'GUA': 'V',
'UUG': 'L',     'CUG': 'L',    'AUG': 'M',    'GUG': 'V',
'UCU': 'S',     'CCU': 'P',    'ACU': 'T',    'GCU': 'A',
'UCC': 'S',     'CCC': 'P',    'ACC': 'T',    'GCC': 'A',
'UCA': 'S',     'CCA': 'P',    'ACA': 'T',    'GCA': 'A',
'UCG': 'S',     'CCG': 'P',    'ACG': 'T',    'GCG': 'A',
'UAU': 'Y',     'CAU': 'H',    'AAU': 'N',    'GAU': 'D',
'UAC': 'Y',     'CAC': 'H',    'AAC': 'N',    'GAC': 'D',
'UAA': 'Stop',  'CAA': 'Q',    'AAA': 'K',    'GAA': 'E',
'UAG': 'Stop',  'CAG': 'Q',    'AAG': 'K',    'GAG': 'E',
'UGU': 'C',     'CGU': 'R',    'AGU': 'S',    'GGU': 'G',
'UGC': 'C',     'CGC': 'R',    'AGC': 'S',    'GGC': 'G',
'UGA': 'Stop',  'CGA': 'R',    'AGA': 'R',    'GGA': 'G',
'UGG': 'W',     'CGG': 'R',    'AGG': 'R',    'GGG': 'G' }

def protein_string(rna_data):
    with open(rna, 'r') as f:
        str_rna = f.read()
        a = len(str_rna)
        result = ''
        for i in range(0,a,3):
        	if str_rna[i : i+3] in rna_codon:
        		if rna_codon[str_rna[i : i+3]] == 'Stop':
        			return result
        		else:
        			result += rna_codon[str_rna[i : i+3]]
        return result
        
print protein_string(rna)