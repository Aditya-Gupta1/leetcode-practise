class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i = j = 0
        
        while i < n or j < n:
            
            while i < n and start[i] == '_': i += 1
            while j < n and target[j] == '_': j += 1
            
            if i == n or j == n: return i == n and j == n
            
            if start[i] != target[j]: return False
            
            if target[j] == 'L':
                if j > i: return False
            
            elif target[j] == 'R':
                if j < i: return False
            
            i += 1
            j += 1
        
        return i == n and j == n