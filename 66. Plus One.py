class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the last digit and move towards the first digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Set the current digit to 0 and continue to the next digit
            digits[i] = 0
        
        # If we have gone through all digits and all were 9,
        # we need an extra digit at the beginning
        return [1] + [0] * n