"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        que = collections.deque([root])
        while que:
            curr_size = len(que)
            right = None
            for _ in range(curr_size):
                node = que.popleft()
                node.next = right
                right = node
                if node.right: que.append(node.right)
                if node.left: que.append(node.left)
        return root