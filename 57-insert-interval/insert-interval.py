class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Start with a binary search to find sorted position in array
        # 
        left, right = [], []
        for interval in intervals:
            if newInterval[0] > interval[1]:
                left.append(interval)
            elif newInterval[1] < interval[0]:
                right.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        return left + [newInterval] + right