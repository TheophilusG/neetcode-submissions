class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #I am doing it on the 4th of july too cheers neetcode!
        #row check  =o(n)
        #column check = 0(n)
        #sub 3*3 check will require us to go through the entire list


        cols = collections.defaultdict(set) 
        # key= col numbers 
        # value=  is a set of all particular values in the column 

        rows = collections.defaultdict(set)
        # key = row numbers 
        # value is a set of all particular values in the row 


        squares = collections.defaultdict(set)

        # key = (r//3, c//3)
        # value is a set of all particular values in the grid 

        for r in range(9): # 0 to 8 rows
            for c in range(9): # 0 to 8 columns
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or  # if the number exist in the row
                    board[r][c] in cols[c] or  # if the number exist in the column
                    board[r][c] in squares[(r//3, c//3)]): # if it exists in the square

                    return True
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True
                
                    
                    

        