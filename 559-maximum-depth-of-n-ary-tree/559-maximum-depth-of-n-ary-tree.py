"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        # DFS
        # if not root: return 0
        # maxHeight = 0
        # for child in root.children:
        #     height = self.maxDepth(child)
        #     maxHeight = max(maxHeight, height)
        # return maxHeight + 1
        
        # BFS
        if not root: return 0
        que = [root]
        depth = 0
        while len(que) > 0:
            currLen = len(que)
            for i in range(currLen):
                node = que.pop(0)
                for child in node.children:
                    que.append(child)
            depth += 1
        return depth