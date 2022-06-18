# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def helper(self, root):
    #     if root:
    #         self.helper(root.left)
    #         self.traverse.append(root.val)
    #         self.helper(root.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive
        # self.traverse = []
        # self.helper(root)
        # return self.traverse
        
        # Iterative
        ans = []
        stk = []
        while True:
            while root:
                stk.append(root)
                root = root.left
            if not stk:
                break
            root = stk.pop()
            ans.append(root.val)
            root = root.right
        return ans
            