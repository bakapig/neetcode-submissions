# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = []
        current = head
        ans = ListNode()
        while current is not None:
            res.append(current.val)
            current = current.next

        res.reverse()
        print(res)

        dummy = ListNode(0)
        tail = dummy

        for num in res:
            tail.next = ListNode(num)
            tail = tail.next
    
        return dummy.next




       
     


        return ans
