# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        addresses = dict() # stores nodes corresponsing to the values
        
        # consutruct a tree
        for parent, child, isLeft in descriptions:
            
            # creates nodes if they don't exists
            if parent not in addresses: addresses[parent] = TreeNode(parent)
            if child not in addresses: addresses[child] = TreeNode(child)
            
            # get the parent and child nodes
            parentNode = addresses.get(parent)
            childNode = addresses.get(child)
            
            # create a reference from parent to child
            if isLeft: parentNode.left = childNode
            else: parentNode.right = childNode
        
        root = set(addresses.keys()) # assume that all the nodes are root
        
        for parent, child, isLeft in descriptions:
            # a node that is a child cannot be a root
            if child in root:
                root.remove(child)
        
        return addresses[list(root)[0]]
        
        