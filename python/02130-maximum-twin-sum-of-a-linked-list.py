class Solution:
    def pairSum(self, head):
        slow, fast = head, head
        prev = None

        # Find the middle of the linked list and reverse the first half
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        res = 0

        # Calculate the maximum twin sum
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return res
