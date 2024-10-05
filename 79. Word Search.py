class Solution:
    def exist(self, board, word):
        if not board:
            return False

        self.rows, self.cols = len(board), len(board[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, i, j, index):
        if index == len(word):
            return True
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or board[i][j] != word[index]:
            return False

        temp = board[i][j]
        board[i][j] = '#'  # mark as visited

        found = (self.dfs(board, word, i + 1, j, index + 1) or
                 self.dfs(board, word, i - 1, j, index + 1) or
                 self.dfs(board, word, i, j + 1, index + 1) or
                 self.dfs(board, word, i, j - 1, index + 1))

        board[i][j] = temp  # unmark
        return found
