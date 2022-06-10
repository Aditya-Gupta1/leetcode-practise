# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        que = [root]
        total = 0
        
        while que:
            node = que.pop(0)
            if low <= node.val <= high:
                total += node.val
            if node.left: que.append(node.left)
            if node.right: que.append(node.right)
        
        return total