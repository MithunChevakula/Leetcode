class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_double = s+s
        s_double = s_double[1:]
        s_double = s_double[:-1]
        
        if s in s_double:
            return True 
        else:
            return False