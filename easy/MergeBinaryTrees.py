# Question: https://leetcode.com/problems/merge-two-binary-trees/description/
#
# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.


from Helper.TreeNode import TreeNode
from typing import Optional

class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1 and not root2:
            return root1
        elif not root1 and root2:
            return root2
        elif root1 and not root2:
            return root1

        answer = TreeNode()
        answer.val = root1.val + root2.val
        answer.left = self.mergeTrees(root1.left, root2.left)
        answer.right = self.mergeTrees(root1.right, root2.right)
        return answer


solution = Solution()
root1 = TreeNode.from_list([1,3,2,5])
root2 = TreeNode.from_list([2, 1, 3, None, 4, None, 7])
sol = solution.mergeTrees(root1, root2)
print(sol.to_list())

# Time complexity: O(min(m, n))
# n = number of nodes in root1
# m = number of nodes in root2

# Each overlapping node position is visited once
# Recursion stops when either tree is None
# Each visit performs Θ(1) work (addition, node creation)

# Space Complexity: O(h)
# Recursion call stack uses O(h) space
# h = height of the recursion tree
# Worst case: O(n) for skewed tree
# Best case: O(log n) for balanced tree

# Output space: The merged tree contains between max(m,n) 
# and m+n nodes depending on overlap. 