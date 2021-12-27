class Solution:
    def setZeroes(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(arr)
        cols = len(arr[0])
        for i in range(rows):
            for j in range(cols):
                if(arr[i][j] == 0):
                    self.util(arr, i, j, rows, cols)
        for i in range(rows):
            for j in range(cols):
                if(arr[i][j] == '-1'):
                    arr[i][j] = 0
        
    def util(self, arr, i, j, rows, cols):
        for jj in range(cols):
            if(arr[i][jj] != 0 and arr[i][jj] != '-1'):
                arr[i][jj] = '-1'
        for ii in range(rows):
            if(arr[ii][j] != 0 and arr[ii][j] != '-1'):
                arr[ii][j] = '-1'        