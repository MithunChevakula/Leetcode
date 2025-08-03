class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n=Counter(nums)
        # return [num for num, freq in n.most_common(k)]

        freq=[]
        li=list(set(nums))
        for num in li:
            freq.append((num,nums.count(num)))
        freq.sort(key=lambda x:x[1],reverse=True)
        return [freq[i][0] for i in range(k)]



        