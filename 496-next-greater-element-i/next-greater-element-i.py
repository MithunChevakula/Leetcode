class Solution:
    def nextGreaterElement(self,nums1, nums2):
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)
        return [next_greater.get(x, -1) for x in nums1]