# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy
        carry = 0

        # Continue if either list has node
        while l1 is not None or l2 is not None:  
            if l1 is not None:
                value1 = l1.val
                l1 = l1.next
            else:
                value1 = 0

            if l2 is not None:
                value2 = l2.val
                l2 = l2.next
            else:
                value2 = 0

            total = value1 + value2 + carry
            carry = total // 10
            digit = total % 10

            tail.next = ListNode(digit)
            tail = tail.next
            

        # Add the remaining carry after both lists finish
        if carry != 0:
            tail.next = ListNode(carry)
            
        return dummy.next

        
        