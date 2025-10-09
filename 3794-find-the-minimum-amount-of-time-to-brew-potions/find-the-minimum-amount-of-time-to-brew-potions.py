from numpy import array, append
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        res = sum(skill) * mana[-1]
        acc = array(list(accumulate(skill)))
        offset = append(0, acc[:-1])
        for m1, m2 in pairwise(mana):
            res += int((acc * m1 - offset * m2).max())

        return res