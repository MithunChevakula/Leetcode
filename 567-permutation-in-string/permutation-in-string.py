class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1=Counter(s1)
        for i in range(len(s2)):
            sub=s2[i:i+len(s1)]
            map2=Counter(sub)
            if map1==map2:
                return True
        return False
        