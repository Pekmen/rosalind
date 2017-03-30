import sys

dna = sys.argv[1]


def hamming_distance():
    with open(dna, 'r') as f:
        count = 0
        line1, line2 = f.readlines()
        for i in range(len(line1)):
            if line1[i] != line2[i]:
                count += 1
    return count

print hamming_distance()
