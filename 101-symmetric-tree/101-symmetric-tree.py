# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        if root1.val == root2.val:
            left = self.check(root1.left, root2.right)
            right = self.check(root1.right, root2.left)
            return left and right
        return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # DFS
        # if not root or (not root.left and not root.right): return True
        # return self.check(root.left, root.right)
        
        # BFS
        
        que = [[root, root]]
        while len(que) > 0:
            size = len(que)
            for _ in range(size):
                nodes = que.pop(0)
                if nodes[0].val != nodes[1].val: return False
                if nodes[0].left:
                    if nodes[1].right:
                        que.append([nodes[0].left, nodes[1].right])
                    else: return False
                if nodes[0].right:
                    if nodes[1].left:
                        que.append([nodes[0].right, nodes[1].left])
                    else: return False
        return True