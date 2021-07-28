from typing import Dict, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        father = dict()
        father[root.val] = None

        def dfs(root: TreeNode, father: Dict, p: TreeNode) -> None:
            if root is None:
                return
            if not p is None:
                father[root.val] = p
            dfs(root.left, father, root)
            dfs(root.right, father, root)
        dfs(root, father, None)

        ans = list()
        visit = set()
        def dfs1(root, distance):
            if root is None:
                return
            if root.val in visit:
                return
            visit.add(root.val)
            if distance == k:
                ans.append(root.val)
                return
            dfs1(root.left, distance + 1)
            dfs1(root.right, distance + 1)
            dfs1(father[root.val], distance + 1)
        dfs1(target, 0)
        return ans

