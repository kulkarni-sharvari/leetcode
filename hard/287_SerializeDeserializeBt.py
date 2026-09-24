# 287. Serialize and deserialize binary tree - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

################################### Examples ###################################

# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:
# Input: root = []
# Output: []

################################### Solution ###################################

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def __init__(self):
        self.serialized = list()

    def serialize(self, root):
        response = list()

        def dfs(node):

            if not node:
                response.append("N")
                return
            else:
                response.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(response)
        
                
    def deserialize(self, data):
        treeDeque = deque(data.split(','))
        def dfs():
            nodeVal = treeDeque.popleft()
            if nodeVal == "N":
                return
            node = TreeNode(nodeVal)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

################################## Complexity ##################################

# Time complexity: Θ(n)
# Space complexity: O(n)