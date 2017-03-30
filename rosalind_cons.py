import sys

data = sys.argv[1]


def dna_strings(a):
    with open(a, 'r') as f:
        dataset = f.readlines()
    matrix = []
    dna_seq = ''
    for line in dataset:
        if line[0] != '>':
            dna_seq += line.strip()
        elif dna_seq != '':
            matrix.append(dna_seq)
            dna_seq = ''
    matrix.append(dna_seq)
    return matrix


def profile(b):
    matrix = dna_strings(b)
    dnk_len = len(matrix[0])
    p_mtrx = {'A': [], 'C': [], 'G': [], 'T': []}
    for item in p_mtrx:
        for i in range(dnk_len):
            p_mtrx[item].append(0)

    for i in range(dnk_len):
        for dna in matrix:
            p_mtrx[dna[i]][i] += 1
    return p_mtrx, dnk_len


def consensus(d, l):
    cons_str = ''
    for i in range(dnk_len):
        maximum = max([d[key][i] for key in d])    
        for key in d:
            if d[key][i] == maximum:
                cons_str += key
                break
    return cons_str
            
if __name__ == '__main__':
    p_matrix, dnk_len = profile(data)
    cons = consensus(p_matrix, dnk_len)
    print cons
    for char in 'ACGT':
        print '{}: {}'.format(char,' '.join(map(str, p_matrix[char])))   
