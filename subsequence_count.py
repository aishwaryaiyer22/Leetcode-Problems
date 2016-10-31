string1 = 'acbcbcbcb'
count2 = 0
count1 = 0
count3 = 0
count = 0
pattern = 'abc'
index = len(string1) -1
while(index >= 0):
	if string1[index] == 'c':
		count2 += 1
		# count1 = 0
		# print "c count at "count2
	elif string1[index] == 'b':
		if count2 > 0:
			count3 += count2
			# print "count is {} at index {}".format(count3, index)
			# count1 += 1 
			# count2 = 0
	elif string1[index] == 'a':
		count += count3
		# print "count is {} at index {}".format(count, index)
			# count3 = 0
		# count1 = 0
		# count2 = 0
	index -= 1	
print count						