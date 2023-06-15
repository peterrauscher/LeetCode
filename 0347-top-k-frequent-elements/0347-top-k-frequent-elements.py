class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [
        n for n, o in reversed(sorted(Counter(nums).items(), key=lambda item: item[1]))
    ][:k]