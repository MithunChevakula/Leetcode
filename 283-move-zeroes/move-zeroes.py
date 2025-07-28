class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        n=len(nums)
        for  j in range(n):
            if nums[j]==0:
                continue
            else:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        return nums
        