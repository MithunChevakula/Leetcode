class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax=nums[0]
        curmin=nums[0]
        prod=nums[0]
        for i in range(1,len(nums)):
            temp=max(nums[i],nums[i]*curmax,nums[i]*curmin)
            curmin=min(nums[i],nums[i]*curmax,nums[i]*curmin)
            curmax=temp
            prod=max(prod,curmax)
        return prod

