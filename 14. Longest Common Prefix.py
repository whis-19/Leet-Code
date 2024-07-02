class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Find the minimum length string from the array
        min_length = min(len(s) for s in strs)
        
        # Initialize the prefix to the first string's entire length
        prefix = strs[0][:min_length]

        # Compare the prefix with each string in the array
        for s in strs:
            while s[:len(prefix)] != prefix:
                # Reduce the prefix length until it matches the start of s
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix