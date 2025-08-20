# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next

        k=k % length
        if k==0:
            return head
        
        for _ in range(k):
            temp=head
            while temp.next.next:
                temp=temp.next

            new_head=temp.next
            temp.next=None
            new_head.next=head
            head=new_head
        return head


        