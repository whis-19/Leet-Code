class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        # First pass: record the rows and columns that need to be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Second pass: zero out the recorded rows
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        # Third pass: zero out the recorded columns
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0