# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.smin = float('inf')
        
        def dfs(node):
            if node:
                if root.val < node.val < self.smin:
                    self.smin = node.val
                if root.val == node.val:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.smin if self.smin != float('inf') else -1