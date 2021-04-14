from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# method 1: recursive in-order travel
#class BSTIterator:
#    def __init__(self, root: Optional[TreeNode]):
#        self.NodeList = []
#        def inorder(root: Optional[TreeNode]):
#            if not root:
#                return
#            inorder(root.left)
#            self.NodeList.append(root.val)
#            inorder(root.right)
#        inorder(root)
#        self.start = -1
#    def next(self) -> int:
#        self.start += 1
#        return self.NodeList[self.start]
#    def hasNext(self) -> bool:
#        return self.start >= len(self.NodeList)-1


# method 2:non-recursive inorder travel
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stk = list()
        self.p = root

    def next(self) -> int:
        while self.p:
            self.stk.append(self.p)
            self.p = self.p.left
        self.p = self.stk.pop()
        ans = self.p.val
        self.p = self.p.right
        return ans

    def hasNext(self) -> bool:
        return bool(self.p) or bool(self.stk)

