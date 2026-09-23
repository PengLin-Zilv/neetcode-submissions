# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # lets say we have a linked list called head
        # reverse the list
        # return the new list

        # 1->2->3->None

        prev = None
        curr = head  # (1 -> 2 -> 3 -> None)
        # we want 3->2->1-> None
        while curr != None:
            # we want to save the next_node
            next_node = curr.next
            # curr = 1, next_node = 2

            # we also want to link head to the None(or prev)
            curr.next = prev
            # 1.next = None

            # here we also want to update the prev and curr here
            # 1-> None
            # 2 -> 3 -> None

            prev = curr
            # now update prev to curr, which is 1
        
            curr = next_node
            # curr = 2, start the loop again, next node= 3, 2.next = 1...

        return prev


