class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    @staticmethod
    def from_list(values):
        if not values:
            return None

        it = iter(values)
        root_val = next(it)
        if root_val is None:
            return None

        root = TreeNode(root_val)
        queue = [root]

        try:
            while queue:
                node = queue.pop(0)

                # Left child
                left_val = next(it)
                if left_val is not None:
                    node.left = TreeNode(left_val)
                    queue.append(node.left)

                # Right child
                right_val = next(it)
                if right_val is not None:
                    node.right = TreeNode(right_val)
                    queue.append(node.right)

        except StopIteration:
            pass

        return root

    
    def to_list(self):
        if not self:
            return None
        result = []
        queue = [self]
        while queue:
            node = queue.pop()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return result