class RotatedSearch {
	public static void main(String args[]) {
		 //find pivot point
		int nums[] = {4, 5, 6, 7, 0, 1, 2, 3};
		int target = 6;
		int n = nums.length -1;
        int lo = 0, hi = n;
        int mid = hi/2;
        int rot, realMid;
        while(lo < hi) {
            if(nums[mid] > nums[hi])
                lo = mid + 1;
            else 
                hi = mid;
            mid = (hi + lo) / 2;
        }


        rot = lo;
        hi = n-1;
       	lo = 0;
        while(lo < hi) {
        	mid =  (hi + lo) / 2;
       		realMid = (mid + rot) % n;
        	if(nums[realMid] == target) {
        		System.out.println(realMid);
        		return;
        	}
        	else if(nums[realMid] < target)
        		lo = mid+1;
        	else
        		hi = mid -1; 
        }
        System.out.println("Not found");
	}
}