nums = [3,4,1,2]
if not nums:
	print 0
if len(nums) <= 2:
	if len(nums) == 1:
		return nums[0]
	elif len(nums) == 2:
		return max(nums[0],nums[1])
curr_max = 0		
while True:
    for j in range(len(nums)-1-i):
        if nums[j] > nums[j+1]:
            nums[j] += nums[j+1]
            nums[j+1] = nums[j] - nums[j+1]
            nums[j] = nums[j] - nums[j+1]
        if nums[len(nums)-1-i] > curr_max:
        	if curr_max  
            
    print nums 
i = 0
while 

def swap(i,j):
	nums[i] += nums[j]
	nums[j] = nums[i]-nums[j]
	nums[i] = nums[i]-nums[j]