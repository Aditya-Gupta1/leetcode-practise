# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # approach 1
        if root:
            yield from self.postorderTraversal(root.left)
            yield from self.postorderTraversal(root.right)
            yield root.val
            