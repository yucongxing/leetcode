from typing import List


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def printlist(head: ListNode):
    p = head
    while p:
        print(p.val, end=' ')
        p = p.next
    print()


def createlist(l: List) -> ListNode:
    head = ListNode(l[0])
    p = head
    for i in range(1,len(l)):
        t = ListNode(l[i])
        p.next = t
        p = p.next
    return head


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1, head)
        p = dummy
        for _ in range(left - 1):
            p = p.next
        pre = p
        pleft = p.next
        for _ in range(right - left + 1):
            p = p.next
        pright = p
        next = p.next
        pre.next = None
        pright.next = None
        old = None
        new = pleft
        while(new):
            t = new.next
            new.next = old
            old = new
            new = t
        pre.next = pright
        pleft.next = next

        return dummy.next

if __name__ == '__main__':
    s = Solution()
    head = createlist([1,2,3,4,5])
    printlist(head)
    s.reverseBetween(head,2,4)
    printlist(head)
    head = createlist([1])
    printlist(head)
    s.reverseBetween(head,1,1)
    printlist(head)
