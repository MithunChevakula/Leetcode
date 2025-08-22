class Solution:
    def nextGreaterElement(self,nums1, nums2):
        # ans=[]
        # for num in nums1:
        #     index=nums2.index(num)
        #     next_greater=-1
        #     for i in range(index+1,len(nums2)):
        #         if nums2[i]>num:
        #             next_greater=nums2[i]
        #             break
        #     ans.append(next_greater)
        # return ans

        # next_greater={}
        # for i in range(len(nums2)):
        #     one=nums2[i]
        #     for j in range(i+1,len(nums2)):
        #         two=nums2[j]
        #         if two>one:
        #             next_greater[one]=two
        #             break
        #     else:
        #         next_greater[one]=-1
        
        # ans=[]
        # for num in nums1:
        #     ans.append(next_greater[num])
        # return ans
        
        next_greater={}
        stack=[]
        for num in reversed(nums2):
            while stack and stack[-1]<=num:
                stack.pop()
            if stack :
                next_greater[num]=stack[-1]
            else:
                next_greater[num]=-1
            stack.append(num)
        return [next_greater[num] for num in nums1]