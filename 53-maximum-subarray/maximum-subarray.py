class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalsum=nums[0]
        currentsum=0
        for i in nums:
            currentsum+=i
            globalsum=max(globalsum,currentsum)
            if currentsum<0:
                currentsum=0
        return globalsum