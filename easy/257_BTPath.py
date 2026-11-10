# 257: Binary Tree path - https://leetcode.com/problems/binary-tree-paths/description/
# You are given the root of a binary tree.

# Return all root-to-leaf paths in any order.

# A leaf is a node with no children.

 
################################### Examples ###################################

# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Example 2:
# Input: root = [1]
# Output: ["1"]

################################### Solution ###################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:

        res,path = [],[root.val]

        def backtracking(curr):
            if not curr.left and not curr.right:
                res.append("->".join(map(str, path)))
            
            
            if curr.left:
                path.append(curr.left.val)
                backtracking(curr.left)
                # path.pop()
            if curr.right:
                path.append(curr.right.val)
                backtracking(curr.right)
            path.pop()

        
        backtracking(root)
        return res
        