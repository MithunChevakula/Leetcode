from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m=Counter(s)
        return next((i for i,v in enumerate(s) if m[v]==1),-1)