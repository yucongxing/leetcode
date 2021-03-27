class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1, head)
        length = 0
        p = dummy
        while p.next:
            p = p.next
            length += 1
        k %= length
        if k == 0 or not head:
            return head
        curlast = curhead = dummy
        cnt = 0
        while curlast.next and cnt < k:
            curlast = curlast.next
            cnt += 1
        while curlast.next:
            curlast = curlast.next
            curhead = curhead.next
        newhead = curhead.next
        curhead.next = None
        curlast.next = head
        dummy.next = newhead
        return dummy.next

