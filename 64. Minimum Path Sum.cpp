class Solution
{
public:
    int minPathSum(vector<vector<int>> &grid)
    {
        int m = grid.size();
        int n = grid[0].size();

        // Create a 2D vector to store the minimum path sums
        vector<vector<int>> dp(m, vector<int>(n));

        // Initialize the first cell
        dp[0][0] = grid[0][0];

        // Initialize the first row
        for (int j = 1; j < n; ++j)
        {
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }

        // Initialize the first column
        for (int i = 1; i < m; ++i)
        {
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }

        // Fill in the rest of the dp table
        for (int i = 1; i < m; ++i)
        {
            for (int j = 1; j < n; ++j)
            {
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        // The bottom-right corner contains the minimum path sum
        return dp[m - 1][n - 1];
    }
};