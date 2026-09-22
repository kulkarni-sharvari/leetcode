# 98.  Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/description/
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

################################### Examples ###################################

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Exampke 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

################################### Solution ###################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.inorder(root, float(-inf), float(inf))
        
    def inorder(self, node, left, right):
        if not node:
            return True

        if node.val>=right or node.val<=left:
            return False
        
        return self.inorder(node.left, left, node.val) and self.inorder(node.right, node.val, right)
        
################################## Complexity ##################################

# Time complexity: Θ(n)
# Space complexity: O(n)