# 226. Invert Binary Tree - https://leetcode.com/problems/invert-binary-tree/description/

# Given the root of a binary tree, invert the tree, and return its root.

################################### Examples ###################################
# 1. Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# 2. Input: root = [2,1,3]
# Output: [2,3,1]

# 3. Input: root = []
# Output: []

################################### Solution ###################################
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root 

################################## Complexity ##################################
# Time complexity: Θ(n)
# Space complexity: O(1)