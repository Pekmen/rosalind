def dna_counting(data):
	nuc_bases = ['A', 'C', 'G', 'T']
	with open(data, 'r') as f:
		dna_sample = f.read()
		for symbol in nuc_bases:
			print dna_sample.count(symbol),


dna_counting('rosalind_dna.txt')