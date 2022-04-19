class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, node, k):
        if node is None:
            return node

        # find length of LL
        tail, length = node, 1
        while tail.next:
            tail, length = tail.next, length + 1

        #reduce rotations by using k mod length
        k = k % length

        # if k == 0, return node
        if k == 0:
            return node

        #find the node prev to Kth node from end
        curr = node
        for _ in range(length - k - 1):
            curr = curr.next

        #new head with the node next to prev, here next to the current
        #Store new head, assign curr.next to None and link last node's next to head
        head = curr.next
        curr.next = None
        tail.next = node

        return head
