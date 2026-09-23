# 124. Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

################################### Examples ###################################

# Example 1:
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

################################### Solution ###################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxSum = root.val

        def dfs(node, currentSum):
            nonlocal maxSum

            if not node:
                return 0

            leftSum  = dfs(node.left, currentSum)
            rightSum = dfs(node.right, currentSum)

            currentSum  = max(node.val + leftSum + rightSum, node.val + leftSum, node.val + rightSum, node.val)


            maxSum = max(maxSum, currentSum)
            return max(node.val + leftSum, node.val + rightSum, node.val)
        
        dfs(root, 0)
        return maxSum
        
################################## Complexity ##################################

# Time complexity: Θ(n)
# Space complexity: O(n)