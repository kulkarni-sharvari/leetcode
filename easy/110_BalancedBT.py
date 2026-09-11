# 110: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/
# Given a binary tree, determine if it is height-balanced.
# Height balanced: A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

################################### Examples ###################################

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

################################### Solution ###################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root)[0]
        

    def dfs(self, node):
        if not node:
            return (True,0)
        else:
            left = self.dfs(node.left)
            right = self.dfs(node.right)
            isBalanced = left[0] and right[0] and abs(right[1]-left[1])<=1
            return(isBalanced, 1+ max(left[1], right[1]))
            
################################## Complexity ##################################
# Time complexity: Θ(n)
# Space complexity: O(n)
