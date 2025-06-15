class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        res=sorted(set(nums),reverse=True)
        if len(res)>=3:
            return res[2]
        else:
            return res[0]