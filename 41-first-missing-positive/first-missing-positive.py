class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # i=1
        # while True:
        #     if i not in nums:
        #         return i
        #     i+=1
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i in range(1,n+1):
            if i!=nums[i-1]:
                return i
        return n+1
        