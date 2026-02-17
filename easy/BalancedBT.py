# Question:https://leetcode.com/problems/balanced-binary-tree/description/?source=submission-noac

# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.

from Helper.TreeNode import TreeNode
from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node:
                return (True, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            balanced = left[0] and right[0] and abs(right[1]-left[1])<=1
            return (balanced, 1+ max(left[1],right[1]))
        return dfs(root)[0]

solution = Solution()
root1 = TreeNode.from_list([3,9,20,None,None,15,7])
sol = solution.isBalanced(root1)
print(sol)
root2 = TreeNode.from_list([1,2,3,4,5,6,None,8])
sol = solution.isBalanced(root2)
print(sol)

# Time complexity:𝚹(n)
# n = number of nodes in the tree.
# Each node is visited exactly once to find the height from root. Therefore the time complexity = 𝚹(n)

# Space complexity:O(h) where h = height of the tree.
# Recursion stack depth = height of tree
# Best case (balanced): O(log n)
# Worst case (skewed): O(n)
