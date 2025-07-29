class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        res = set()
        max_len = 0
        while i < len(s) and j < len(s):
            if s[j] not in res:
                res.add(s[j])
                max_len = max(max_len, j-i+1)
                j+=1
            else:
                res.remove(s[i])
                i += 1

        return max_len