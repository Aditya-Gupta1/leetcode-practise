# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        que = [root]
        
        while len(que) > 0:
            node = que.pop(0)
            if node.left:
                if not node.left.right and not node.left.left:
                    total += node.left.val
                que.append(node.left)
            if node.right: que.append(node.right)
        
        return total