# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        ans = []
        que = [root]
        
        while que:
            currSize = len(que)
            maxEle = float('-inf')
            for _ in range(currSize):
                node = que.pop(0)
                maxEle = max(maxEle, node.val)
                if node.right: que.append(node.right)
                if node.left: que.append(node.left)
            ans.append(maxEle)
        
        return ans