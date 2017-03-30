def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name:
        yield (name, ''.join(seq))

def substrings(string):
    length = len(string)
    for s in xrange(length - 1):
        for f in xrange(s + 1, length + 1):
            yield(string[s:f])

with open('rosalind_test.txt') as fp:
    dataset = [s for n, s in read_fasta(fp)]
test = dataset[0]
max_sub = ''


for sub in substrings(test):
    if all( sub in seq for seq in dataset) and len(sub) >= len(max_sub):
        max_sub = sub
print max_sub