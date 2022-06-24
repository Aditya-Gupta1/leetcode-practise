# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from hashlib import sha256
class Solution:
    def isIdentical(self, root1, root2):
        if not root1 and not root2: return True
        if root1 and root2:
            if root1.val == root2.val:
                left = self.isIdentical(root1.left, root2.left)
                right = self.isIdentical(root1.right, root2.right)
                return left and right
            else: return False
        return False
    
    def hash(self, value):
        s = sha256()
        value = value.encode('utf-8')
        s.update(value)
        return s.hexdigest()
    
    def merkle(self, root):
        if not root: return '#'
        left = self.merkle(root.left)
        right = self.merkle(root.right)
        root.merkle = self.hash(left + str(root.val) + right)
        return root.merkle
    
    def dfs(self, root, subRoot):
        if not root: return False
        return root.merkle == subRoot.merkle or self.dfs(root.right, subRoot) or self.dfs(root.left, subRoot)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # approach 1
        # if not root and not subRoot: return True
        # que = [root]
        # ans = []
        # while que:
        #     node = que.pop(0)
        #     if node.val == subRoot.val:
        #         ans.append(self.isIdentical(node, subRoot))
        #     if node.left: que.append(node.left)
        #     if node.right: que.append(node.right)
        # return any(ans)
        
        # approach 2
        self.merkle(root)
        self.merkle(subRoot)
        
        return self.dfs(root, subRoot)