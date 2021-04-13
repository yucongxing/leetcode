from typing import AnyStr


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ans = list()
        def travel(root):
            if not root:
                return
            travel(root.left)
            ans.append(root.val)
            travel(root.right)
        travel(root)
        minans = 100002
        for i in range(len(ans)-1):
            if ans[i+1] - ans[i] < minans:
                minans = ans[i+1] - ans[i]
        return minans

if __name__ == '__main__':
    s = Solution()

