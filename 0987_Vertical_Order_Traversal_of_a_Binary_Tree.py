from typing import List
from functools import cmp_to_key


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        re = dict()
        def dfs(root, row, col):
            if root is None:
                return
            if not (row, col) in re:
                re[(row, col)] = []
            re[(row, col)].append(root.val)
            dfs(root.left, row + 1, col -1)
            dfs(root.right, row + 1, col + 1)
        dfs(root, 0, 0)
        for r in re.keys():
            re[r].sort()
        def cmp(a, b):
            if a[0][1] == b[0][1]:
                return a[0][0] - b[0][0]
            else:
                return a[0][1] - b[0][1]
        preans = sorted(re.items(), key=cmp_to_key(cmp))
        colset = set()
        ans = list()
        for it in preans:
            if not it[0][1] in colset:
                ans.append([])
                colset.add(it[0][1])
            ans[-1].extend(it[1])
        return ans

