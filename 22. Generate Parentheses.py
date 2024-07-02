class Solution(object):
    def backtrack(self, current, open_count, close_count):
        if len(current) == 2 * self.n:
            self.result.append(current)
            return
        
        if open_count < self.n:
            self.backtrack(current + '(', open_count + 1, close_count)
        
        if close_count < open_count:
            self.backtrack(current + ')', open_count, close_count + 1)
    
    def generateParenthesis(self, n):
        self.n = n
        self.result = []
        self.backtrack('', 0, 0)
        return self.result
