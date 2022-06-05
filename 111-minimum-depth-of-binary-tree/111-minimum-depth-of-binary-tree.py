# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        # if not root: return 0
        # if not root.right and not root.left: return 1
        # left = self.minDepth(root.left)
        # right = self.minDepth(root.right)
        # if not left: return right + 1
        # if not right: return left + 1
        # return min(left, right) + 1
        # BFS
        if not root: return 0
        que = [[root, 1]]
        while que:
            node, depth = que.pop(0)
            if not node.left and not node.right: return depth
            if node.left:
                que.append([node.left, depth+1])
            if node.right:
                que.append([node.right, depth+1])
        return False