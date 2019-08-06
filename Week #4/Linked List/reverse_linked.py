# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        if(head != None):
            newHead = ListNode(head.val)
            head = head.next
        
        temp = newHead
        while(head != None):
            temp = ListNode(head.val)
            temp.next = newHead
            newHead = temp
            head = head.next
        return newHead
