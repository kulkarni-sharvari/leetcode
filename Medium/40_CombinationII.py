# 40. combination Sum II - https://leetcode.com/problems/combination-sum-ii/description/

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

################################### Examples ###################################

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

################################### Solution ###################################

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        local, sol = [], []
        n = len(candidates)
        candidates.sort()

        def backtracking(i, curr_sum):
            if curr_sum == target:
                sol.append(local.copy())
                return
            if i >= n or curr_sum > target:
                return
            
            if curr_sum + candidates[i] <= target:
                local.append(candidates[i])
                backtracking(i + 1, curr_sum + candidates[i])
                curr = local.pop()

                while i < n - 1 and candidates[i + 1] == curr:
                    i += 1

                backtracking(i + 1, curr_sum)

        backtracking(0, 0)
        return sol

################################## Complexity ##################################

# Time complexity: O(nlgn + n.2^n) = O(n.2^n)
# Space complexity: 
# - Auxiliary (recursion stack + local) = O(n)
# - Output (sol) = O(2^n)