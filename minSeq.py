



"""given 12345"""
#brute force- try every pair
n = "1"

def roundedAvg(a,b):
	avg = (a+b)/2.0
	#print str(int(round(avg)))
	return str(int(round(avg)))

if not n:
	print 0
if len(n) == 1:
	print n	
i = 0	
max_number = ""
while i < len(n)-1:
	j = i+1
	new_string = n[0:i]	+ roundedAvg(int(n[i]), int(n[j])) + n[j+1:]
	print new_string
	max_number = max(max_number, new_string)
	i += 1
print max_number	


