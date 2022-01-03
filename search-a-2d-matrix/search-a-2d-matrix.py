class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        target_arr = matrix[0]
        
        for i in range(rows):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                target_arr = matrix[i]
        
        return self.binary_search(target_arr, 0, cols-1, target)
        
        
    def binary_search(self, matrix, l, h, target):
        while l <= h:
            mid = l + (h-l)//2
            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                l = mid+1
            else:
                h = mid-1
        return False