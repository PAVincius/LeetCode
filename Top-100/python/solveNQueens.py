class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(row, cols, diag1, diag2):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if cols & (1 << col) or diag1 & (1 << (row + col)) or diag2 & (1 << (row - col + n)):
                    continue
                
                board[row][col] = 'Q'
                solve(row + 1, cols | (1 << col), diag1 | (1 << (row + col)), diag2 | (1 << (row - col + n)))
                board[row][col] = '.'
        
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        solve(0, 0, 0, 0)
        return res