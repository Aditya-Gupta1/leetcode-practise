# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # approach-1: BFS
#         ansDepth = 0
#         maxSum = float('-inf')
        
#         que = [root]
#         depth = 0
        
#         while que:
            
#             currSize = len(que)
#             total = 0
            
#             for _ in range(currSize):
#                 node = que.pop(0)
#                 total += node.val
                
#                 if node.left: que.append(node.left)
#                 if node.right: que.append(node.right)
            
#             depth += 1
            
#             if total > maxSum:
#                 maxSum = total
#                 ansDepth = depth
        
#        return ansDepth
        
        # approach-2: DFS
        def dfs(root, totals, level):
            if not root: return
            
            if len(totals) == level:
                totals.append(root.val)
            else:
                totals[level] += root.val
            
            dfs(root.left, totals, level+1)
            dfs(root.right, totals, level+1)
        
        totals = []
        dfs(root, totals, 0)
        return 1 + totals.index(max(totals))