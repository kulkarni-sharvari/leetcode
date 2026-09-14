
# 111. Minimum Depth of Binary Tree - https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

################################### Examples ###################################

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
################################### Solution ###################################

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        level = deque([root])
        depth = 0

        while level:
            nodesInLevel = len(level)
            for i in range(nodesInLevel):
                node = level.popleft()
                if not node.left and not node.right:
                    return depth + 1
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            depth += 1

################################## Complexity ##################################
# Time complexity: Θ(n)
# Space complexity: O(n)

# Because we have to find the min depth => minimum level at which there is a leaf, we do level order traversal.