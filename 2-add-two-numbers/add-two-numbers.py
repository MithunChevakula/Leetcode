# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []

        # collect digits from l1
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next

        # collect digits from l2 (your bug was here - you were appending into num1 again)
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next

        # reverse once, because input is in reverse order
        n1 = int("".join(num1[::-1])) if num1 else 0
        n2 = int("".join(num2[::-1])) if num2 else 0

        total = str(n1 + n2)

        dummy = ListNode(0)
        current = dummy

        # build result list in reverse order
        for digit in total[::-1]:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next   # (your code returned dummy, should return dummy.next)
