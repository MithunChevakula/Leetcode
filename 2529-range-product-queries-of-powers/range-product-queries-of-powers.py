class Solution(object):
    MOD = 1000000007

    def productQueries(self, n, queries):
        powers = []
        answers = [0] * len(queries)
        i = 1
        product = 1

        # Find largest power of 2 greater than n
        while i <= n:
            i *= 2

        # Extract powers of 2 from n
        while n > 0:
            if n >= i:
                n -= i
                powers.append(i)
            i //= 2

        powers.sort()

        for idx in range(len(queries)):
            product = 1
            l, r = queries[idx]
            while l <= r:
                product = (product * powers[l]) % self.MOD
                l += 1
            answers[idx] = product

        return answers