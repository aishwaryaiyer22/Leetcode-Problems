s = "Hello World"
if not s:
	print 0

words = s.split()
if len(words) > 0:
    print len(words[-1])
else:
    print 0
	