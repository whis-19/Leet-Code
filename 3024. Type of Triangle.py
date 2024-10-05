class Solution(object):
    def triangleType(self, nums):
        nums.sort()

        if nums[2] >= nums[0] + nums[1]:
            return "none"

        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        else:
            return "scalene"

