class Solution(object):
    def permute(self, nums):
        if not nums:
            return [[]]

        result = [[]]
        
        for num in nums:
            new_result = []
            for perm in result:
                for i in range(len(perm) + 1):
                    new_result.append(perm[:i] + [num] + perm[i:])
            result = new_result
        
        return result