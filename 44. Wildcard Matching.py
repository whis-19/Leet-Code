class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if the first i characters in s match the first j characters in p
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string and empty pattern match
        dp[0][0] = True
        
        # Handle patterns with *
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]