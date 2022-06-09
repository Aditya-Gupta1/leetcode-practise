# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if root:
            self.helper(root.left)
            self.traverse.append(root.val)
            self.helper(root.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse = []
        self.helper(root)
        return self.traverse