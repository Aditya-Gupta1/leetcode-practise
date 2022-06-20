# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root: return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        temp = max(left, right) + 1
        ans = max(temp, left + right + 1)
        self.res = max(ans, self.res)
        return temp
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        self.helper(root)
        return self.res-1