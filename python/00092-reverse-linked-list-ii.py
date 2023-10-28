class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node and set its next pointer to the head
        dummy = ListNode(0, head)

        # Phase 1: Reach the left position
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Phase 2: Reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # Phase 3: Update pointers
        leftPrev.next.next = cur  # cur is the node after "right"
        leftPrev.next = prev  # prev is "right"

        return dummy.next
