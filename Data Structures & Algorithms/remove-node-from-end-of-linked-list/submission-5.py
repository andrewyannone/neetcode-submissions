# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previous = ListNode(0)
        previous.next = head
        fast = previous
        slow = previous
        for _ in range (n):
            fast = fast.next
        if fast is None:
            return fast
        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next
        prev = slow
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        return previous.next
      


        