# 4. Median of two sorted arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = sorted(nums1+nums2)
        n = len(merge)
        if n%2 == 0:
            mid = int(n/2)
            return ((merge[mid] + merge[mid - 1])/2)
        else:
            return merge[n//2]


# Time complexity: O((n+m) log(n+m))
# Space Complexity: O(n+m)