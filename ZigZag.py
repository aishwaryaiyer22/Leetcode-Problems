"""ZigZag pattern : n 1 n 1 n 1 ... """


"""s = "PAYPAL"
n = 4
if s is None:
	print s
if n == 1:
	print s
i = 0;	
alpha = 0
count = 0
zig = ""
while alpha < len(s):
	count = i
	if i%2 == 0:
		while(count < len(s)):
			zig = zig + s[count]
			print "at letter"+ s[count]
			count = count + n + 1
			alpha = alpha + 1
	else:
		while count < len(s):
			zig = zig + s[count]
			print "at letter"+ s[count]
			count = count + 2
			alpha = alpha + 1		
	i = i +1 	
print zig"""

numRows = 2
s = "ABC"
# initialize a matrix with numRows * empty strings
matrix = [""]*numRows
# default moving direction, down
inc = 1
# i is the index of row in the matrix
i = 0
for x in range(len(s)):
    # append char in s to corresponding row of matrix
    print i
    matrix[i] += s[x]

    # if out of boundary, change moving direction
    if i+inc >=numRows or i+inc < 0:
        inc = -inc
    i += inc
# append each strings in matrix to the result string     
res = ""
for ma in matrix:
	print ma
	res += ma
print res


