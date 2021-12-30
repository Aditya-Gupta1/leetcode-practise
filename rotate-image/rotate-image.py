class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        self.mirrorDiagonally(matrix, n)
        self.mirrorVertically(matrix, n)
    
    def mirrorDiagonally(self, arr, n):
        for i in range(n):
            for j in range(i):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    
    def mirrorVertically(self, arr, n):
        for i in range(n):
            for j in range(n//2):
                arr[i][j], arr[i][n-j-1] = arr[i][n-j-1], arr[i][j]
                
    def swap(self, arr, first, second):
        arr[first], arr[second] = arr[second], arr[first]