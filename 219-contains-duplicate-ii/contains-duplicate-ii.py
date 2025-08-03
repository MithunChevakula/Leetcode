class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = {}
        for i,num in enumerate(nums):
            if num in hset:
                if abs(i - hset[num]) <= k:
                    return True
            hset[num] = i
        return False