class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = list()
        queue.append((0, root))
        xf, yf = False, False
        while queue:
            f1, f2 = False, False
            le, p = queue.pop(0)
            if p.val == x:
                xf = True
            if p.val == y:
                yf = True
            if p.left:
                queue.append((le + 1, p.left))
                f1 = (p.left.val == y or p.left.val == x)
            if p.right:
                queue.append((le + 1, p.right))
                f2 = (p.right.val == y or p.right.val == x)
            if f1 and f2:
                return False
            if queue and queue[0][0] != le:
                if xf != yf:
                    return False
                if xf and yf:
                    return True
        return xf and yf


if __name__ == '__main__':
    s = Solution()

