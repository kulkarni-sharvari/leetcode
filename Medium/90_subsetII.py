# 90: Subset II https://leetcode.com/problems/subsets-ii/description/

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

################################### Examples ###################################
 
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

################################### Solution ###################################

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        local = []
        sol = []
        n = len(nums)
        nums.sort() #O(nlg(n))

        def backtracking(i): #O(n.2^n)
            if i >= n:
                # if local not in sol:
                sol.append(local.copy())
                return

            local.append(nums[i])
            backtracking(i+1)
            curr = local.pop()

            while i < n-1 and nums[i+1] == curr:
                i+=1

            backtracking(i+1)

        backtracking(0)
        return (sol)


################################## Complexity ##################################

# Time complexity: O(n.2^n+nlgn) = O(n.2^n)
# Space complexity: O(n+lgn)