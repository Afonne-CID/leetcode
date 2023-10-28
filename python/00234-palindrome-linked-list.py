def isPalindrome(self, head: ListNode) -> bool:
    fast = head
    slow = head

    # Find the middle (slow)
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse the second half
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    # Check if it's a palindrome
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
