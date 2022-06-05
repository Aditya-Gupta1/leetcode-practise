# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        # DFS
        # if not root: return False
        # if not root.left and not root.right:
        #     if target == root.val: return True
        #     else: return False
        # if self.hasPathSum(root.left, target - root.val): return True
        # else: return self.hasPathSum(root.right, target - root.val)
        
        # BFS
        if not root: return False
        que = [[root, target - root.val]]
        while len(que) > 0:
            node, value = que.pop(0)
            if not node.left and not node.right and value == 0: return True
            if node.left:
                que.append([node.left, value - node.left.val])
            if node.right:
                que.append([node.right, value - node.right.val])
        return False