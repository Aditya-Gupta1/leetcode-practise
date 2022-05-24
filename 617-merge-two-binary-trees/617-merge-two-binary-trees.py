# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2: return None
        
        val1 = 0 if root1 == None else root1.val
        val2 = 0 if root2 == None else root2.val
        
        newNode = TreeNode(val1 + val2)
        
        leftTree1 = None if root1 == None else root1.left
        rightTree1 = None if root1 == None else root1.right
        leftTree2 = None if root2 == None else root2.left
        rightTree2 = None if root2 == None else root2.right
        
        newNode.left = self.mergeTrees(leftTree1, leftTree2)
        newNode.right = self.mergeTrees(rightTree1, rightTree2)
        
        return newNode
        