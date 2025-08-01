from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:

        # for i in range(len(s)):
        #     if s.count(s[i])==1:
        #         return i
        # return -1
        st=Counter(s)

        for key,val in st.items():
            if val==1:
                return s.index(key)
        return -1