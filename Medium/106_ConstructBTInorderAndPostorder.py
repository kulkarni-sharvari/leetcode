# 106. Construct Binary Tree from Inorder and Postorder Traversal -  https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

################################### Examples ###################################

# Example 1:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

################################### Solution ###################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        inorderIdx = dict()
        inorderLen = len(inorder)
        for i in range(inorderLen):
            inorderIdx[inorder[i]] = i

        def helper(left, right):
            if left >= right:
                return None

            root = TreeNode(postorder.pop())
            idx = inorderIdx[root.val]
            
            root.right = helper(idx+1,right)
            root.left = helper(left, idx)
            return root
        
        return helper(0, inorderLen)

################################## Complexity ##################################

# Time complexity: Θ(n)
# Space complexity: O(n)
