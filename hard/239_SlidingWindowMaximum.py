# https://leetcode.com/problems/sliding-window-maximum/description/

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        l = r = 0
        result = []

        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop() # removes the right most element
            q.append(r)

            while l>q[0]:
                q.popleft()

            if r+1 >= k:
                result.append(nums[q[0]])
                l+=1

        return result
# Time complexity of above is 𝚹(n)

# Pattern to recognize.
# 1. Sliding window from the question.
# 2. max min query = monotonic queue.
# 3. overlapping problems = maintain a datastructure that solves repeated question. here it happened to be a monotnic queue.


# -----------------------------------------------------------------------------

#  The below code exceeds time because 
#           maxIndex, maxValue = max(enumerate(nums[l: right+1]), key=lambda x: x[1])
#  this is O(n) operation. which slows down the algorithm

# left = 0
# result = []
# index = []
# for right in range(k - 1, len(nums)):
#     if len(index) > 0 and index[-1] >= left and index[-1] <= right:
#         if nums[index[-1]] > nums[right]:
#             index.append(index[-1])
#         else:
#             index.append(right)
#     else:
#         l = right-k+1 if len(index) == 0 else index[-1]+1
#         maxIndex, maxValue = max(enumerate(nums[l: right+1]), key=lambda x: x[1])
#         index.append(left + maxIndex)
#     # while(nums[left] < nums[-1]):
#     left+=1
# for i in range(len(index)):
#     index[i] = nums[index[i]]
# return index
