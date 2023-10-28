def removeElements(self, head: ListNode, val: int) -> ListNode:
    # Create a dummy node to handle edge cases
    dummy = ListNode(next=head)
    prev, curr = dummy, head

    while curr:
        nxt = curr.next

        if curr.val == val:
            # Remove the node by updating the previous pointer
            prev.next = nxt
        else:
            # If the current node's value doesn't match the target value, update the previous pointer
            prev = curr

        curr = nxt

    # Return the new head
    return dummy.next
