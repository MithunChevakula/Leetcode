class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        
        a=re.sub(r'[^a-zA-Z0-9]','',s.lower())
       
        if a[::-1]==a:
            return True
        else:
            return False
        