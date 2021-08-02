from typing import List
from functools import cmp_to_key


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = list()
        for i in range(m):
            l, r = 0, n - 1
            while l < r:
                middle = ((l + r) // 2)
                print(middle, l, r)
                if mat[i][middle] == 0:
                    r = middle - 1
                else:
                    l = middle
            ans.append((i, l + 1))
        def cmp(a, b):
            if a[1] == b[1]:
                return a[0] - b[0]
            else:
                return a[1] - b[1]
        ans.sort(key=cmp_to_key(cmp))
        return [x[0] for x in ans[:k]]


if __name__ == '__main__':
    s = Solution()
    print(s.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))

