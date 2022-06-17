"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # DFS
        # if root:
        #     yield root.val
        #     for child in root.children:
        #         yield from self.preorder(child)
        
        # BFS
        if not root: return[]
        stk = [root]
        ans = []
        while len(stk) > 0:
            node = stk.pop()
            ans.append(node.val)
            for child in reversed(node.children):
                stk.append(child)
        return ans