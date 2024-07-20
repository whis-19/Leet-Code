class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Initialize the result matrix with zeros
        n, m = len(rowSum), len(colSum)
        result = [[0] * m for _ in range(n)]
        
        # Initialize row and column pointers
        i, j = 0, 0
        
        while i < n and j < m:
            # Fill the matrix cell with the minimum of current rowSum and colSum
            min_value = min(rowSum[i], colSum[j])
            result[i][j] = min_value
            
            # Update rowSum and colSum
            rowSum[i] -= min_value
            colSum[j] -= min_value
            
            # Move to the next row or column if the current rowSum or colSum is zero
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        
        return result