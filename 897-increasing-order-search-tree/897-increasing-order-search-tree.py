# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder2(self, root):
        if root:
            self.inorder2(root.left)
            self.curr.right = root
            root.left = None
            self.curr = self.curr.right
            self.inorder2(root.right)
            
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        self.curr = ans = TreeNode(None)
        self.inorder2(root)
        return ans.right
        