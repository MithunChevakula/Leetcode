class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalsum=nums[0]
        currsum=0
        for i in nums:
            currsum+=i
            globalsum=max(globalsum,currsum)
            if currsum<0:
                currsum=0
        return globalsum