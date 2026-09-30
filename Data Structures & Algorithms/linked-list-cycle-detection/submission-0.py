# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett = set()
        curr = head

        while curr in sett:
            index = ListNode(head)
        curr = curr.next
        sett.add(curr)

        if curr.next == None:
            return False
        return True
        