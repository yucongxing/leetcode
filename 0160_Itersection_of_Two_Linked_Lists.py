from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        p = headA
        q = headB
        
        lenA = 0
        lenB = 0

        while p:
            lenA += 1
            p = p.next
        while q:
            lenB += 1
            q = q.next

        if lenA > lenB:
            p = headA
            q = headB
        else:
            p = headB
            q = headA
        d = abs(lenA - lenB)
        while d > 0:
            p = p.next
            d -= 1
        
        ans = None
        while p:
            if p == q:
                ans = p
                break
            else:
                p = p.next
                q = q.next
        return ans

