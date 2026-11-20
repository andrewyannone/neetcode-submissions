# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lower_start = ListNode(0)
        bigger_start = ListNode(0)
        lower = lower_start
        bigger = bigger_start
        temp = head

        while temp is not None:
            if temp.val < x:
                lower.next = temp
                lower = lower.next
                temp = temp.next
            else:
                bigger.next = temp
                bigger = bigger.next
                temp = temp.next
        bigger.next = None
        
        lower.next = bigger_start.next
        return lower_start.next


        