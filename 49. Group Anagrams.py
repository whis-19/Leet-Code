class Solution(object):
    def groupAnagrams(self, strs):
        # Dictionary to hold lists of anagrams
        anagrams = defaultdict(list)
        
        # Group words by sorted tuple of characters
        for word in strs:
            sorted_word = tuple(sorted(word))
            anagrams[sorted_word].append(word)
        
        # Convert the dictionary values to a list of lists
        return list(anagrams.values())