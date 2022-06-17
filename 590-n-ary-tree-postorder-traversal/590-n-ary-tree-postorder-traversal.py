"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
            
    def postorder(self, root: 'Node') -> List[int]:
        if root:
            for child in root.children:
                yield from self.postorder(child)
            yield root.val