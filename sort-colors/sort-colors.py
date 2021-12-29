class Solution:
    def swap(self, arr, firstIndex, secondIndex):
        arr[firstIndex], arr[secondIndex] = arr[secondIndex], arr[firstIndex]
        
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = mid = 0
        high = len(nums)-1
        
        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums, mid, low)
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                self.swap(nums, mid, high)
                high -= 1
        