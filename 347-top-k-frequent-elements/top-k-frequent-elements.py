class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=Counter(nums)
        return [num for num, freq in n.most_common(k)]


        