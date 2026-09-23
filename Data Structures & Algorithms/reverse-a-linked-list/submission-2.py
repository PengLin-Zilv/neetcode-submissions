# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initially, the head = 1 -> 2 -> 3 -> None
        # we want to reverse, and get
        # 3 -> 2 -> 1 -> None
        # we need 1-> None
        # and then 2-> 1-> None
        # and then 3-> 2-> 1 -> None
        # first step, to make 1-> None

        # initial set up
        prev = None
        curr = head
        # now here prev = None
        # curr = 1



        while curr != None:
            next_node = curr.next
            # next node = 2
            curr.next = prev
            # 1.next = None
            # 1-> None

            prev = curr
            # prev now  = 1
            curr = next_node
            # curr now = 2

        return prev



