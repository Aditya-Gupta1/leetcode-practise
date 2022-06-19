# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def findPaths(self, root, path = ""):
    #     if not root: return
    #     if not root.right and not root.left:
    #         path += str(root.val)
    #         self.ans.append(path)
    #         return
    #     self.findPaths(root.left, path + str(root.val) + "->")
    #     self.findPaths(root.right, path + str(root.val) + "->")
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # approach 1
        # self.ans = []
        # self.findPaths(root)
        # return self.ans
        
        # approach 2
        que = [[root, ""]]
        ans = []
        while que:
            node, path = que.pop(0)
            if not node.left and not node.right:
                path += str(node.val)
                ans.append(path)
            if node.left:
                que.append([node.left, path + str(node.val) + "->"])
            if node.right:
                que.append([node.right, path + str(node.val) + "->"])
        return ans