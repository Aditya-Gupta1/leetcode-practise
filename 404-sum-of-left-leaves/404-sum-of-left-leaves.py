# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root):
        if root.left:
            if not root.left.left and not root.left.right:
                self.total += root.left.val
            self.helper(root.left)
        if root.right: self.helper(root.right)
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        # BFS
#         total = 0
#         que = [root]
        
#         while len(que) > 0:
#             node = que.pop(0)
#             if node.left:
#                 if not node.left.right and not node.left.left:
#                     total += node.left.val
#                 que.append(node.left)
#             if node.right: que.append(node.right)
        
#         return total
        # DFS
        
        self.total = 0
        self.helper(root)
        return self.total
        