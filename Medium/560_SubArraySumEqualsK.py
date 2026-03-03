# Question: https://leetcode.com/problems/subarray-sum-equals-k/description/
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = 0
        count = 0
        prefix_freq = {0:1}

        for num in nums:
            prefix += num

            if prefix - k in prefix_freq:
                count += prefix_freq.get(prefix - k)
            prefix_freq[prefix] = prefix_freq.get(prefix, 0) + 1
        
        return count
solution = Solution()
eg1 = solution.subarraySum([1,1,1], 2)
print(eg1)
eg2 = solution.subarraySum([1,2,3], 3)
print(eg2)
                   

# The reason we use prefix sum here instead of sliding window:
# 1. for sliding window - we need to know for certainity that the values are monotic. that means the numbers in the array are only positive or negative. Hence we can say that when we remove a number from the window the overall sum will decrease or when we add a number in the window the overall sum will increase. 
# But in this question, such certainity is not possible as we can have a negative number anywhere in the array. Hence we go with prefix-sum pattern.

# to undertsand this problem:
# 
# We want to find subarrays that sum to K.
# If we hae a subarray from index i to j that sums to k:
# sum[i..j] = k.
# can be rephrased as : prefix[j] - prefix[i-1] = k
# => prefix[j] - k = prefix[i-1]

# Why did we initiate prefix_freq with {0:1}
# 1: Handle subarrays starting with index 0.
# nums = [3, 3], k = 3

# Index 0: prefix = 3
#   Check: (3 - 3) = 0
#   Is 0 in map? YES! (because we initialized with {0:1})
#   This means subarray [3] (from start) sums to k ✓
# ```

# Without `{0: 1}`, we'd miss subarrays that start from the beginning!

# #2: Mathematical correctness
# ```
# prefix[j] - prefix[-1] = sum[0...j]

# prefix[-1] should be 0 (sum of "nothing" before the array starts)
# ```

# **Visual explanation:**
# ```
# Before array: prefix = 0  ← We record this as {0: 1}
#               ↓
# nums:     [  3,  1,  2  ]
# prefix:   0  3   4   6
# Time complexity: 𝚹(n)
# Space complexity: O(n)