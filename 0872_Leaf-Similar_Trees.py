from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root: Optional[TreeNode], ans: List[int]) -> None:
            if not root:
                return
            dfs(root.left, ans)
            if self.isLeaf(root):
                ans.append(root.val)
            dfs(root.right, ans)
        ans1, ans2 = list(), list()
        dfs(root1, ans1)
        dfs(root2, ans2)
        return ans1 == ans2

    def isLeaf(self, node: TreeNode) -> bool:
        return node.left is None and node.right is None


if __name__ == '__main__':
    s = Solution()

