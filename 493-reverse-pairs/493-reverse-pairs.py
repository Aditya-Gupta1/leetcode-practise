class Solution:
    
    def merge(self, arr, l, mid, r):
        count = 0
        j = mid+1
        for i in range(l, mid+1):
            while j <= r and arr[i] > 2 * arr[j]:
                j += 1
            count += (j - (mid+1))
        
        temp = []
        left = l
        right = mid + 1
        while left <= mid and right <= r:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        
        while left <= mid:
            temp.append(arr[left])
            left += 1
        
        while right <= r:
            temp.append(arr[right])
            right += 1
        
        for i in range(l, r+1):
            arr[i] = temp[i-l]
        
        return count
    
    def mergeSort(self, arr, l, r):
        ans = 0
        if l < r:
            mid = (l+r)//2
            count_left = self.mergeSort(arr, l, mid)
            count_right = self.mergeSort(arr, mid+1, r)
            count = self.merge(arr, l, mid, r)
            ans = count + count_left + count_right
        return ans
    
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums)-1)