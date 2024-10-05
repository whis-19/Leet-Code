class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces
        s = s.rstrip()
        
        # Split the string into words
        words = s.split()
        
        # Return the length of the last word
        return len(words[-1]) if words else 0