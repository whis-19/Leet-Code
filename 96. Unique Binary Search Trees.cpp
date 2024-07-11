class Solution
{
public:
    int numTrees(int n)
    {
        // Base case
        if (n == 0 || n == 1)
            return 1;

        // dp[i] will store the number of unique BSTs with i nodes
        vector<int> dp(n + 1, 0);

        // There's one unique BST for a tree with 0 or 1 node
        dp[0] = 1;
        dp[1] = 1;

        // Fill the dp array using the recurrence relation
        for (int nodes = 2; nodes <= n; ++nodes)
        {
            for (int root = 1; root <= nodes; ++root)
            {
                dp[nodes] += dp[root - 1] * dp[nodes - root];
            }
        }

        // The answer is the number of unique BSTs with n nodes
        return dp[n];
    }
};