class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    new_head = reverseList(head.next)
    head.next.next = head
    head.next = None

    return new_head
