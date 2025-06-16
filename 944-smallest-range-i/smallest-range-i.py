class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minv= min(nums)
        maxv= max(nums)
        return max(0,(maxv-minv-2*k))