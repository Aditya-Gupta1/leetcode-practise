# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.nodes.append(root.val)
            self.inorder(root.right)
            
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.nodes = []
        self.inorder(root)
        minDiff = 1000000
        for i in range(1, len(self.nodes)):
            minDiff = min(minDiff, self.nodes[i] - self.nodes[i-1])
        return minDiff