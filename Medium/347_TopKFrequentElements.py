# 347. Top K Frequent Elements
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

# Time complexity analysis: 𝚹(nlgn)
# Explanation:
# countMap = Counter(nums) = O(n) steps.
# sortedCountMap = {k:v for k, v in sorted(countMap.items(), key = lambda item: item[1], reverse=True)} = O(m log m) steps where m is number of unique elements in the array.
# Lines 18 to 20 = O(m) steps.

# Overall time complexity = O(n + m log m + m) = O(n + m log m)

# Since m ≤ n:
# - Best case: m = 1 → Ω(n)
# - Worst case: m = n → O(n log n)

# Space complexity: O(m) if m = n then O(n)
