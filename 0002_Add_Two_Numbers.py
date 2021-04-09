from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        p1, p2 = l1, l2
        ans = ListNode(-1, None)
        p3 = ans
        flag = False
        while p1 and p2:
            newval = p1.val + p2.val + (1 if flag else 0)
            if newval >= 10:
                flag = True
                newval -= 10
            else:
                flag = False
            newnode = ListNode(newval, None)
            p3.next = newnode
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        while p1:
            val = p1.val + (1 if flag else 0)
            if val >= 10:
                flag = True
                val -= 10
            else:
                flag = False
            p3.next = ListNode(val, None)
            p3 = p3.next
            p1 = p1.next
        while p2:
            val = p2.val + (1 if flag else 0)
            if val >= 10:
                flag = True
                val -= 10
            else:
                flag = False
            p3.next = ListNode(val, None)
            p3 = p3.next
            p2 = p2.next
        if flag:
            p3.next = ListNode(1, None)
        return ans.next
                
