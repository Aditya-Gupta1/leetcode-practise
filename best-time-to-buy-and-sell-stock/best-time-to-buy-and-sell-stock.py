class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # optimised approach
        if len(prices) < 2:
            return 0
        ans = 0
        max_element = prices[-1]
        
        for i in range(len(prices)-2, -1, -1):
            ans = max(ans, max_element - prices[i])
            max_element = max(max_element, prices[i])
        
        return ans
        
        # brute-force - TLE
#         ans = float('-inf')
#         for i in range(len(prices)-1):
#             profit = float('-inf')
#             for j in range(i+1, len(prices)):
#                 profit = max(profit, prices[j] - prices[i])
#             ans = max(ans, profit)
        
#         return ans if ans > 0 else 0