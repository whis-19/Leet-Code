class Solution(object):
    def is_valid_block(self, block):
        block = [num for num in block if num != '.']
        return len(block) == len(set(block))
    
    def isValidSudoku(self, board):
        # Check rows
        for row in board:
            if not self.is_valid_block(row):
                return False

        # Check columns
        for col in zip(*board):
            if not self.is_valid_block(col):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid_block(block):
                    return False

        return True

