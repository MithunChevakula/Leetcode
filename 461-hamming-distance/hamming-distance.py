class Solution: #approach 2
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0 # distance set to zero
        xor = x ^ y # x and y xored and assign to xor
        while xor: # while xor is not zero
            xor = xor & (xor - 1) # xor is anded with (xor - 1)
            dist += 1 # incrementing distance
        return dist # return dist as output