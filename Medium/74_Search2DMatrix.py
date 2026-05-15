# 74. Search a 2D matrix. https://leetcode.com/problems/search-a-2d-matrix/description/

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        rowToConsider = None
        for row in matrix:
            if row[n-1]>=target:
                rowToConsider = row
                break
            rowToConsider = row

        
        low = 0
        high = n-1
        while low<=high:
            mid = low + (high-low)//2
            if rowToConsider[mid] == target:
                return True
            elif rowToConsider[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return False

# The description said that the algorithm should be in order of log. A big hint to use Binary Search. Additionally, the input rows were ordered so Binary Search was possible.

# Time Complexity: O(m+lg(n))
# Space Complexity O(1)
    # rowToConsider = row is pointing to the same memory location therefore it will O(1)



# Option 2:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        low = 0
        high = m-1
        rowIdx = 0
        while low<=high:
            rowIdx = low + (high-low)//2
            if matrix[rowIdx][0]<=target and matrix[rowIdx][n-1]>=target:
                break
            elif matrix[rowIdx][0]>target:
                high = rowIdx - 1
            else:
                low = rowIdx + 1

        
        low = 0
        high = n-1
        while low<=high:
            mid = low + (high-low)//2
            if matrix[rowIdx][mid] == target:
                return True
            elif matrix[rowIdx][mid] < target:
                low = mid+1
            else:
                high = mid-1
        return False

# Time Complexity: O(lgm + lgn)
# Space Complexity: O(1)