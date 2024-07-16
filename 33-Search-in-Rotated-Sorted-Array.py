class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        i = -1
        l, r = 0, len(nums)-1

        # We do a binary search and look for number at middle index and compare it with target
        while l <= r:
            m = (l + r)//2
            
            # If match is found, return the mid index
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[r]:
                if nums[l] <= target < nums[m]:
                    # If target is between left and mid index, search in left sorted array
                    r = m - 1
                else:
                    # Otherwise search in right sorted array
                    l = m + 1
            else:
                # If target is between mid and right index, search in right sorted array
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    # Otherwise search in left sorted array
                    r = m - 1

        return -1

# Time complexity is O(logN) since we perform binary search
# Explanation: https://www.youtube.com/watch?v=U8XENwh8Oy8
