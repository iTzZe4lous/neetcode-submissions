# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast=head, head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        two=slow.next
        prev=slow.next=None
        while two:
            temp=two.next
            two.next=prev
            prev=two
            two=temp
        one, two=head, prev
        while two:
            tmp1, tmp2=one.next, two.next
            one.next=two
            two.next=tmp1
            one=tmp1
            two=tmp2
