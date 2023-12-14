class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        for i, v in enumerate(temperatures):
            while s and v > temperatures[s[-1]]:
                index = s.pop()
                temperatures[index] = i - index
            s.append(i)
        while s:
            temperatures[s.pop()] = 0
        return temperatures