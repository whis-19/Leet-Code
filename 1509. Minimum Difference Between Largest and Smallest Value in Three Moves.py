class Solution(object):
    def minDifference(self, nums):
        # Edge case: if there are 4 or fewer elements, we can make all elements the same
        if len(nums) <= 4:
            return 0
        
        # Sort the array
        nums.sort()
        
        # Initialize a large difference
        min_diff = float('inf')
        
        # Consider changing the largest three elements
        min_diff = min(min_diff, nums[-4] - nums[0])
        
        # Consider changing the smallest three elements
        min_diff = min(min_diff, nums[-1] - nums[3])
        
        # Consider changing two smallest and one largest element
        min_diff = min(min_diff, nums[-2] - nums[2])
        
        # Consider changing one smallest and two largest elements
        min_diff = min(min_diff, nums[-3] - nums[1])
        
        return min_diff