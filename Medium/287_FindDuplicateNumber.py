# 287 - Find Duplicate number: https://leetcode.com/problems/find-the-duplicate-number/description/


# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:
# Input: nums = [3,3,3,3,3]
# Output: 3


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sortedList = sorted(nums)

        for i in range(len(sortedList) - 1):
            if sortedList[i] == sortedList[i+1]:
                return sortedList[i]


# Time complexity: O(nlgn + n) = O(nlgn)
# Space complexity: O(n)