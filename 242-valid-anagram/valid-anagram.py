from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s)==Counter(t)
        #return sorted(s)==sorted(t)
        ar1=[0]*26
        ar2=[0]*26
        for i in s.lower():
            ar1[ord(i)-97]+=1
        for i in t.lower():
            ar2[ord(i)-97]+=1
        return ar1==ar2


        