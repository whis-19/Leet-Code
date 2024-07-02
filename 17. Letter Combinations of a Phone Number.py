class Solution(object):
    def backtrack(self, digits, index, digit_to_letters, current_combination, result):
        if index == len(digits):
            result.append("".join(current_combination))
            return

        digit = digits[index]
        letters = digit_to_letters[digit]
        for letter in letters:
            current_combination.append(letter)
            self.backtrack(digits, index + 1, digit_to_letters, current_combination, result)
            current_combination.pop()  # backtrack

    def letterCombinations(self, digits):
        if not digits:
            return []

        digit_to_letters = {
            '2': "abc", '3': "def", '4': "ghi",
            '5': "jkl", '6': "mno", '7': "pqrs",
            '8': "tuv", '9': "wxyz"
        }

        result = []
        current_combination = []
        self.backtrack(digits, 0, digit_to_letters, current_combination, result)
        
        return result


