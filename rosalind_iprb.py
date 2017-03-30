# I found solution on internet :(
import sys

k, m, n = map(int, sys.argv[1:])
t = k + m + n
print ( k*(k-1) + 2*k*m + 2*k*n + 1*m*n + 0.75*m*(m-1) )/(t*(t-1))