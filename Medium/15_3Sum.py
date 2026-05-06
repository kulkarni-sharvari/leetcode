# 15. 3 Sum: https://leetcode.com/problems/3sum/description/
# 
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums) # Uses Tim's Algorithm - O(nlgn)
        length = len(nums)
        answer = set()
        for i in range(0, length-2): # O(n^2)
            sumDict = {}
            for j in range(i+1, length):
                value = sumDict.get(nums[j], None)
                if value != None:
                    answer.add((nums[i], nums[j], -nums[i]-nums[j]))
                else:
                    sumDict[-nums[i] - nums[j]] = nums[j]
        return list(answer)

# Time complexity: O(nlgn + n^2) = O(n^2)
# Space Complexity: O(n^2)
# sumDict -> O(n)
# answer -> can store upto O(n^2) triplets.
    # For each fixed a, there can be O(n) valid (b, c) pairs.
    # Since there are O(n) choices of a:
    # Total triplets = O(n) * O(n) = O(n²)