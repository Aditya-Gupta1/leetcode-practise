# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
            
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
        if not root: return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)