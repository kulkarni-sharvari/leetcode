# Question: https://leetcode.com/problems/product-of-array-except-self/description/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        result = []
        if zeros >= 2:
            return [0] * len(nums)

        prodNonZero = 1
        allProd = 1

        for num in nums:
            if num != 0:
                prodNonZero *= num
            allProd *= num

        for num in nums:
            if num == 0:
                result.append(prodNonZero)
            else:
                result.append(allProd // num)
        return result

# Time complexity: 𝚹(n)
# Space Complexity: 𝚹(1); we only have 3 new variables - zeros, prodNonZero and allProd. These don't depend on the input size.