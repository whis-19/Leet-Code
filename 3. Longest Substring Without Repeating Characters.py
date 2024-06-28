class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Initialize the dictionary to keep track of characters and their most recent positions
        char_index = {}
        max_length = 0
        left = 0

        # Traverse the string with the right pointer
        for right, char in enumerate(s):
            # If the character is already in the dictionary and its index is within the current window
            if char in char_index and char_index[char] >= left:
                # Move the left pointer to the right of the previous occurrence of the character
                left = char_index[char] + 1

            # Update the character's most recent position
            char_index[char] = right

            # Calculate the length of the current window
            max_length = max(max_length, right - left + 1)

        return max_length
        