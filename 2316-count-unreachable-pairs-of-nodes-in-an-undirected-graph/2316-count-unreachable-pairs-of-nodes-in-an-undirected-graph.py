from collections import defaultdict
class Solution:
    
    def dfs(self, source, graph, visited):
        visited[source] = True
        self.countComp += 1
        for node in graph[source]:
            if not visited[node]: self.dfs(node, graph, visited)
        
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [False for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        ans = (n*(n-1))//2
        
        for i in range(n):
            if not visited[i]:
                self.countComp = 0
                self.dfs(i, graph, visited)
                ans -= (self.countComp * (self.countComp - 1))//2
                
        return ans