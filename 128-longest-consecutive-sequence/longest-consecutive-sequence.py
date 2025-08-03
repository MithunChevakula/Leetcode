class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # nums.sort()
        # curr=1
        # longest=1
        # for i in range(1,len(nums)):
        #     if nums[i]!=nums[i-1]:
        #         if nums[i]==nums[i-1]+1:
        #             curr+=1
        #         else:
        #             longest=max(curr,longest)
        #             curr=1
        # return max(curr,longest)

        nums_set = set(nums)
        longest_seq = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 0
                while num + length in nums_set:
                    length += 1
                longest_seq = max(longest_seq, length)
        return longest_seq