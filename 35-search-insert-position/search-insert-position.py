class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)

        # low=0
        # high=len(nums)-1
        # while low<=high:
        #     mid=(low+high)//2
        #     if nums[mid]==target:
        #         return mid
        #     elif nums[mid]<target:
        #         low=mid+1
        #     else:
        #         high=mid-1
        # return low
        