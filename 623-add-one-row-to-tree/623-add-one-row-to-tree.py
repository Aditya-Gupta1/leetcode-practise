# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertChild(self, node, val):
        left, right = node.left, node.right
        node.left = TreeNode(val)
        node.right = TreeNode(val)
        node.left.left = left
        node.right.right = right
        
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        que = collections.deque([root])
        curr_depth = 1
        
        while que:
            curr_size = len(que)
            for _ in range(curr_size):
                node = que.popleft()
                if curr_depth == depth-1:
                    self.insertChild(node, val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            curr_depth += 1
            if curr_depth == depth: break
        
        return root