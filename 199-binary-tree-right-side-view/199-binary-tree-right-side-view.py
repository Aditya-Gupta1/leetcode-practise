# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        que = [[root, 0]]
        ans = []
        
        while que:
            node, depth = que.pop(0)
            if depth == len(ans): ans.append(node.val)
            if node.right: que.append((node.right, depth+1))
            if node.left: que.append((node.left, depth+1))
                
        return ans
        
        
        # approach-1: DFS
#         res = []
#         self.helper(root, res, 0)
#         return res
    
    def helper(self, root, res, level):
        if not root: return
        if len(res) == level: res.append(root.val)
        self.helper(root.right, res, level+1)
        self.helper(root.left, res, level+1)