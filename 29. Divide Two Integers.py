class Solution(object):
    def divide(self, dividend, divisor):
        # Constants for the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Special case where overflow might happen
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the quotient
        negative = (dividend < 0) != (divisor < 0)

        # Take the absolute values of dividend and divisor
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Perform the division using bit manipulation
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # Apply the sign of the quotient
        quotient = -quotient if negative else quotient

        # Ensure the result is within the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))