class Solution(object):
    def numberOfSubmatrices(self, grid):

        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        # Prefix sums for counts of 'X' and 'Y'
        prefix_X = [[0] * (n + 1) for _ in range(m + 1)]
        prefix_Y = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix_X[i+1][j+1] = prefix_X[i+1][j] + prefix_X[i][j+1] - prefix_X[i][j] + (1 if grid[i][j] == 'X' else 0)
                prefix_Y[i+1][j+1] = prefix_Y[i+1][j] + prefix_Y[i][j+1] - prefix_Y[i][j] + (1 if grid[i][j] == 'Y' else 0)

        count = 0

        # Iterate over all submatrices starting from (0, 0) to (i, j)
        for i in range(m):
            for j in range(n):
                total_X = prefix_X[i+1][j+1]
                total_Y = prefix_Y[i+1][j+1]

                # Only consider submatrices with at least one 'X' and equal number of 'X' and 'Y'
                if total_X > 0 and total_X == total_Y:
                    count += 1

        return count


