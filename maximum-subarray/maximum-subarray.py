class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        max_sum = nums[0]
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum = nums[i]+curr_sum
            max_sum = max(max_sum, curr_sum)
            curr_sum = max(0, curr_sum)
        
        return max_sum