# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        lst = []
        dummy = ListNode(0)
        tail = dummy

        while head is not None:
            lst.append(head.val)
            head = head.next

        lst.reverse()
        print(lst)

        for num in lst:
            tail.next = ListNode(num)
            tail = tail.next

        return dummy.next
            


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = []
        # current = head
        # ans = ListNode()
        # while current is not None:
        #     res.append(current.val)
        #     current = current.next

        # res.reverse()
        # print(res)

        # dummy = ListNode(0)
        # tail = dummy

        # for num in res:
        #     tail.next = ListNode(num)
        #     tail = tail.next
    
        # return dummy.next




       
     


        return ans
