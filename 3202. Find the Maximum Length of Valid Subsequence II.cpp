class Solution
{
public:
    int maximumLength(vector<int> &nums, int k)
    {
        int n = nums.size();
        if (k == 1 || n == 2)
            return n;
        vector<vector<int>> dp(n, vector<int>(k, 0));
        int maxLen = 0;
        for (int i = 1; i < n; i++)
        {
            for (int j = i - 1; j >= 0; j--)
            {
                int val = (nums[i] + nums[j]) % k;
                dp[i][val] = max(dp[i][val], dp[j][val] + 1);
                maxLen = max(maxLen, dp[i][val]);
            }
        }
        return maxLen + 1;
    }
};
