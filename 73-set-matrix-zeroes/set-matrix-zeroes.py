class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)  # number of rows
        n = len(matrix[0])  # number of columns
        rows,cols = set(),set() # set to store columns that contain zero
        
        # First pass to find columns that need to be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for r in rows:
            for i in range(n):
                matrix[r][i]=0
        for c in cols:
            for j in range(m):
                matrix[j][c]=0
