# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root: return 0
        if not root.right and not root.left: return 1
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        return max(left, right)+1
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        height = self.height(root)
        total = 0
        que = [root]
        tempHeight = 0
        
        while que:
            tempHeight += 1
            currSize = len(que)
            
            for _ in range(currSize):
                node = que.pop(0)
                if tempHeight == height: total += node.val
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
        
        return total