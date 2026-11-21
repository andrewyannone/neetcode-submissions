# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        placeholder = ListNode(0)
        placeholder.next = head
        node_a = head
        node_b = head.next
        before = placeholder
        while node_b is not None:
            before.next = node_b
            node_a.next = node_b.next
            node_b.next = node_a
            before = node_a
            node_a = before.next
            if node_a is not None:
                node_b = node_a.next
            else:
                node_b = None

        return placeholder.next

