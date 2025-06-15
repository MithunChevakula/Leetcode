class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            ans[i] = sum([int(b) for b in bin(i)[2:]])
        return ans