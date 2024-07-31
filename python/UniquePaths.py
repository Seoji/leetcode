# Runtime: 35ms
# MemoryUsage: 16.5MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0] * m for _ in range(0, n)]
        
        board[0][0] = 1
        
        for row_idx in range(0, n):
            for col_idx in range(0, m):
                if row_idx > 0:
                    board[row_idx][col_idx] += board[row_idx-1][col_idx]
                if col_idx > 0:
                    board[row_idx][col_idx] += board[row_idx][col_idx-1]
        return board[-1][-1]
