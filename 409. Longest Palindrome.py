from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        # Count the frequency of each character in the string
        char_count = Counter(s)
        
        # Initialize variables to track the length of the palindrome
        length = 0
        odd_found = False
        
        # Iterate through the counts of each character
        for count in char_count.values():
            if count % 2 == 0:
                # If the count is even, it can fully contribute to the palindrome
                length += count
            else:
                # If the count is odd, one less than the count can contribute
                # and mark that we have found an odd count
                length += count - 1
                odd_found = True
        
        # If an odd count was found, we can add one extra character in the center
        if odd_found:
            length += 1
        
        return length

