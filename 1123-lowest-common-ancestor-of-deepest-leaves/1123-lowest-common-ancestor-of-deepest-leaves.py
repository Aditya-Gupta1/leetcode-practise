class Solution:
    # def lca(self, root, nodes):
    #     if not root: return None
    #     if root in nodes: return root
    #     left = self.lca(root.left, nodes)
    #     right = self.lca(root.right, nodes)
    #     if not left: return right
    #     if not right: return left
    #     return root
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # brute force
#         if not root.left and not root.right: return root
        
#         maxDepth = 0
#         deepestLeaves = []
#         que = [[root, 0]]
        
#         while que:
#             node, depth = que.pop(0)
#             if depth > maxDepth:
#                 deepestLeaves = [node]
#                 maxDepth = depth
#             elif depth == maxDepth:
#                 deepestLeaves.append(node)
#             if node.left: que.append([node.left, depth+1])
#             if node.right: que.append([node.right, depth+1])
        
        # if len(deepestLeaves) == 1: return deepestLeaves[0]
        
#         return self.lca(root, deepestLeaves)
        
        # approach 2
        def helper(root):
            if not root: return [0, root]
            leftHeight, leftLCA = helper(root.left)
            rightHeight, rightLCA = helper(root.right)
            if leftHeight > rightHeight:
                return [leftHeight+1, leftLCA]
            if rightHeight > leftHeight:
                return [rightHeight+1, rightLCA]
            return [leftHeight+1, root]
        
        return helper(root)[1]