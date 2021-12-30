class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1: return intervals
        
        intervals.sort(key = lambda x: x[0])
        ans = []
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        
        for i in range(1, n):
            
            if curr_end < intervals[i][0]:
                ans.append([curr_start, curr_end])
                curr_start = intervals[i][0]
                curr_end = intervals[i][1]
            elif curr_end >= intervals[i][0] and curr_end <= intervals[i][1]:
                curr_end = intervals[i][1]
        
        if curr_start != -1:
            ans.append([curr_start, curr_end])
        
        return ans