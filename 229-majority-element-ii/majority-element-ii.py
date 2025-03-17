class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        res=[]
        freq = Counter(nums)
        for key, value in freq.items():
            if value > n:
                res.append(key)
        return res