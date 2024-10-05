class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Create a dp table with (m+1) x (n+1) dimensions
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the table for the base cases
        for i in range(m + 1):
            dp[i][0] = i  # word1 to empty word2
        for j in range(n + 1):
            dp[0][j] = j  # empty word1 to word2
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No operation needed
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1,      # Deletion
                                dp[i][j - 1] + 1,      # Insertion
                                dp[i - 1][j - 1] + 1)  # Replacement
        
        return dp[m][n]