from collections import defaultdict
class TreeNode:
    def __init__(self, val, children = None):
        self.val = val
        self.children = [] if children == None else children
        
class Solution:
    def constructTree(self, headID, managers, informTime, n):
        nodes = dict()
        for i in range(n):
            nodes[i] = TreeNode(i)
        
        for employee, manager in enumerate(managers):
            if manager != -1:
                nodes[manager].children.append(nodes[employee])
        
        return nodes[headID]
    
    def numOfMinutesUtil(self, root, informTime):
        if not root: return 0
        
        maxTime = 0
        for child in root.children:
            time = self.numOfMinutesUtil(child, informTime)
            maxTime = max(maxTime, time)
        
        return maxTime + informTime[root.val]
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        root = self.constructTree(headID, manager, informTime, n)
        return self.numOfMinutesUtil(root, informTime)
        