# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        placeholder = ListNode(0)
        placeholder.next = head
        temp = placeholder
        prev = None
        next_node = None
        for _ in range (left-1):
            temp = temp.next
        reversal = temp.next
        for _ in range (right - left + 1):
            next_node = reversal.next
            reversal.next = prev
            prev = reversal
            reversal = next_node
        temp.next.next = reversal
        temp.next = prev
        return placeholder.next

        