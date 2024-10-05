class Solution(object):
    def romanToInt(self, s):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # Iterate through each character in the string
        for i in range(n):
            # If the current value is less than the next value, subtract it
            if i < n - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]
            # Otherwise, add the current value to the total
            else:
                total += roman_values[s[i]]
        
        return total


