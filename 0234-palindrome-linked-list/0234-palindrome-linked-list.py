# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast=slow=head

        while fast.next and fast.next.next:  # compute the middle of the linkedlist

            slow=slow.next
            fast=fast.next.next

        newHead= self.rev(slow.next)
        first=head
        second=newHead

        while second:
            if first.val != second.val:
                self.rev(newHead)
                return False
            first=first.next
            second=second.next

        self.rev(newHead)
        return True



    def rev(self,head): # reversing the linkedlist

        if not head or not head.next:
            return head

        new_head=self.rev(head.next)

        front = head.next
        front.next = head

        head.next = None

        return new_head
         

        








        

        