s = "abaabdddbaad"

if not s:
	print ""
final_substr = s[0]

#starting with zero treat every string char as possible center of palindromic substring

#odd pivot and even pivot condition
left_pivot = 0
right_pivot = 0
left_element = -1
right_element = 1


while (left_pivot < len(s)):
	#check if there are copies on the right_pivot
	while right_pivot + 1 < len(s) and s[right_pivot+1] == s[left_pivot]:
		right_pivot = right_pivot + 1	
	right_element = right_pivot + 1
	while left_element >= 0 and right_element < len(s) and s[left_element] == s[right_element]:
		left_element = left_element -1
		right_element = right_element + 1
	if (len(s[left_element+1:right_element]) > len(final_substr)):
		final_substr = s[left_element+1:right_element]
	left_pivot = right_pivot + 1
	right_pivot = left_pivot
	left_element = left_pivot -1
print final_substr