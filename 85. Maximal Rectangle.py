from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                # Update the heights array
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            
            # Update the maximum area with the largest rectangle in histogram
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Add a sentinel value to the end of heights to simplify the logic
        heights.append(0)
        stack = []
        max_area = 0
        index = 0

        while index < len(heights):
            # Maintain the stack such that the heights are in non-decreasing order
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                # Calculate the area for the height at the top of the stack
                top_of_stack = stack.pop()
                height = heights[top_of_stack]
                width = index if not stack else index - stack[-1] - 1
                max_area = max(max_area, height * width)

        # Remove the sentinel value
        heights.pop()
        return max_area



