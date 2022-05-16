# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        
        leftHeight = self.getLeftHeight(root.left)
        rightHeight = self.getRightHeight(root.right)
        
        if leftHeight == rightHeight: return (2<<leftHeight)-1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def getLeftHeight(self, node):
        count = 0
        while node!=None:
            count += 1
            node = node.left
        return count
    
    def getRightHeight(self, node):
        count = 0
        while node != None:
            count += 1
            node = node.right
        return count
        