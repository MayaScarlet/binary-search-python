"""
Implement a stack with the following methods:

MinimumStack() constructs a new instance of a minimum stack
append(int val) appends val to the stack
peek() retrieves the last element in the stack
min() retrieves the minimum value in the stack
pop() pops and returns the last element in the stack
Each method should be done in \mathcal{O}(1)O(1) time. You can assume that for peek, min and pop, the stack is non-empty when they are called.

Constraints

n ≤ 100,000 where n is the number of calls to append, peek, min, and pop.
Example 1
Input
methods = ["constructor", "append", "append", "min", "peek", "pop", "pop"]
arguments = [[], [1], [2], [], [], [], []]`

"""


class MinimumStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def append(self, val):
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def peek(self):
        return self.stack[-1]


    def min(self):
        return self.min_stack[-1]

    def pop(self):
        val = self.stack.pop()
        self.min_stack.pop()
        return val
