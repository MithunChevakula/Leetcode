from typing import List
from functools import lru_cache
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i>=len(questions):
                return 0
            points,brainpower=questions[i]
            return max(points+dfs(i+brainpower+1),dfs(i+1))
        return dfs(0)

        