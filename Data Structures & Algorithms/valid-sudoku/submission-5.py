class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Keep track of which row,column each number appears in, check if there is a duplication in rows or column numbers or same box. For same box, we can restructure boxes to be box row and col numbers but doing //3? 

        box_set = {}
        for i in range(3):
            for j in range(3):
                box_set[(i,j)] = set()
    
        #Row check
        for row in range(9):
            row_check = set()
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in row_check:
                    return False
                else:
                    row_check.add(val)
                if val in box_set[(row//3,col//3)]:
                    return False
                else:
                    box_set[(row//3,col//3)].add(val)
        #Col check
        for col in range(9):
            col_check = set()
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in col_check:
                    return False
                else:
                    col_check.add(val)
            
        return True
        

            
