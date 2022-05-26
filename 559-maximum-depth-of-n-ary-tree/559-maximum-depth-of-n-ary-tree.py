"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        maxHeight = 0
        for child in root.children:
            height = self.maxDepth(child)
            maxHeight = max(maxHeight, height)
        return maxHeight + 1