def canPlaceBalls(position, m, min_force):
    count = 1  # Place the first ball
    last_position = position[0]
    
    for i in range(1, len(position)):
        if position[i] - last_position >= min_force:
            count += 1
            last_position = position[i]
            if count == m:
                return True
    return False

class Solution(object):
    def maxDistance(self, position, m):
        # Sort the basket positions
        position.sort()

        # Initialize binary search bounds
        left, right = 1, position[-1] - position[0]
        result = 0

        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2
            if canPlaceBalls(position, m, mid):
                result = mid
                left = mid + 1  # Try for a larger minimum distance
            else:
                right = mid - 1  # Try for a smaller minimum distance

        return result
