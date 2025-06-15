class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.scores = nums

    def add(self, val: int) -> int:
        self.scores.append(val)
        self.scores.sort()
        return self.scores[-self.k]