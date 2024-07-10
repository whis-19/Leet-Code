def backtrack(row, cols, hills, dales, n):
    if row == n:
        return 1
    solutions = 0
    for col in range(n):
        if col in cols or (row - col) in hills or (row + col) in dales:
            continue
        cols.add(col)
        hills.add(row - col)
        dales.add(row + col)
        solutions += backtrack(row + 1, cols, hills, dales, n)
        cols.remove(col)
        hills.remove(row - col)
        dales.remove(row + col)
    return solutions


class Solution(object):
    def totalNQueens(self, n):
        return backtrack(0, set(), set(), set(), n)
