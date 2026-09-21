# 199. Binary Tree Right side View - https://leetcode.com/problems/binary-tree-right-side-view/submissions/2148612916/

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

################################### Examples ###################################
 

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]

# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 4:
# Input: root = []
# Output: []

################################### Solution ###################################

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        
        bfs = deque([root])
        rightView = list()

        while bfs:
            numberOfNodesInLevel = len(bfs)
            for i in range(numberOfNodesInLevel):
                node = bfs.popleft()
                if i == numberOfNodesInLevel-1:
                    rightView.append(node.val)
                if node.left: 
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        
        return rightView

################################## Complexity ##################################

# Time complexity: Θ(n)
# Space complexity: O(n)
