class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        majority=None
        for num in nums:
            if c==0:
                majority=num
                c=1
            elif majority==num:
                c+=1
            else:
                c-=1
        return majority

            
        
        