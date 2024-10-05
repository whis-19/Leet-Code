class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()          # To track sequences we've seen
        repeated = set()      # To track sequences that are repeated

        # Iterate through the string, stopping at the last 10-letter substring
        for i in range(len(s) - 9):
            seq = s[i:i + 10]  # Extract the 10-letter substring
            if seq in seen:
                repeated.add(seq)  # If it's seen before, add to repeated
            else:
                seen.add(seq)      # Otherwise, add it to seen

        return list(repeated)    # Return the list of repeated sequences