class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        stack = [(0, target, [])]

        while stack:
            start, remain, combo = stack.pop()
            
            if remain == 0:
                result.append(combo)
                continue
            
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                stack.append((i, remain - candidates[i], combo + [candidates[i]]))
        
        return result