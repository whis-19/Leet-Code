class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        # Get the lengths of the haystack and needle strings
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        # Iterate through the haystack to find the needle
        for i in range(haystack_len - needle_len + 1):
            # Check if the substring of haystack matches the needle
            if haystack[i:i + needle_len] == needle:
                return i
        
        # If the needle is not found in the haystack, return -1
        return -1