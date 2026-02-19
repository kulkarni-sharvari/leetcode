# Question: https://leetcode.com/problems/diameter-of-binary-tree/

# 543. Diameter of Binary Tree

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

from Helper.TreeNode import TreeNode
from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal diameter
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right)
            return 1+ max(left, right)
        dfs(root)
        return diameter


solution = Solution()
root1 = TreeNode.from_list([1,2,3,4,5])
sol = solution.diameterOfBinaryTree(root1)
print(sol)