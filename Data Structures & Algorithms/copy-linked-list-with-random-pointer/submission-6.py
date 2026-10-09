"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        p1=head
        while p1 is not None:
            p2=Node(p1.val)
            p2.next=p1.next
            p1.next=p2
            p1=p2.next
        resHead=head.next

        p1=head
        while p1 is not None:
            if p1.random is not None:
                p1.next.random=p1.random.next
            p1=p1.next.next
        p1=head
        while p1 is not None:
            p2=p1.next
            p1.next=p2.next
            if p2.next is not None:
                p2.next = p2.next.next
            p1=p1.next
        return resHead

        