# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        
        sortedCountMap = {k:v for k, v in sorted(countMap.items(), key = lambda item: item[1], reverse=True)}
        sol = list()
        
        for key in sortedCountMap:
            if len(sol) < k:
                sol.append(key)
        return(sol)

solution = Solution()
sol = solution.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)
print(sol)