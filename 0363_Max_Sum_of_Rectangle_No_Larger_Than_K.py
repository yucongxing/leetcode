from typing import List
from sortedcontainers import SortedList
 

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')
        for i in range(m):
            sumlst = [0 for _ in range(n)]
            for j in range(i, m):
                for c in range(n):
                    sumlst[c] += matrix[j][c]
                sumSet = SortedList([0])
                s = 0
                for v in sumlst:
                    s += v
                    lb = sumSet.bisect_left(s - k)
                    if lb != len(sumSet):
                        ans = max(ans, s - sumSet[lb])
                    sumSet.add(s)

        return int(ans)

