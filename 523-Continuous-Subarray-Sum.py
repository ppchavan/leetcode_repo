class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        
        # Explanation: https://www.youtube.com/watch?v=OKcrLfR-8mE
        cum_sum = 0
        remainder = {0: -1}

        for i, n in enumerate(nums):
            cum_sum += n
            r = cum_sum % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        
        return False           

# Time complexity: O(N), Since we iterate over whole array only once. Lookup in dictionary is constant time.
# Space complexity: O(N) Since we are iterating over an array and storing values in a dictionary       
        