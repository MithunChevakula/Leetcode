class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        out = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                    out[i][j]=matrix[j][i]
        return out
        