def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    length = 1
    tail = head

    while tail.next:
        tail = tail.next
        length += 1

    k %= length

    if k == 0:
        return head

    tail.next = head
    for _ in range(length - k):
        tail = tail.next

    new_head = tail.next
    tail.next = None

    return new_head
