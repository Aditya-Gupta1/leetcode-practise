# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS
        # if not root: return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
        
        # BFS
        if not root: return root
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return root