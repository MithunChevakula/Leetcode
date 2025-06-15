class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = str(bin(n)[2:])
        if "00" in binary or "11" in binary:
            return False
        return True    