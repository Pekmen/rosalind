import sys

pairs, offsprings = map(int, sys.argv[1:])

def rabs(n,k):
	if n < 2:
		return n
	else:
		return rabs(n-1,k) + rabs(n-2,k)*k	
    	

print rabs(pairs, offsprings)


#############    Case study   ###################  
#             _ 
#            |0                         n=0   
# rabs(n,k) =|1                         n=1 | n=2
#            |rabs(n-1) + rabs(n-2)*k   n>1             
#
#
# k = 3           k = 2           k = 1
# 1 2 3 4 5       1 2 3 4 5       1 2 3 4 5 
#                
#         1
#         0
#         0
#         0
#         1
#         1
#         1
#         1
#         0               1
#         0               0
#         0               0
#         1               1
#       1 0               1
#       0 0               1
#       0 0             1 0               1
#     1 0 1             0 0               0
#     0 1 0           1 0 1             1 1
#     0 1 0           0 1 0           1 0 1
# 0 1 0 1 0       0 1 0 1 0       0 1 0 1 0  
#
# 1 1 4 7 19      1 1 3 5 11      1 1 2 3 5
#
#
# rabs(0,3)=0     rabs(0,2)=0     rabs(0,1)=0
# rabs(1,3)=1     rabs(1,2)=1     rabs(1,1)=1
# rabs(2,3)=1     rabs(2,2)=1     rabs(2,1)=1
# rabs(3,3)=4     rabs(3,2)=3     rabs(3,1)=2
# rabs(4,3)=7     rabs(4,2)=5     rabs(4,1)=3
# rabs(5,3)=19    rabs(5,2)=11    rabs(5,1)=5

