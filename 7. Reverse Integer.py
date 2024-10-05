class Solution {
public:
    int reverse(int x) {


        int result = 0;

        while (x != 0) {
            int digit = x % 10; // Extract the last digit
            x /= 10; // Remove the last digit from x

            // Check for overflow before updating result
            if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > INT_MAX % 10)) {
                return 0; // Overflow would occur
            }
            if (result < INT_MIN / 10 || (result == INT_MIN / 10 && digit < INT_MIN % 10)) {
                return 0; // Underflow would occur
            }

            // Append the digit to the result
            result = result * 10 + digit;
        }

        return result;
    }
};
