class Solution:
    def digitCount(self, num: str) -> bool:
        freq = dict()
        for i in num:
            freq[int(i)] = freq.get(int(i), 0)+1
        ans = True
        for i in range(len(num)):
            if freq.get(i, 0) != int(num[i]):
                return False
        return True