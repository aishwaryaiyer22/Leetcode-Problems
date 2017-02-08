def mergesort(arr,lb,ub):
    m = (lb + ub)/2
    if lb < ub:
        mergesort(arr,lb,m)
        mergesort(arr,m+1,ub)
    tmp = [None] * (ub-lb+1)
    kin = lb
    lin = m+1
    tin = 0
    while kin < m+1 and lin <= ub:
        if arr[kin] <= arr[lin]:
            tmp[tin] = arr[kin]
            tin += 1
            kin += 1
        else:
            tmp[tin] = arr[lin]
            tin += 1
            lin += 1
    while kin < m+1:
        tmp[tin] = arr[kin]
        tin += 1
        kin += 1
    while lin <= ub:
        tmp[tin] = arr[lin]
        tin += 1
        lin += 1 
    tin = 0
    while lb <= ub:
        arr[lb] = tmp[tin]
        lb += 1
        tin +=1   
 
def binary_search(nums,start,target):
    end = len(nums)-1
    first = (start + end) /2
    second = first +1
    i, j = 0,0
    diff = target
    while first < second:
        _sum = nums[first] + nums[second]
        if target-_sum == 0:  # match found
            return first,second
        elif _sum > target:
            if _sum - target < diff:
                diff = _sum - target
                i = first
                j = second
            second = first
            end = first
            first = (start + end) / 2
        else:
            if target-_sum < diff:
                diff = target-_sum
                i = first
                j = second
            start = second
            first = second   
            second = (start + end) / 2
    return i,j

def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
        print 0
    mergesort(nums,0,len(nums)-1)
    print nums
    a,b,c = 0,0,0
    #make sure target is not greater than any sum possible
    max_sum = sum(nums[-3:])
    min_sum = sum(nums[:3])
    if max_sum <= target:
        print max_sum
    elif min_sum >= target:
        print min_sum
    i,j = binary_search(nums,0,29)
    print "i:{} j:{}".format(i,j)    
    # else:        
    #     diff = max_sum-target
    #     for i in xrange(len(nums)-2):
    #             expected_sum = target-nums[i]
    #             start,end = binary_search(nums,i+1,expected_sum)
    #             _sum = nums[i]+nums[start]+nums[end]  
    #             if _sum == target:
    #                 print "match found for {}".format(i)
    #                 a= i
    #                 b = start
    #                 c = end
    #                 break
    #             elif abs(target - _sum) < diff:
    #                 diff = abs(target - _sum)
    #                 a= i
    #                 b = start
    #                 c = end
    # print "{} {} {}".format(a,b,c)
            
    # print closest 
nums = [7,9,4,0,33,55,22,36,87]
target = 26
threeSumClosest(nums,target)  
    