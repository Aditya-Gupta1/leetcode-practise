      
class Solution:
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        children = [[] for _ in range(n)]
        for emp, man in enumerate(manager):
            if man != -1:
                children[man].append(emp)
        
        def dfs(emp):
            maxTime = 0
            for child in children[emp]:
                time = dfs(child)
                maxTime = max(maxTime, time)
            return maxTime + informTime[emp]
        
        return dfs(headID)