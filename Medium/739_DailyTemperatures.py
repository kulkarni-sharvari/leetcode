# 739. Daily Temperatures: https://leetcode.com/problems/daily-temperatures/description/

# Description:
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        warmerIndices = list()

        for i in range(n-1, -1, -1):
            while warmerIndices and temperatures[warmerIndices[-1]] <= temperatures[i]: 
                # Remove days that are not warmer than today,
                # since they cannot be the next warmer day for this index.
                warmerIndices.pop()
            if warmerIndices:
                answer[i] = warmerIndices[-1] - i
            warmerIndices.append(i)

        return answer

# Time Complexity: Θ(n)
# Space complexity: O(n)