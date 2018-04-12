# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2:
            current_val = carry
            if l1:
                current_val += l1.val
                l1 = l1.next
            if l2:
                current_val += l2.val
                l2 = l2.next
            if current_val >= 10:
                carry = 1
                current_val -= 10
            else:
                carry = 0
            current.next = ListNode(current_val)
            current = current.next
        if carry:
            current.next = ListNode(carry)
        return dummy.next
        
