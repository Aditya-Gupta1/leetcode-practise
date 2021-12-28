class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(arr)-1, 0, -1):
            if arr[i] > arr[i-1]:
                pivot = i-1
                break
        
        if(pivot >= 0):
            for j in range(len(arr)-1, pivot, -1):
                if arr[j] > arr[pivot]:                    
                    arr[j], arr[pivot] = arr[pivot], arr[j]
                    break        
        self.reverse(arr, pivot+1)        
            
    def reverse(self, arr, start):
        end = len(arr)-1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1