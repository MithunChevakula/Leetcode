class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged=[]
        intervals.sort(key=lambda x:x[0])
        left=intervals[0]
        for right in intervals[1:]:
            if left[1]>=right[0]:
                left[1]=max(left[1],right[1])
            else:
                merged.append(left)
                left=right
        merged.append(left)
        return merged

        