inf = 0
arr = [3,2,1,1,4,5]
min_dst = 0
for i in xrange(len(arr)-2, -1, -1):
	if arr[i] >min_dst:
		min_dst = 0
	else:
		min_dst += 1	
print min_dst == 0        
