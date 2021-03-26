class ListNode:
    def __init__(self, val-0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next.val:
            if cur.val == cur.next:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

