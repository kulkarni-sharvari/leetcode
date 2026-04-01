# https://leetcode.com/problems/valid-sudoku/description/
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        # validity rows
        for row in range(9): #𝚹(1)
            seen = set()
            for ele in range(9):
                if board[row][ele]!= '.':
                    if board[row][ele] in seen:
                        return False
                    else:
                        seen.add(board[row][ele])

        
        # validity columns
        for col in range(9): #𝚹(1)
            seen = set()
            for row in range(9):
                if board[row][col]!= '.':
                    if board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
    
        #validity 3*3 matrix
        for x in range(0,9,3): #𝚹(1)
            for y in range(0,9,3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        if board[row+x][col+y] != '.':
                            if board[row+x][col+y] in seen:
                                return False
                            else:
                                seen.add(board[row+x][col+y])

        return True

# Time complexity = #𝚹(1)
# Since the Sudoku board size is fixed (9×9), the algorithm always performs a constant number of operations (checking rows, columns, and 3×3 boxes). Therefore, the time complexity is Θ(1).

# Space complexity: O(1)
# The auxiliary space is also constant because the seen set never stores more than 9 elements at a time. Hence, space complexity is O(1).

# If generalized to an N×N board, the time complexity becomes O(N²) and space complexity becomes O(N).