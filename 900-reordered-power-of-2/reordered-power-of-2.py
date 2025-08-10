class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        m = set()
        c = 1
        while c <= (10 ** 9):
            m.add(''.join(sorted(str(c))))
            c *= 2

        return ''.join(sorted(str(n))) in m 