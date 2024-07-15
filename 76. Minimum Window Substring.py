class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        t_count = Counter(t)
        window_count = defaultdict(int)
        
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1
            
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            
            while have == need:
                # Update our result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                # Pop from the left of our window
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        
        left, right = res
        return s[left:right + 1] if res_len != float('inf') else ""