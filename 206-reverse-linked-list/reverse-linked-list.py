class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev=None
        while temp:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        return prev
