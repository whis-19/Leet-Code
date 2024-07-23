class Solution
{
public:
    int maxProfit(int k, vector<int> &prices)
    {
        if (prices.empty() || k == 0)
        {
            return 0;
        }

        int n = prices.size();

        // If k is larger than n/2, we can treat it as unlimited transactions
        if (k >= n / 2)
        {
            int maxProfit = 0;
            for (int i = 1; i < n; ++i)
            {
                if (prices[i] > prices[i - 1])
                {
                    maxProfit += prices[i] - prices[i - 1];
                }
            }
            return maxProfit;
        }

        // Initialize the dp array
        vector<vector<int>> dp(k + 1, vector<int>(n, 0));

        for (int t = 1; t <= k; ++t)
        {
            int max_prev = -prices[0]; // This will represent the maximum profit we could have before selling
            for (int d = 1; d < n; ++d)
            {
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_prev);
                max_prev = max(max_prev, dp[t - 1][d] - prices[d]); // Update max_prev for the next day
            }
        }

        return dp[k][n - 1];
    }
};
