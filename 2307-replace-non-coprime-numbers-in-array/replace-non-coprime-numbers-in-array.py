from typing import List
from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = [1] # 1
        for val in nums: # 2
            while (g := gcd(stack[-1], val)) != 1: # 3
                val = stack.pop() * val // g
            stack.append(val) # 4
        return stack[1:] # 5