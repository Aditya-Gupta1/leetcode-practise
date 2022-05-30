# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return [0]
        ans = []
        que = [root]
        
        while len(que) > 0:
            currSize = len(que)
            total = 0
            for _ in range(currSize):
                node = que.pop(0)
                total += node.val
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            ans.append(total/currSize)
        return ans