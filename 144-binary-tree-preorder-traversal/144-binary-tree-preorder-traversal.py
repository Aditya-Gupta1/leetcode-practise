# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stk = []
        while True:
            while root:
                ans.append(root.val)
                stk.append(root)
                root = root.left
            if not stk: break
            root = stk.pop()
            root = root.right
        return ans