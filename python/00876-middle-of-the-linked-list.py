def middleNode(head):
    if not head or not head.next:
        return head

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
