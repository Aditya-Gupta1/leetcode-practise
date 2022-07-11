# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, freq):
        if not root: return
        if not root.right and not root.left:
            freq[root.val] = freq.get(root.val, 0) + 1
            
            nOdds = 0
            for k, v in freq.items():
                if v % 2 != 0: nOdds += 1
            if nOdds <= 1: self.ans += 1
            
            freq[root.val] -= 1
            
            return
        
        freq[root.val] = freq.get(root.val, 0) + 1
        
        self.helper(root.left, freq)
        self.helper(root.right, freq)
        
        freq[root.val] -= 1
        
        return
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.helper(root, dict())
        return self.ans