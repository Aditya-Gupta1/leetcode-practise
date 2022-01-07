class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        if n <= 0: return []
        
        nums.sort()
        
        i = 0
        j = i+1
        
        while i < n :
            j = i+1
            while j < n:
                curr_target = target - nums[i] - nums[j]
                left = j + 1
                right = n-1
                
                while left < right:
                    two_sum = nums[left] + nums[right]
                    
                    if two_sum < curr_target: left += 1
                    elif two_sum > curr_target: right -= 1
                    else:
                        quad = [nums[i], nums[j], nums[left], nums[right]]
                        ans.append(quad)
                    
                        while left < right and nums[left] == quad[2]: left += 1
                        while right > left and nums[right] == quad[3]: right -= 1
                
                while j+1 < n and nums[j+1] == nums[j]: j += 1
                j += 1
            while i+1 < n and nums[i+1] == nums[i]: i += 1
            i += 1
        
        return ans