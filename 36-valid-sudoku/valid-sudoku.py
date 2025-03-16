from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset_rows=defaultdict(set)
        hashset_cols=defaultdict(set)
        hashset_subboxes=defaultdict(set)
        for r in range(9):
            for c in range(9):
                if (board[r][c] != '.') and (board[r][c] in hashset_rows[r] or board[r][c] in hashset_cols[c] or board[r][c] in hashset_subboxes[(r//3,c//3)]):
                    return False
                hashset_rows[r].add(board[r][c])
                hashset_cols[c].add(board[r][c])
                hashset_subboxes[(r//3,c//3)].add(board[r][c])
        return True
