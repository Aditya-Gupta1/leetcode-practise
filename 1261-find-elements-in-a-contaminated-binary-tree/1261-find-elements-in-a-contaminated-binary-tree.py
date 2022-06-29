# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.values = {0: True}
        self.recover(self.root)
        
    def recover(self, root):
        if not root: return
        if root.left: 
            root.left.val = 2*root.val+1
            self.values[root.left.val] = True
            self.recover(root.left)
        if root.right:
            root.right.val = 2*root.val+2
            self.values[root.right.val] = True
            self.recover(root.right)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)