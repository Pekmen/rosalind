import sys


months, life = map(int, sys.argv[1:])


# recursive method - slow
#
#
#months -= 1
#def rabsd(n, m):
#    if n < 2:
#		 return 1
#	 elif n < m:
#		 return rabsd(n - 2, m) + rabsd(n - 1, m)
#	 else:
#	     return rabsd(n - 2, m) + rabsd(n - 1, m) - rabsd(n - (m + 1), m)
#
#print rabsd(months, life)

def rabs(n, m):
    i = 2
    rabbits = [1,1]
    while i < n:
        if i < m:
        	rabbits.append(rabbits[-2] + rabbits[-1])
        elif i == m or i == m + 1:
        	rabbits.append(rabbits[-2] + rabbits[-1] - 1)
        else:
        	rabbits.append(rabbits[-2] + rabbits[-1] - rabbits[i - (m + 1)])
        i += 1
    print rabbits[-1]

rabs(months, life)
