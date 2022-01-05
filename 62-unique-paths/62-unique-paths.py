class Solution:
    def fact(self, start, end = 1):
        ans = 1
        for num in range(start, end-1, -1):
            ans *= num
        return ans
    
    def comb(self, n, r):
        numerator = self.fact(n, n-r+1)
        denominator = self.fact(r)
        return numerator // denominator
    
    def uniquePaths(self, m: int, n: int) -> int:
        steps_down = m-1
        steps_right = n-1
        total_steps = steps_down + steps_right
        
        if steps_down < steps_right:
            return self.comb(total_steps, steps_down)
        else:
            return self.comb(total_steps, steps_right)