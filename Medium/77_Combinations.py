# 77. Combinations - https://leetcode.com/problems/combinations/
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

################################### Examples ###################################

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

################################### Solution ###################################

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        solution, local_sol = [], []

        def backtracking(i):
            if len(local_sol) == k:
                solution.append(local_sol.copy())
                return

            if k - len(local_sol) <= n - i:  # Sol1: i<n:
                local_sol.append(i + 1)
                backtracking(i + 1)
                local_sol.pop()

                backtracking(i + 1)

        backtracking(0)
        return solution


# Sol1: Problem with this solution: I can try to prune the branches that will never work EVER!

################################## Complexity ##################################
# Time complexity: O(2^n)
# Space complexity: O(lgn)