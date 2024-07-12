def remove_and_count(s: str, sub: str, points: int) -> (str, int):
    stack = []
    count = 0
    for char in s:
        stack.append(char)
        if len(stack) >= 2 and stack[-2] + stack[-1] == sub:
            stack.pop()
            stack.pop()
            count += points
    return ''.join(stack), count

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        if x >= y:
            # Remove "ab" first, then "ba"
            s, points_ab = remove_and_count(s, "ab", x)
            s, points_ba = remove_and_count(s, "ba", y)
        else:
            # Remove "ba" first, then "ab"
            s, points_ba = remove_and_count(s, "ba", y)
            s, points_ab = remove_and_count(s, "ab", x)

        return points_ab + points_ba

