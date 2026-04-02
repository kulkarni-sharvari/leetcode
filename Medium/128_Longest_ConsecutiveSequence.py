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
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        sortedNums = sorted(list(set(nums)))
        p1 = 0
        p2 = 0
        while(p2<len(sortedNums)):
            if p2>0 and sortedNums[p2] - 1 != sortedNums[p2-1]:
                p1 = p2
            p2+=1
            maxCount = max(maxCount, p2-p1)
        return maxCount

# Time Complexity: O(nlgn) 
# Python uses Tim sort under the hood for sorting. It takes O(nlgn).
# Conversion from list to set = O(n)
# Rest of the code runs the number of unique element which in worst case can be O(n).
# Total TC = O(nlgn) + O(n) + O(n) = O(nlgn) 

# Space Complexity: O(n)
# sortedNum[] holds the number of unique elements in nums in sorted order.
# In worst case, all elements can be unique. So Space Complexity = O(n)