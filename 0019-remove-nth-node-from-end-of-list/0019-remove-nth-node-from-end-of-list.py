# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None

        temp=head

        size=1

        while temp.next:
            temp=temp.next
            size+=1
        
        if size<n:
            return None
        
        if size==n:
            return head.next

        rem=size-n+1

        t=head
        counter=1
        while t.next:
            counter+=1
            if counter==rem:
                break
            t=t.next
        
        t.next = t.next.next

        return head

        


        