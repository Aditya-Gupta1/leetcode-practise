# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, parent, grandParent):
        if not root: return 0
        left = self.helper(root.left, root.val, parent)
        right = self.helper(root.right, root.val, parent)
        
        if grandParent % 2 == 0:
            return left+right+root.val
        return left+right
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.helper(root, 1, 1)