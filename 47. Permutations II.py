class Solution(object):
    def permuteUnique(self, nums):
        if not nums:
            return [[]]

        result = [[]]
        
        for num in nums:
            new_result = []
            for perm in result:
                for i in range(len(perm) + 1):
                    new_perm = perm[:i] + [num] + perm[i:]
                    if new_perm not in new_result:
                        new_result.append(new_perm)
            result = new_result
        
        return result
        