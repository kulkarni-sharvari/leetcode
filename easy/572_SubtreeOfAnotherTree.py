# 572. Subtree of Another Tree - https://leetcode.com/problems/subtree-of-another-tree/description/

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

################################### Examples ###################################
# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

################################### Solution ###################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.helper(root, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p:
            return False
        if not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def helper(self, p, q):
        if not p:
            return False
        elif self.isSameTree(p, q):
            return True
        else:
            return self.helper(p.left, q) or self.helper(p.right, q)
        
        ################################## Complexity ##################################
# Time complexity: Θ(n)
# Space complexity: O(n)