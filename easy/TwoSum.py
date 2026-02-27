# Question: https://leetcode.com/problems/two-sum/description/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict={}
        for i in range(len(nums)):
            if target-nums[i] in sum_dict:
                return [i, sum_dict.get(target-nums[i])]
            sum_dict.update({nums[i]:i})

# Time complexity: 𝚹(n)
# Space Complexity: 𝚹(n)