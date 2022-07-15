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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        if not root.left and not root.right: return root
        
        que = [root.left, root.right]
        while que:
            
            currSize = len(que)
            prevNode = que.pop(0)
            
            if prevNode.left: que.append(prevNode.left)
            if prevNode.right: que.append(prevNode.right)
            
            for i in range(currSize-1):
                nextNode = que.pop(0)
                prevNode.next = nextNode
                if nextNode.left: que.append(nextNode.left)
                if nextNode.right: que.append(nextNode.right)
                prevNode = nextNode

        return root