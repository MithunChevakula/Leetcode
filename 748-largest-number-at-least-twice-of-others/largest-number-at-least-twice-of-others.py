class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        h = nums.index(max(nums))
    
        for i in range(len(nums)):
            if nums[i]*2>nums[h] and i!=h:
                return -1

        return h 
        