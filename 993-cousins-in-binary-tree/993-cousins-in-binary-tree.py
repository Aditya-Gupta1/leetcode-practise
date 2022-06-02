# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, depth, parent, target):
        if not root: return [-1, -1]
        if root.val == target: return [depth, parent]
        left = self.helper(root.left, depth+1, root.val, target)
        if left != [-1, -1]: return left
        return self.helper(root.right, depth+1, root.val, target)
    
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # DFS
#         if root.val == x or root.val == y: return False
        
#         xDepth, xParent = self.helper(root, 0, -1, x)
#         yDepth, yParent = self.helper(root, 0, -1, y)
        
#         if xDepth == yDepth and xParent != yParent: return True
#         return False
        
        # BFS
        
        if not root or root.val == x or root.val == y: return False
        que = [root]
        while len(que) > 0:
            currSize = len(que)
            xExists = False
            yExists = False
            for _ in range(currSize):
                node = que.pop(0)
                if node.val == x: xExists = True
                if node.val == y: yExists = True
                if node.left and node.right:
                    if set([node.left.val, node.right.val]) == set([x, y]):
                        return False
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            if xExists and yExists: return True
        return False