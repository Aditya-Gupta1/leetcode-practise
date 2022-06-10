# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, low, high):
        if not root: return
        if low <= root.val <= high:
            self.total += root.val
            self.helper(root.left, low, high)
            self.helper(root.right, low, high)
        elif root.val < low:
            self.helper(root.right, low, high)
        else:
            self.helper(root.left, low, high)
            
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # approach-1
#         que = [root]
#         total = 0
        
#         while que:
#             node = que.pop(0)
#             if low <= node.val <= high:
#                 total += node.val
#             if node.left: que.append(node.left)
#             if node.right: que.append(node.right)
        
#         return total

        # approach-2
        self.total = 0
        self.helper(root, low, high)
        return self.total