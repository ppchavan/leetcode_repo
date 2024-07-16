class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Solution is a slight variation of answer in https://www.youtube.com/watch?v=nIVW4P8b1VA
        if not nums:
            return -1
        
        res = nums[0]
        l, r = 0, len(nums)-1
        
        # We use binary search approach. Iterate through the array, make sure that left and right pointers don't cross. But they can be same element (mid).
        while l <= r:
            mid = (l + r)// 2
            # Keep track of min at each iteration.
            res = min(res, nums[mid])     
            
            # Check if middle element is greater than or equal to right element. If yes, search right.
            # Otherwise search in the left side interval.
            if nums[mid] >= nums[r]:
                # search right interval                
                l = mid + 1
            else:
                # search left interval
                r = mid - 1            
        
        return res
                
# Since we are using binary search approach, the time complexity is O(logN) 