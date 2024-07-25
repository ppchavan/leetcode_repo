class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        
        # Explanation: https://www.youtube.com/watch?v=OKcrLfR-8mE
        cum_sum = 0
        # This is a map of remainder to index, by computing cumulative sum and storing remainder = sum % k
        # We need to store index i here as value in dictionary because the condition is that subarray length has to be at least 2.
        remainder = {0: -1}

        for i, n in enumerate(nums):
            cum_sum += n
            r = cum_sum % k
            # This is a new entry in the map since key is not found in map
            if r not in remainder:
                remainder[r] = i
            # Key was found, so check if subarray length is greater than 1 (at least 2 elements long)
            elif i - remainder[r] > 1:
                return True
        
        # If solution not found after full iteration, means there is no subarray sum which is multiple of k
        return False           

# Time complexity: O(N), Since we iterate over whole array only once. Lookup in dictionary is constant time.
# Space complexity: O(N) Since we are iterating over an array and storing values in a dictionary       
        