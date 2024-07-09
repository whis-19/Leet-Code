class Solution(object):
    def canJump(self, nums):
        max_reachable = 0
        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + jump)
            if max_reachable >= len(nums) - 1:
                return True
        return False