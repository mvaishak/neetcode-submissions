class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_set = {}
        for i in range(3):
            for j in range(3):
                box_set[(i,j)] = set()

        # Row check
        for i in range(9):
            nums = set()
            for j in range(9):
                cur = board[i][j]
                if cur.isnumeric():
                    cur = int(cur)
                    if cur < 1 or cur > 9:
                        return False
                    elif cur in nums:
                        return False
                    else:
                        nums.add(cur)

                    if cur in box_set[(i//3,j//3)]:
                        return False
                    else:
                        box_set[(i//3,j//3)].add(cur)
        box_set = {}
        for i in range(3):
            for j in range(3):
                box_set[(i,j)] = set()
                
        #column check
        for i in range(9):
            nums = set()
            for j in range(9):
                cur = board[j][i]
                if cur.isnumeric():
                    cur = int(cur)
                    if cur < 1 or cur > 9:
                        return False
                    elif cur in nums:
                        return False
                    else:
                        nums.add(cur)

                    if cur in box_set[(j//3,i//3)]:
                        return False
                    else:
                        box_set[(j//3,i//3)].add(cur)
        
        return True

        
