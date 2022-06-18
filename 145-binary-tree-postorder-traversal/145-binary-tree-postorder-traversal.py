# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # approach 1
        # if root:
        #     yield from self.postorderTraversal(root.left)
        #     yield from self.postorderTraversal(root.right)
        #     yield root.val
        
        # approach 2
        stk = []
        ans = []
        previous = None
        while True:
            while root:
                stk.append(root)
                root = root.left
            while not root and stk:
                root = stk[-1]
                if not root.right or root.right == previous:
                    ans.append(root.val)
                    stk.pop()
                    previous = root
                    root = None
                else:
                    root = root.right
            if not stk: break
        return ans