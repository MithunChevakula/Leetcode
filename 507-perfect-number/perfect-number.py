class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 != 0:
            return False
        count = 1
        i = 2
        j = num//2
        while i < j:
            if num%i == 0:
                count += i
            if num%j == 0:
                count += j
            i += 1
            j -= 1
        return count == num
        