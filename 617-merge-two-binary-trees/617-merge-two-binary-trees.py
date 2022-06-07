# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2: return None
        val1 = 0 if not root1 else root1.val
        val2 = 0 if not root2 else root2.val
        
        node = TreeNode(val1 + val2)
        
        left1 = root1.left if root1 else root1
        right1 = root1.right if root1 else root1
        left2 = root2.left if root2 else root2
        right2 = root2.right if root2 else root2
        
        node.left = self.mergeTrees(left1, left2)
        node.right = self.mergeTrees(right1, right2)
        
        return node
        