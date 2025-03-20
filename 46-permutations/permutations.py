from itertools import permutations
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=list(permutations(nums))
        return l
        