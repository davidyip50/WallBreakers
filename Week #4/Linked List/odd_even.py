# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
            return head
        if(head.next == None):
            return head
        oddHead = head
        evenHead = head.next
        head = head.next.next
        tempOdd = oddHead
        tempEven = evenHead
        i = 3
        while(head):
            if(i % 2 == 1):
                tempOdd.next = head
                tempOdd = tempOdd.next
            if(i % 2 == 0):
                tempEven.next = head
                tempEven = tempEven.next
            head = head.next
            i += 1
        tempEven.next = None
        
        tempOdd.next = evenHead
        head = oddHead
        
        return head
