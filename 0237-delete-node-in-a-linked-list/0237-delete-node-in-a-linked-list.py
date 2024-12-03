# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        '''
        #If head is provided , follow the below code
        
        if head==None or (head.next is None and head.val == node.val):
            return None
        
            
        temp=head
        while temp.next != None:
            if (temp.next.val==node.val):
                temp.next=temp.next.next
                
            temp=temp.next
         '''   
        
        node.val = node.next.val
        
        node.next = node.next.next
        
        
        
        
        
        
        
        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        