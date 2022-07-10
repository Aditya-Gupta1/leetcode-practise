class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = []
        maxDiff = -1
        for element1, element2 in zip(nums1, nums2):
            diff.append(abs(element1-element2))
            maxDiff = max(maxDiff, diff[-1])
        
        bucket = [0 for _ in range(maxDiff+1)]
        for value in diff:
            bucket[value] += 1
        
        totalMoves = k1+k2
        for i in range(maxDiff, 0, -1):
            if bucket[i] > 0:
                moves = min(bucket[i], totalMoves)
                bucket[i] -= moves
                bucket[i-1] += moves
                totalMoves -= moves
        
        ans = 0
        for idx, value in enumerate(bucket):
            ans += value*idx*idx
        
        return ans