# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        ans = []
        self.inorderModified(root, ans)
        return ans
        
    def inorderModified(self, root, ans):
        if root:
            self.inorderModified(root.left, ans)
            if not root.right and not root.left:
                ans.append(root.val)
            self.inorderModified(root.right, ans)
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        order1 = self.helper(root1)
        order2 = self.helper(root2)
        if len(order1) != len(order2):
            return False
        for x,y in zip(order1, order2):
            if x!= y: return False
        return True