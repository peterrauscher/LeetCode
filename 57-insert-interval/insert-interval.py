class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Start with a binary search to find sorted position in array
        # 
        if len(intervals) == 0: return [newInterval]
        newIntervals = []
        i = 0
        while i < len(intervals):
            if newInterval[0] > intervals[i][1]:
                newIntervals.append(intervals[i])
            elif newInterval[0] <= intervals[i][1]:
                if newInterval[1] < intervals[i][0]:
                    newIntervals.append(newInterval)
                    newIntervals += intervals[i:]
                    return newIntervals
                thisNewInterval = [min(intervals[i][0], newInterval[0])]
                while i < len(intervals) and newInterval[1] >= intervals[i][0]:
                    i += 1
                thisNewInterval.append(max(newInterval[1], intervals[i-1][1]))
                newIntervals.append(thisNewInterval)
                newIntervals += intervals[i:]
                return newIntervals
            i += 1
        newIntervals.append(newInterval)
        return newIntervals