# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root:
            yield from self.inorder(root.left)
            yield root.val
            yield from self.inorder(root.right)
            
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # approach-1
        ans = curr = TreeNode(None)
        for node in self.inorder(root):
            curr.right = TreeNode(node)
            curr = curr.right
        return ans.right