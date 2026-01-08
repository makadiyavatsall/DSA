
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev, cur = None, slow.next
        slow.next = None  # Split the list into two halves
        while cur:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
        
        # Step 3: Merge the two halves alternately
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
