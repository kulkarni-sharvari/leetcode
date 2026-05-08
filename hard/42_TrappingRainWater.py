
# 42. Trapping Rain Water: https://leetcode.com/problems/trapping-rain-water/description/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Brute force - worked for 323/324 testcases:
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for h in range(1, len(height)):
            if h>1:
                leftWall = max(height[0:h])
                # print("leftWall", h, height[0:h], leftWall)
            else:
                leftWall = height[0]
            if h+1 < len(height):
                rightWall = max(height[h+1:])
            current = min(leftWall, rightWall) - height[h]
            if current > 0:
                water+=current
            # print(h, leftWall, rightWall, height[h], water)
        return water

# Time complexity: O(n^2)
# Space Complexity: O(n) due to slicing on like 21 and 26.

# Memorizing leftWall
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        leftWall = height[0]
        for h in range(1, len(height)):
            if h+1 < len(height):
                rightWall = max(height[h+1:])
            current = min(leftWall, rightWall) - height[h]
            if current > 0:
                water+=current
            leftWall = max(leftWall, height[h])
            # print(h, leftWall, rightWall, height[h], water)
        return water

# Time complexity: O(n^2)
# Space Complexity: O(n) due to slicing on line rightWall = max(height[h+1:]).

# Memorizing left and right walls:

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        leftWall = height[0]
        rightWall = max(height)

        rightWalls = [0] * n
        rightWalls[n-1] = height[n-1]

        for i in range(n-2, -1, -1):
            rightWalls[i] = max(rightWalls[i+1], height[i])

        for h in range(1, len(height)):
            current = min(leftWall, rightWalls[h]) - height[h]
            if current > 0:
                water+=current
            leftWall = max(leftWall, height[h])
        return water

# Time Complexity: θ(n)
# Space Complexity: O(n)