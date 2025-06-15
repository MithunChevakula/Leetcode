class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=''
        for i in s:
            temp=ord(i)
            if 65<=temp<=90:
                a=temp-65
                ans+=chr(a+97)
            else:
                ans+=i
        return ans