class Solution:
    from collections import deque

    def solve(self, mailboxes):
        # Whenever we process a piece of mail mailboxes[i][j],
        # we enqueue mailboxes[i][j + 1] for processing (if that piece of mail exists.)

        locs = [(i, 0) for i in range(len(mailboxes))]
        result = []
        for i, j in locs:
            if mailboxes[i][j] != "junk":
                result.append(mailboxes[i][j])
            if j + 1 < len(mailboxes[i]):
                locs.append((i, j + 1))
        return result
