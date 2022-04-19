class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, node1, node2):
        if node1 is None and node2 is None:
            return None

        val1 = node1.val if node1 else 0
        val2 = node2.val if node2 else 0

        root = Tree(val1 + val2)
        root.left = self.solve(node1.left if node1 else None,
                node2.left if node2 else None
            )
        root.right = self.solve(node1.right if node1 else None,
                node2.right if node2 else None
            )
        return root
