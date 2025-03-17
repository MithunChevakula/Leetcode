class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        a=n//2
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 
        for key, value in freq.items():
            if value > a:
                return key
            
        
        