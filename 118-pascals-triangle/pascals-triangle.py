class Solution:
    def generateRows(self, numRows):
        result = 1
        answer = []
        answer.append(1)
        for i in range(1, numRows):
            result = result * (numRows - i)
            result = result // i
            answer.append(result)
        return answer
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1,numRows + 1):
            result.append(self.generateRows(i))
        return result