class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = 0
        if n == 0: return 0
        temp = set(nums)
        
        for num in nums:
            count = 0
            if not num-1 in temp:
                x = num
                while x in temp:
                    count += 1
                    x += 1
                max_count = max(max_count, count)
        
        return max_count