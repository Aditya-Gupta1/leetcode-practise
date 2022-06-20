# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from statistics import multimode
class Solution:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traverse.append(root.val)
            self.inorder(root.right)
            
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse = []
        self.inorder(root)
        return multimode(self.traverse)
        