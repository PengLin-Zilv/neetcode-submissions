# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. split, goal: find the middle

        mid = end = head
        while end and end.next:
            mid = mid.next
            end = end.next.next
        l2 = mid.next
        mid.next = None

        # 2. reverse, goal: reverse l2 because we want it to be back to front
        prev = None
        while l2:
            l2next = l2.next
            
            l2.next = prev
            prev = l2

            l2 = l2next

        # 3. merge, goal: pick the first, pick second, pick first, pick second
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            first = tmp1
            second.next = first
            second = tmp2






