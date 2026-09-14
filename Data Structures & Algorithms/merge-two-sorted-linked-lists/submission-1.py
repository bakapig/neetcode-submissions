# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        current_one =  list1
        current_two = list2

        dummy = ListNode(0)
        tail = dummy

        while current_one is not None and current_two is not None:
            if current_one.val < current_two.val:
                tail.next = current_one
                current_one = current_one.next
                tail = tail.next
            else:
                tail.next = current_two
                current_two = current_two.next
                tail = tail.next

        if current_one is None:
            tail.next = current_two
        else:
            tail.next = current_one

        return dummy.next
























        current_one = list1
        current_two = list2
        dummy = ListNode(0)
        tail = dummy

        while current_one is not None and current_two is not None:

            if current_one.val < current_two.val:
                tail.next = current_one
                current_one = current_one.next
            else:
                tail.next = current_two 
                current_two = current_two.next

            tail = tail.next

        if current_one is not None:
            tail.next = current_one
        else:
            tail.next = current_two

        return dummy.next

    





        