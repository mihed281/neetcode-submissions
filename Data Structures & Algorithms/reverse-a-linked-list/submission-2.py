# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=None
        m=head
        if m and m.next!=None:
            nxt=m.next
            while nxt!=None:
                nxt=m.next
                m.next=p
                p=m
                m=nxt 
            return(p)
        else:
            return m

            

        