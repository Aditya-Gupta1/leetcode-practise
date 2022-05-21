# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if not original or original == target: return cloned
        res = self.getTargetCopy(original.left, cloned.left, target)
        if res: return res
        return self.getTargetCopy(original.right, cloned.right, target)
        
        # BFS
#         originalQueue = [original]
#         cloneQueue = [cloned]
        
#         while len(originalQueue) != 0 and len(cloneQueue) != 0:
#             origElement = originalQueue[0]
#             cloneElement = cloneQueue[0]
            
#             if origElement == target:
#                 return cloneElement
            
#             if origElement.left: 
#                 originalQueue.append(origElement.left)
#                 cloneQueue.append(cloneElement.left)
#             if origElement.right: 
#                 originalQueue.append(origElement.right)
#                 cloneQueue.append(cloneElement.right)
            
#             originalQueue.pop(0)
#             cloneQueue.pop(0)
        
#         return None