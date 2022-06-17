"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def traverse(self, root):
        if root:
            for child in root.children:
                yield from self.traverse(child)
            yield root.val
            
            
    def postorder(self, root: 'Node') -> List[int]:
        return self.traverse(root)