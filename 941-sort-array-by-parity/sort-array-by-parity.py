class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        eve=[]
        odd=[]
        for i in range(n):
            if nums[i]%2==0:
                eve.append(nums[i])
            else:
                odd.append(nums[i])
        return eve+odd