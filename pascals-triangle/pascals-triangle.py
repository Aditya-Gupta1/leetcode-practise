class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 0: return []
        if n == 1: return [[1]]
        if n == 2: return [[1], [1, 1]]
        
        result = [[1], [1, 1]]
        
        for row in range(3, n+1):
            row_elements = [1]
            for col in range(row-2):
                row_elements.append(result[row-2][col] + result[row-2][col+1])
            row_elements.append(1)
            result.append(row_elements)
        
        return result