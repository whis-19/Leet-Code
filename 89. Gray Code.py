class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            # Add 1 << i to each element of the current result in reverse order
            result += [x + (1 << i) for x in reversed(result)]
        return result
