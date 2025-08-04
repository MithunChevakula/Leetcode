class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            missing_count=arr[mid]-(mid+1)
            if missing_count<k:
                left=mid+1
            else:
                right=mid-1
        return left+k 
        