"""conditions : +,-,inf?, how to return int, ui1? 5rffcdeesza
"""
if not str:
    return 0
    	
int_max = 2147483647	
sum = 0
start = 0
include_neg = 1
str = str.strip()
if (str[0] == '-'):
	start = 1
	include_neg = -1
	int_max = 2147483648
elif (str[0] == '+'):
    start = 1
print start	
for i in range(start,len(str)):
	if ord(str[i]) >= 48 and ord(str[i]) <= 57:
	    if sum * 10	+ (ord(str[i])-48) > int_max:
	        sum = int_max
	        break
	    sum = sum * 10	+ (ord(str[i])-48)
	else:
	    break
	
sum = include_neg * sum	
return sum