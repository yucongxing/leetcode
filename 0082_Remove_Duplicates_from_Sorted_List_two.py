from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                curval = cur.next.val
                while cur.next and cur.next.val == curval:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
