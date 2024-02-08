class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        maxAltitude = 0
        for change in gain:
            altitude += change
            maxAltitude = max(altitude, maxAltitude)
        return maxAltitude
