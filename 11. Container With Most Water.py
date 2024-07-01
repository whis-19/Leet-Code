class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the height and width
            current_height = min(height[left], height[right])
            current_width = right - left
            
            # Calculate the current area
            current_area = current_height * current_width
            
            # Update max_water if the current area is greater
            max_water = max(max_water, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water