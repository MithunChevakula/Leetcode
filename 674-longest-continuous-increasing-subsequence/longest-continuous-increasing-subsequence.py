class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        ma = 0
        temp = 0
        
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                temp += 1
                ma = max(ma, temp)
            else:
                temp = 0

        return ma+1