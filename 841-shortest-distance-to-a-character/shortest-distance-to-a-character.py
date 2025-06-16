class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        sol = []
        for i in range(len(s)):

            if s[i] == c:
                sol.append(0)
            else:
                cou = float('inf')
                j = i
                # if i != 0:
                while s[j] != c and j >= 0:
                    j -= 1
                if s[j] == c:
                    cou = min(cou, i-j)
                if j == -1:
                    cou = float('inf')
                j = i
                # if i != len(s):
                while s[j] != c and j < len(s)-1:
                    j += 1
                if s[j] == c:
                    cou = min(cou, j-i)
                sol.append(cou)

        return sol
        

        #   lst = []
        # for i in range(len(s)):
        #     if s[i] == c:
        #         lst.append(i)
        
        # sol = []
        # for j in range(len(s)):
        #     if s[i] == c:
        #         sol.append(0)
        #     else:
        #         cou = float('inf')
                
        #         l = []
        #         for i in lst:
        #             l.append(abs(i-j))
        #         print(l)