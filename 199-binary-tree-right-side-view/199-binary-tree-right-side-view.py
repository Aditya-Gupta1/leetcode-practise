# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res, 0)
        return res
    
    def helper(self, root, res, level):
        if not root: return
        if len(res) == level: res.append(root.val)
        self.helper(root.right, res, level+1)
        self.helper(root.left, res, level+1)