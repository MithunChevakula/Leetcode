class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n=len(nums)
        bit_mapping = defaultdict(list)
        cur_bit_freq = defaultdict(int)
        j = n-1
        ans = [1]*n
        def try_removing_jth(cur_bit_freq, idx):
            for bit in bit_mapping[idx]:
                if cur_bit_freq[bit] <= 1:
                    return False
            
            for bit in bit_mapping[idx]:
                cur_bit_freq[bit] -= 1
            
            return True

        for i in range(n-1, -1, -1):
            cnt = 0
            while nums[i]:
                if nums[i] & 1:
                    bit_mapping[i].append(cnt)
                    cur_bit_freq[cnt] += 1
                cnt+=1
                nums[i] >>=1
            
            while j > i and try_removing_jth(cur_bit_freq, j):
                j-=1
            
            ans[i] = (j-i+1)
        
        return ans
            
        