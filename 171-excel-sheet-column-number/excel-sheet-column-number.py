class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans=0
        n=len(columnTitle)
        for x in columnTitle:
            ans=ans+(ord(x)-ord("A")+1)*26**(n-1)
            n-=1
        return ans
        # # 26*26^1+25*26^0=701
        # # AAA
        # return 1*26**3+1*26**2+1*26**1+1*26**0
         