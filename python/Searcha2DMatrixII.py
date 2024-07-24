# Runtime: 130ms
# MemoryUsage: 23.8MB

class Solution:
    matrix = None
    target = None
    row_len = None
    col_len = None
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.matrix = matrix
        self.target = target
        self.row_len = len(matrix)
        self.col_len = len(matrix[0])
        def search(row_idx, col_idx):
            if row_idx < 0 or row_idx >= self.row_len:
                return False
            
            if col_idx < 0 or col_idx >= self.col_len:
                return False
            
            value = self.matrix[row_idx][col_idx]
            
            if value == None:
                return False
            else:
                self.matrix[row_idx][col_idx] = None
                
            if value == target:
                return True
            elif value > target:
                return search(row_idx-1, col_idx) or search(row_idx, col_idx-1)
            else:
                return search(row_idx+1, col_idx) or search(row_idx, col_idx+1)
                
        
        return search(0, 0)
