"""
Given a binary tree root, return whether all leaves are at the same level.

Constraints:
n ≤ 100,000 where n is the number of nodes in root

Example:
        3
      /   \
     4     1
      \   /
       2 0
Leaf 2 and 0 are on the same level

"""


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def solve(self, root):
        leaf_set = {}
        queue = [root]
        level = []
        curr_level = 0

        while queue:
            for node in queue:
                if node.right is None and node.left is None:
                    if curr_level not in leaf_set:
                        leaf_set[curr_level] = [node.val]
                    else:
                        leaf_set[curr_level].append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
            level = []
            curr_level += 1

        levels = leaf_set.keys()
        return len(levels) == 1
