# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def util(self, root, currNum = "", total = 0):
        if not root: return total
        if not root.right and not root.left:
            total += int(currNum + str(root.val), 2)
            return total
        left = self.util(root.left, currNum + str(root.val), total)
        right = self.util(root.right, currNum + str(root.val), total)
        return left + right
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.util(root)