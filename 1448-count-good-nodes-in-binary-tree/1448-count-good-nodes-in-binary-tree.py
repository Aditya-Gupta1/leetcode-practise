# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, currMax = float(-inf)) -> int:
        if not root: return 0
        currMax = max(currMax, root.val)
        left = self.goodNodes(root.left, currMax)
        right = self.goodNodes(root.right, currMax)
        if currMax <= root.val:
            return left + right + 1
        else:
            return left + right
        