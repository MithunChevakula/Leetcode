class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        for ope in operations:
            if ope == '+':
                record.append(record[-1]+record[-2])
            elif ope == 'D':
                record.append(2*record[-1])
            elif ope == 'C':
                record.pop(-1)
            else:
                record.append(int(ope))
        return sum(record)