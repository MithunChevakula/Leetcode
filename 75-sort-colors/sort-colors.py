class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes,ones,twoes=[],[],[]
        for i in range(len(nums)):
            if nums[i]==0:
                zeroes.append(nums[i])
            elif nums[i]==1:
                ones.append(nums[i])
            else:
                twoes.append(nums[i])
        nums[:]=zeroes+ones+twoes
        return nums
        