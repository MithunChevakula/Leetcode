class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        answer = 1 
        result.append(answer)
        for i in range(1, rowIndex + 1):
            answer = answer * (rowIndex - i + 1)
            answer = answer // i
            result.append(answer)
        return result