class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        return self.isScrambleHelper(s1, s2, memo)
    
    def isScrambleHelper(self, s1: str, s2: str, memo: dict) -> bool:
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        
        if s1 == s2:
            return True
        
        if sorted(s1) != sorted(s2):
            return False
        
        n = len(s1)
        for i in range(1, n):
            if (self.isScrambleHelper(s1[:i], s2[:i], memo) and self.isScrambleHelper(s1[i:], s2[i:], memo)) or \
               (self.isScrambleHelper(s1[:i], s2[-i:], memo) and self.isScrambleHelper(s1[i:], s2[:-i], memo)):
                memo[(s1, s2)] = True
                return True
        
        memo[(s1, s2)] = False
        return False
