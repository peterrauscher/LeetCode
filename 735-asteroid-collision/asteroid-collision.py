class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remaining = []
        for asteroid in asteroids:
            if not remaining:
                remaining.append(asteroid)
            elif (asteroid // abs(asteroid) == remaining[-1] // abs(remaining[-1])) or asteroid > 0:
                remaining.append(asteroid)
            else:
                while remaining and remaining[-1] > 0 and abs(asteroid) > abs(remaining[-1]):
                    remaining.pop()
                if (not remaining) or (remaining[-1] < 0):
                    remaining.append(asteroid)
                elif abs(asteroid) > abs(remaining[-1]):
                    remaining.append(asteroid)
                elif abs(asteroid) == abs(remaining[-1]):
                    remaining.pop()
        return remaining