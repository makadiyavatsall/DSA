from typing import Optional

# Definition for singly-linked list (provided by LeetCode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into a single sorted linked list.
        """
        # Create a dummy node to act as the head of the new list
        dummy = ListNode()
        # 'current' will be our pointer to build the new list
        current = dummy

        # Traverse both lists until one of them is empty
        while list1 and list2:
            if list1.val <= list2.val:
                # Append the smaller node from list1
                current.next = list1
                # Move the list1 pointer forward
                list1 = list1.next
            else:
                # Append the smaller node from list2
                current.next = list2
                # Move the list2 pointer forward
                list2 = list2.next
            
            # Move the 'current' pointer to the last node in the merged list
            current = current.next

        # At this point, one of the lists is exhausted.
        # Append the remaining nodes from the non-empty list.
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # The merged list starts after the dummy node
        return dummy.next