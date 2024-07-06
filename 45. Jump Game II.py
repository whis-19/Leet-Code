class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0  # No jump needed if there's only one element
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):  # No need to jump from the last element
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                if current_end >= n - 1:
                    break
        
        return jumps
