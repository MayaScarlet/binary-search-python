class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_middle_node(self, node):
        slow, fast = node, node.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow

    def merge(self, node1, node2):
        dummy = tail = LLNode(None)
        while node1 and node2:
            if node1.val < node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next

        if node1:
            tail.next = node1
        elif node2:
            tail.next = node2

        return dummy.next

    def solve(self, node):
        if not node or not node.next:
            return node

        left = node
        right = self.get_middle_node(node)

        temp = right.next
        right.next = None
        right = temp

        left = self.solve(left)
        right = self.solve(right)
        return self.merge(left, right)
