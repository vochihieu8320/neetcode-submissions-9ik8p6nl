import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_hash = {}
        box_hash = {}
        for i in range(len(board[0])):
            row_hash = {}

            for j in range(len(board[0])):
                value = board[i][j];
                rowZone = math.ceil((i + 1) / 3)
                colZone = math.ceil((j + 1)/ 3)
        
                if box_hash.get(f"box_#{rowZone}_#{colZone}") is None:
                    box_hash[f"box_#{rowZone}_#{colZone}"] = {}

                # check row and col
                if not value.isdigit(): continue
            
                if col_hash.get(f"col_#{j}") is None:
                    col_hash[f"col_#{j}"] = {}

                if row_hash.get(value) is not None:
                    return False;
                elif col_hash[f"col_#{j}"].get(value) is not None:
                    return False;
                elif box_hash[f"box_#{rowZone}_#{colZone}"].get(value) is not None:
                    return False;
                else:
                    row_hash[value] = True
                    col_hash[f"col_#{j}"][value] = True;
                    box_hash[f"box_#{rowZone}_#{colZone}"][value] = True

                # check the box
        

        return True



        