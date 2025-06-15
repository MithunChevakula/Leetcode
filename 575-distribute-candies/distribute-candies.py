class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        total_lenth = len(candyType) // 2
        unique = len(set(candyType))
        return min(total_lenth,unique) 
        