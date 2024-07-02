class Solution(object):
    def threeSumClosest(self, nums, target):
        # Sort the array to use the two-pointer technique
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            # Initialize two pointers
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is closer to the target, update the closest sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers based on the comparison of current sum and target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If the current sum is exactly equal to the target, return the sum
                    return current_sum
        
        return closest_sum
            