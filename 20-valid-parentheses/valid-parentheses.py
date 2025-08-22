class Solution:
    def isValid(self, s: str) -> bool:
        # pairs=["()","[]","{}"]
        # while True:
        #     found_pair=False
        #     for pair in pairs:
        #         if pair in s:
        #             s=s.replace(pair,"")
        #             found_pair=True
        #     if not found_pair:
        #         break
        # return len(s)==0
        
        

        stack=[]
        brackets={"}":"{",")":"(","]":"["}
        for char in s:
            if char in brackets:
                if stack and stack[-1]==brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack)==0

