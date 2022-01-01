class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        low = 1
        high= n-1        
        
        while low <= high:
            curr = (low+high)//2
            count = sum(num <= curr for num in nums)
            if count > curr:
                duplicate = curr
                high = curr - 1
            else:
                low = curr + 1
        
        return duplicate