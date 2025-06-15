class NumArray:

    def __init__(self, nums: List[int]):

        self.ln = len(nums)
        self.tree = [0] * (2 * self.ln)
        
        for i in range(self.ln):
            self.tree[self.ln + i] = nums[i]
        
        for i in range(self.ln - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) | 1]


        

    def sumRange(self, left: int, right: int) -> int:

        res = 0

        left += self.ln

        right += self.ln

        while left <=right:

            if left&1:

                res += self.tree[left]

                left+=1

            if not(right&1):

                res += self.tree[right]

                right-=1

            left >>=1

            right >>=1

            

        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)