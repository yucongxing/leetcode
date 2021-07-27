class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return -1
        l, r = -1, -1
        if root.left.val > root.val:
            l = root.left.val
        else:
            l = self.findSecondMinimumValue(root.left)
        if root.right.val > root.val:
            r = root.right.val
        else:
            r = self.findSecondMinimumValue(root.right)

        if l == -1 and r == -1:
            return -1
        elif l == -1:
            return r
        elif r == -1:
            return l
        else:
            return min(r, l)
