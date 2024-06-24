class Solution(object):
    def minKBitFlips(self, nums, k):
        n = len(nums)
        flip_count = 0
        is_flipped = [0] * n
        flip_effect = 0  # net effect of flips at the current index
        
        for i in range(n):
            if i >= k:
                flip_effect ^= is_flipped[i - k]
            
            # We need to flip if the net effect leads to the current bit being 0
            if nums[i] == flip_effect:
                if i + k > n:
                    return -1  # Not enough elements to form a k-length subarray
                flip_count += 1
                flip_effect ^= 1
                if i < n:
                    is_flipped[i] = 1
        
        return flip_count
