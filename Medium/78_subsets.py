# 78. Subsets - https://leetcode.com/problems/subsets/description/
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

################################### Examples ###################################
 

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

################################### Solution ###################################

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res, local_res = [], []
        n = len(nums)

        def dfs(i):
            if i == n:
                res.append(local_res[:]) # if we pass local_res instead it will be a reference to local_res. at the end local_res = [] so the end result will be [] for all subsets. thats why we append a copy of local_res
                return

            # pick the nums[i]
            local_res.append(nums[i])
            dfs(i + 1)
            local_res.pop()

            # don't pick the nums[i]
            dfs(i + 1)

        dfs(0)
        return res


################################## Complexity ##################################

# Time complexity: O(2^n)
# Space complexity: O(lgn)