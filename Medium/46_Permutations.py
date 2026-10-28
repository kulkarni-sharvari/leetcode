# 46: Permutations: https://leetcode.com/problems/permutations/description/
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

################################### Examples ###################################

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

################################## Solution 1 ##################################

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        local, sol = [], []

        def backtracking(remaining):
            if not remaining:
                sol.append(local.copy())
                return
            for j in range(len(remaining)):
                local.append(remaining[j])
                backtracking(remaining[:j]+remaining[j+1:])
                local.pop()

        backtracking(nums)
        return sol

################################## Solution 2 ##################################


################################## Complexity ##################################
