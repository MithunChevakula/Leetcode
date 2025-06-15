class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        string = ''
        while columnNumber > 0:
            col = columnNumber % (26)

            if col == 0 and columnNumber >= 26:
                col = 26
                columnNumber -= 26
                columnNumber //= 26
            else: 
                columnNumber //= 26
                
            string = chr(ord('A') - 1 + col) + string

        return string

