# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addParents(self, root, parent):
        if not root: return
        root.parent = parent
        self.addParents(root.right, root)
        self.addParents(root.left, root)
    
    def findTarget(self, root, target):
        if not root: return None
        if root.val == target.val: return root
        left = self.findTarget(root.left, target)
        if left: return left
        return self.findTarget(root.right, target)
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # add parents to every node
        self.addParents(root, None)
        # find the target node in the tree
        targetNode = self.findTarget(root, target)
        # BFS
        que = [(targetNode, 0)]
        res = []
        visited = dict()
        
        while que:
            node, depth = que.pop(0)
            if node.val not in visited:
                if depth == k: res.append(node.val)
                if node.left: que.append((node.left, depth+1))
                if node.right: que.append((node.right, depth+1))
                if node.parent: que.append((node.parent, depth+1))
                visited[node.val] = True
            
        
        return res