class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # slow = fast = head
        # stack = []

        # while fast and fast.next:
        #     stack.append(slow.val)
        #     slow = slow.next
        #     fast = fast.next.next

        # if fast:
        #     slow = slow.next

        # while slow:
        #     if stack.pop() != slow.val:
        #         return False
        #     slow = slow.next

        # return True

        # temp=head
        # arr=[]
        # while temp:
        #     arr.append(temp.val)
        #     temp=temp.next
        # return arr==arr[::-1]

        temp=head
        stack=[]
        while temp:
             stack.append(temp.val)
             temp=temp.next

        temp=head
        while temp:
            if temp.val!=stack.pop():
                return False
            temp=temp.next
        return True