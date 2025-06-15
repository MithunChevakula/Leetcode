class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Start run at 1 since edge counts as 0
        run = 1
        # Count of total possible flowers
        count = 0
        for flower in flowerbed:
          # If empty add 1 to run
          if flower == 0:
            run += 1
          # Otherwise, reset run and compute additional number flowers
          else:
            count += (run - 1) // 2
            run = 0
        
        # Add last run (taking into account edge counts as 0)
        count += run//2
        
        return count >= n