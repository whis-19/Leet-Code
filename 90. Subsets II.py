class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the numbers to handle duplicates
        res = [[]]
        
        start_idx, end_idx = 0, 0
        for i in range(len(nums)):
            start_idx = 0
            
            # If current and the previous elements are the same, new subsets are only from the subsets added in the previous step
            if i > 0 and nums[i] == nums[i - 1]:
                start_idx = end_idx + 1
            
            end_idx = len(res) - 1
            for j in range(start_idx, len(res)):
                res.append(res[j] + [nums[i]])
        
        return res

