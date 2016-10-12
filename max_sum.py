s = [1,-1,2,3,4,-10,1,1]
if not s:
	print 0
start = 0
tmp_sum = 0
finalSum = 0
while start < len(s):
	while start < len(s) and tmp_sum + s[start] > 0:
		tmp_sum += s[start]
		if tmp_sum > finalSum:
			finalSum = tmp_sum
		start = start + 1	
	if start < len(s):
		start = start + 1
		tmp_sum = 0	

print finalSum		

