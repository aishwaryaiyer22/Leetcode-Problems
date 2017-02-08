pattern = "ba*a?"
text = "baaabab"

matrix = [[False for x in range(len(text)+1)] for y in range(len(pattern)+1)]
matrix[0][0] = True


def pattern_match(pattern, text):
	if pattern == '' and text == '':
		return True
	if pattern == '' or text == '':
		return False
	print "we're currently matching " + pattern + " and " + text
	if pattern[0] == '?' or (pattern[0] == text[0]):
		return pattern_match(pattern[1:],text[1:])
	elif pattern[0] == '*':
		return pattern_match(pattern[1:],text) or pattern_match(pattern,text[1:])
	return False	
print pattern_match(pattern, text)		