class Solution(object):
    def longestSubarray(self, nums, limit):
        minDeque = []
        maxDeque = []
        left = 0
        maxLength = 0
        
        for right in range(len(nums)):
            while minDeque and nums[minDeque[-1]] > nums[right]:
                minDeque.pop()
            while maxDeque and nums[maxDeque[-1]] < nums[right]:
                maxDeque.pop()
                
            minDeque.append(right)
            maxDeque.append(right)
            
            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                left += 1
                if minDeque[0] < left:
                    minDeque.pop(0)
                if maxDeque[0] < left:
                    maxDeque.pop(0)
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
