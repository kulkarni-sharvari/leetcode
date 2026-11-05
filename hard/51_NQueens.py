# 51: N-Queens https://leetcode.com/problems/n-queens/description/
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 
################################### Examples ###################################

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:
# Input: n = 1
# Output: [["Q"]]

################################### Solution ###################################

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        sol=[]
        local = [['.' for _ in range(n)] for _ in range(n)]
        col, left_diag, right_diag=set(),set(),set()

        def backtracking(row):
            if row == n:
                sol.append([''.join(row) for row in local])
                return
            
            for c in range(n):
                if c not in col and row-c not in left_diag and row+c not in right_diag:
                    local[row][c] = 'Q'
                    col.add(c)
                    left_diag.add(row-c)
                    right_diag.add(row+c)

                    backtracking(row+1)

                    local[row][c]="."
                    col.remove(c)
                    left_diag.remove(row-c)
                    right_diag.remove(row+c)


        backtracking(0)
        return sol
        