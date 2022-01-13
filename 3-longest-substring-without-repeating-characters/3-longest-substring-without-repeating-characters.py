class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        temp = dict()
        i = j = 0
        
        while j < n:
            if s[j] not in temp:
                temp[s[j]] = 1
                j += 1
                max_len = max(max_len, len(temp))
            else:
                while i < j and s[j] in temp:
                    del temp[s[i]]
                    i += 1
        return max_len
                