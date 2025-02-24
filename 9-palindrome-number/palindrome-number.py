class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        num=x
        sign=1
        if(x<0):
            return False

        while x > 0:
            r = x % 10  
            rev = rev * 10 + r  
            x //= 10    
        if rev==num:
            return True
        else:
            return False
