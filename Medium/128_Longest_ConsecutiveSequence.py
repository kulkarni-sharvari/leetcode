# 128. Longest Consecutive Sequence https://leetcode.com/problems/longest-consecutive-sequence/description/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        unique = sorted(list(set(nums)))
        prev, n, count, maxlen = unique[0], len(unique), 1,1

        for i in range(1, n):
            if prev == unique[i] - 1:
                count+=1
            else:
                count = 1
            maxlen = max(maxlen, count)
            prev = unique[i]
            
        return maxlen

# Time Complexity: O(nlgn) 
# Python uses Tim sort under the hood for sorting. It takes O(nlgn).
# Conversion from list to set = O(n)
# Rest of the code runs the number of unique element which in worst case can be O(n).
# Total TC = O(nlgn) + O(n) + O(n) = O(nlgn) 

# Space Complexity: O(n)
# sortedNum[] holds the number of unique elements in nums in sorted order.
# In worst case, all elements can be unique. So Space Complexity = O(n)

################################## Solution 2 ##################################

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        unique = set(nums)
        count, maxlen = 1,1
        for num in unique:
            if num-1 not in unique:
                count = 1
                current = num
                while current+1 in unique:
                    count +=1
                    current = current+1
                maxlen = max(maxlen, count)

        return maxlen