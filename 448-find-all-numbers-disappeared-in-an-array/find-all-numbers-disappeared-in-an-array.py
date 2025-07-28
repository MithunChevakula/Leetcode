class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[0]*n
        for i in nums:
            l[i-1]=i
        res=[]
        for i in range(len(l)):
            if l[i]==0:
                res.append(i+1)
        return res




    