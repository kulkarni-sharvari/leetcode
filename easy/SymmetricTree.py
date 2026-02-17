# Question: https://leetcode.com/problems/symmetric-tree/

# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


from Helper.TreeNode import TreeNode
from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val == n2.val and isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)
        return isMirror(root.left, root.right)


solution = Solution()
root1 = TreeNode.from_list([1,2,2,3,4,4,3])
sol = solution.isSymmetric(root1)
print(sol)
root2 = TreeNode.from_list([1,2,2,None,3,None,3])
sol = solution.isSymmetric(root2)
print(sol)

# Time complexity:𝚹(n)
# n = number of nodes in the tree.
# Each node is visited exactly once to find the height from root. Therefore the time complexity = 𝚹(n)

# Space complexity:O(h) where h = height of the tree.
# Recursion stack depth = height of tree
# Best case (balanced): O(log n)
# Worst case (skewed): O(n)