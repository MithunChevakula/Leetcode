class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        rotated_arr=[0]*n
        for i in range(n):
            rotated_arr[(i+k)%n]=nums[i]
        nums[:]=rotated_arr[:]
    