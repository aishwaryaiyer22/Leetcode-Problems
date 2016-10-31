import sys
arr = [2,1,3,1,2,3,4]
# brute-force n * n
# res = [-1] * 7
# for i in xrange(len(arr)):
# 	el = arr[i]
# 	for j in xrange(i):
# 		if arr[j] < el:
# 			res[i] = arr[j]
# 			break
# print res
res = [-1] * 7
m = 4
tmp = [sys.maxint] * m
for i in xrange(len(arr)):
	if tmp[arr[i]-1] == sys.maxint:
		tmp[arr[i]-1] = i 
for i in xrange(1,m):
	tmp[i] = min(tmp[i],tmp[i-1])

for i in xrange(len(arr)):
	if arr[i]-2 >= 0 and tmp[arr[i]-2] < i:
		res[i] = arr[tmp[arr[i]-2]]
	else:
		res[i] = -1	
print res		