# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # head = [1,2,3,4]
        # n = 2 -> remove nth node from its end
        # return head, head = [1,2,4]

        # head = [2,4,1,45,1,41,1]
        # n = 4
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        x = 0
        while x < n:
            fast = fast.next
            x += 1

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next



