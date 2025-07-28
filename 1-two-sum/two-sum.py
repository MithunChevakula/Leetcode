class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,val in enumerate(nums):
            res=target-nums[i]
            if res in dict:
                return [i,dict[res]]
            dict[val]=i

            



