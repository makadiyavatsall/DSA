class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Optimize k
        k = k % length
        if k == 0:
            return head

        # Step 3: Make it circular
        tail.next = head

        # Step 4: Find new tail: (length - k - 1) steps from head
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # Step 5: Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
