class Solution(object):
    def solveNQueens(self, n):

        result = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        diags1 = set()
        diags2 = set()
        
        # Stack for the backtracking process
        stack = [(0, board, cols, diags1, diags2)]
        
        while stack:
            row, board, cols, diags1, diags2 = stack.pop()
            
            if row == n:
                result.append(["".join(r) for r in board])
                continue
            
            for col in range(n):
                diag1 = row - col
                diag2 = row + col
                if col in cols or diag1 in diags1 or diag2 in diags2:
                    continue
                
                # Place the queen
                new_board = [r[:] for r in board]
                new_board[row][col] = 'Q'
                new_cols = cols.copy()
                new_diags1 = diags1.copy()
                new_diags2 = diags2.copy()
                new_cols.add(col)
                new_diags1.add(diag1)
                new_diags2.add(diag2)
                
                # Push the next state onto the stack
                stack.append((row + 1, new_board, new_cols, new_diags1, new_diags2))
        
        return result


