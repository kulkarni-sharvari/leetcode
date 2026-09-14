# 102. Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

################################### Examples ###################################

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level = deque([root])
        bfs = list()

        while level:
            nodeInLevel = len(level)
            nodes = []

            for i in range(nodeInLevel):
                node = level.popleft()

                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

                nodes.append(node.val)

            bfs.append(nodes)

        return(bfs)
            
################################## Complexity ##################################
# Time complexity: Θ(n)
# Space complexity: O(n)


        