class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        # Create a hashmap to count occurrences of each word in words
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        result_indices = []

        # Loop through the string
        for i in range(word_len):
            left = i
            right = i
            current_count = {}
            while right + word_len <= len(s):
                # Get a word from the right end
                word = s[right:right + word_len]
                right += word_len
                if word in word_count:
                    if word in current_count:
                        current_count[word] += 1
                    else:
                        current_count[word] = 1
                    
                    # If there are more occurrences of "word" than needed, move left pointer
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                    
                    # If the window size matches the total length of all words, we found a result
                    if right - left == total_len:
                        result_indices.append(left)
                else:
                    # Reset the window
                    current_count.clear()
                    left = right
        
        return result_indices