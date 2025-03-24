# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLL(self, list1, list2):
        dummy= ListNode(-1)
        temp=dummy
        while(list1 and list2):
            if(list1.val < list2.val):
                temp.next=list1
                temp=list1
                list1=list1.next
            else:
                temp.next=list2
                temp=list2
                list2=list2.next
        if(list1):
            temp.next=list1
        else:
            temp.next=list2
        
        return dummy.next
    
    def findMid(self, head):
        if not head or not head.next:
            return head
        
        slow=head
        fast=head.next # using Tortoise Hare but fast starts with head.next as we want the first middle - even length case

        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        mid = self.findMid(head)
        right = mid.next
        mid.next = None
        left = head

        left = self.sortList(left)
        right = self.sortList(right)

        return self.mergeTwoLL(left,right)

         
        
        