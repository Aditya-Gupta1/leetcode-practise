# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ansDepth = 0
        maxSum = float('-inf')
        
        que = [root]
        depth = 0
        
        while que:
            
            currSize = len(que)
            total = 0
            
            for _ in range(currSize):
                node = que.pop(0)
                total += node.val
                
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            
            depth += 1
            
            if total > maxSum:
                maxSum = total
                ansDepth = depth
        
        return ansDepth