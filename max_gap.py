import math
num = [20,5,13,9,11,32]
if len(num) < 2:
		print 0
imin = imax = num[0]
for i in num:
	imin = min(imin,i)
	imax = max(imax,i)
gap = int( math.ceil( float(imax - imin)/(len(num)-1) ) )
print gap
# actually needed bucket numbers, reduce useless bucket
bucketNum = int( math.ceil(float(imax - imin)/gap ) )
bucketMin = [2147483647]* bucketNum
bucketMax = [0]* bucketNum

for i in num:
	if i == imin or i == imax:
		continue
	idx = (i - imin)/ gap
	print "index {}".format(idx)
	bucketMin[idx] = min(bucketMin[idx], i)
	bucketMax[idx] = max(bucketMax[idx], i)
maxgap = 0
print bucketMin
print bucketMax
# consider min
previous = imin
for i in range(bucketNum):
	if bucketMin[i] == 2147483647 and bucketMax[i] == 0:
		#empty bucket
		continue
	maxgap = max(maxgap, bucketMin[i] - previous)
	previous = bucketMax[i]
#consider max
maxgap = max(maxgap, imax - previous)
print maxgap