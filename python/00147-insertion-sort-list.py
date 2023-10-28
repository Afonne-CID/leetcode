class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head):
    if not head or not head.next:
        return head

    # Initialize a sentinel node to simplify edge cases
    sentinel = ListNode()
    curr = head

    while curr:
        prev = sentinel

        # Check if the current node is already in the correct position
        if prev.next and curr.val >= prev.next.val:
            prev = prev.next
        else:
            # Find the correct position to insert the current node
            while prev.next and curr.val >= prev.next.val:
                prev = prev.next

            # Insert the current node in the correct position
            curr.next, prev.next, curr = prev.next, curr, curr.next

    return sentinel.next
