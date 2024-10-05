class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: Partitioning and marking
        # Sort the array
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] to its correct position nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Step 2: Finding the smallest positive integer that is missing
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1  # If all integers from 1 to n are present, return n + 1
            