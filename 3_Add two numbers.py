# 2 . Add two numbers
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        output = ListNode()
        output1 = output
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0) 
            val2 = (l2.val if l2 else 0)
            
            sum = val1 + val2 + carry
            val = sum % 10
            carry = sum // 10
            output1.next = ListNode(val)
            output1 = output1.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return output.next