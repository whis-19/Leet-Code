class Solution
{
public:
    int uniquePaths(int m, int n)
    {
        // Create a 2D vector initialized to 1
        vector<vector<int>> dp(m, vector<int>(n, 1));

        // Iterate over the grid starting from (1,1)
        for (int i = 1; i < m; ++i)
        {
            for (int j = 1; j < n; ++j)
            {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        // The bottom-right corner will have the number of unique paths
        return dp[m - 1][n - 1];
    }
};