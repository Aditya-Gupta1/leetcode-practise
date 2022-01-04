class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        count = 0
        ans = 0
        
        for num in arr:
            if count == 0:
                ans = num
            if num == ans:
                count += 1
            else:
                count -= 1
        
        return ans