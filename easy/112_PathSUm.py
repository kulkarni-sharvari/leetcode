# 112. Path Sum - https://leetcode.com/problems/path-sum/description/

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

################################### Examples ###################################

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There are two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Example 3:
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf pa

################################### Solution ###################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # DFS approach
        return self.dfs(root, 0, targetSum)

    def dfs(self, node, currentSum, targetSum):
        
        if not node:
            return False
        elif not node.left and not node.right:
            currentSum += node.val
            return currentSum == targetSum
        else:
            return self.dfs(node.left, node.val + currentSum, targetSum) or self.dfs(node.right, node.val + currentSum, targetSum)
        
################################## Complexity ##################################
# Time complexity: Θ(n)
# Space complexity: O(n)

################################## Explanation #################################
# I used DFS because we needed to find from root to leaf.
# We had to send data down the tree so i sent that information as parameter to the recursive function.
