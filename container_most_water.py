height = [1,1]
if not height:
	print 0
max_so_far = 0
left = 0
right = len(height)-1
while left < right:
	if (min(height[left],height[right]) * (right - left) > max_so_far):
		max_so_far = min(height[left],height[right]) * (right - left)
	if height[left] < height[right]:
		left = left + 1
	else:
		right = right - 1	
print max_so_far