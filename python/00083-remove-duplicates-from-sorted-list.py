class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head

    while current:
        if current.next and current.next.val == current.val:
            current.next = current.next.next
        else:
            current = current.next

    return head
