from typing import List
from itertools import accumulate


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        presum = list(accumulate(candiesCount))

        ans = list()
        for ft, fd, dc in queries:
            x1 = fd + 1
            x2 = (fd + 1) * dc
            y1 = 1 if ft == 0 else presum[ft - 1] + 1
            y2 = presum[ft]
            ans.append(not(x1 > y2 or x2 < y1))

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.canEat([7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]))
