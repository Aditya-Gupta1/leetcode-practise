# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPaths(self, root, path = ""):
        if not root: return
        if not root.right and not root.left:
            path += str(root.val)
            self.ans.append(path)
            return
        self.findPaths(root.left, path + str(root.val) + "->")
        self.findPaths(root.right, path + str(root.val) + "->")
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.findPaths(root)
        return self.ans