def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode:
    # Create dummy nodes for left and right partitions
    less_head, bigger_head = ListNode(-1), ListNode(-1)
    less_prev, bigger_prev = less_head, bigger_head

    while head:
        if head.val < x:
            # Add the current node to the left partition
            less_prev.next = head
            less_prev = less_prev.next
        else:
            # Add the current node to the right partition
            bigger_prev.next = head
            bigger_prev = bigger_prev.next

        head = head.next

    # Terminate both partitions
    less_prev.next = bigger_prev.next = None

    # Connect the left partition to the beginning of the right partition
    less_prev.next = bigger_head.next

    # Return the resulting partitioned list
    return less_head.next
