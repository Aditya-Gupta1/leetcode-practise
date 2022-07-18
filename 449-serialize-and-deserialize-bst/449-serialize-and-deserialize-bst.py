# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return "X,"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + right
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        que = collections.deque(data.split(","))
        return self.helper(que)
    
    def helper(self, que):
        item = que.popleft()
        if item == 'X': return None
        node = TreeNode(int(item))
        node.left = self.helper(que)
        node.right = self.helper(que)
        return node
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans