from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
        times_to_reach_target = deque()
        for car in cars:
            travel_time = (target - car[0]) / car[1]
            if not times_to_reach_target or travel_time > times_to_reach_target[-1]:
                times_to_reach_target.append(travel_time)
        return len(times_to_reach_target)