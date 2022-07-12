# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, result, depth):
        if not root: return
        
        if len(result) == depth: result.append(root.val)
        else: result[depth] = max(result[depth], root.val)
            
        self.helper(root.left, result, depth+1)
        self.helper(root.right, result, depth+1)
        
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # approach 1
#         if not root: return []
        
#         ans = []
#         que = [root]
        
#         while que:
#             currSize = len(que)
#             maxEle = float('-inf')
#             for _ in range(currSize):
#                 node = que.pop(0)
#                 maxEle = max(maxEle, node.val)
#                 if node.right: que.append(node.right)
#                 if node.left: que.append(node.left)
            # ans.append(maxEle)
        
#         return ans
        # approach-2
        result = []
        depth = 0
        self.helper(root, result, depth)
        return result