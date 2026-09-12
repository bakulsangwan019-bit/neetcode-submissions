class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            seen = set()
            for val in i:
                if val in seen and val != ".":
                    return False
                if val != ".":
                    seen.add(val)
        
        for j in range(len(board)):
            seen = set()
            for k in range(len(board)):
                if board[k][j] in seen and board[k][j] != ".":
                    return False
                if board[k][j] != ".":
                    seen.add(board[k][j])
            
        for row in range(0,len(board),3):
            for col in range(0,len(board),3):
                seen = set()
                for row_s in range(row,row+3):
                    for col_s in range(col ,col+3):
                        if board[row_s][col_s] in seen and board[row_s][col_s] != ".":
                            return False
                        if board[row_s][col_s] != ".":
                            seen.add(board[row_s][col_s])
        
        return True
