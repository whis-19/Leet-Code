class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        # Initialize the unique element pointer
        i = 1
        
        # Traverse the array with the second pointer
        for j in range(1, len(nums)):
            # If we find a new unique element
            if nums[j] != nums[j - 1]:
                # Place it at the i-th position
                nums[i] = nums[j]
                # Move the unique element pointer
                i += 1
        
        return i
        