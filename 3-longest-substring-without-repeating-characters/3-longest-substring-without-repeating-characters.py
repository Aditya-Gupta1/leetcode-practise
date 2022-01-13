class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            temp = {s[i]:1}
            for j in range(i+1, n):
                if s[j] not in temp:
                    temp[s[j]] = 1
                else:
                    break
            max_len = max(max_len, len(temp))
        
        return max_len