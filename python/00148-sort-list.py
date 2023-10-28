class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base cases
        if not head or not head.next:
            return head

        # Split the linked list into two halves
        mid = self.get_mid(head)
        left, right = self.sortList(head), self.sortList(mid)

        # Merge the two sorted halves
        return self.merge_two_sorted(left, right)

    def merge_two_sorted(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2

        if not list2:
            return list1

        sentinel = ListNode()
        prev = sentinel
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        if list1:
            prev.next = list1
        else:
            prev.next = list2

        return sentinel.next

    def get_mid(self, head: ListNode) -> ListNode:
        mid_prev = None
        while head and head.next:
            mid_prev = mid_prev.next if mid_prev else head
            head = head.next.next

        mid = mid_prev.next
        mid_prev.next = None

        return mid
