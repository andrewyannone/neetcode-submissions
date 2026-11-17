# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_1 = None
        current_2 = None
        previous = None
        next_node = None
        if list1 is None and list2 is None:
            return None
        elif list1 == None:
            current_1 = list2
        elif list2 == None:
            current_1 = list1
        elif list1.val <= list2.val:
            current_1 = list1
            current_2 = list2
        else:
            current_1 = list2
            current_2 = list1
        
        head = current_1
        while current_1 and current_2 is not None:
            if current_1.val > current_2.val:
                next_node = current_2.next
                current_1 = current_2
                current_2.next = previous.next
                previous.next = current_2
                previous = current_1
                current_2 = next_node
            else:
                previous = current_1
                current_1 = current_1.next
        if current_1 == None:
            previous.next = current_2
        return head

                

            

            
            
       
            
           
        

        