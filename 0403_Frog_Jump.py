from typing import List
from functools import lru_cache
import bisect


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        if stones[1] != 1:
            return False
        
        @lru_cache(None)
        def dfs(cur, k):
            if cur == n-1:
                return True
            nextStone = stones[cur] + k
            p1 = bisect.bisect_left(stones[cur + 1:], nextStone - 1)
            p2 = bisect.bisect_left(stones[cur + 1:], nextStone)
            p3 = bisect.bisect_left(stones[cur + 1:], nextStone + 1)
            ret1, ret2, ret3 = False, False, False
            if p1 + cur + 1 != n and stones[p1 + cur + 1] == nextStone - 1 and k != 1:
                ret1 = dfs(p1 + cur + 1, k - 1)
            if ret1:
                return ret1
            if p2 + cur + 1 != n and stones[p2 + cur + 1] == nextStone:
                ret2 = dfs(p2 + cur + 1, k)
            if ret2:
                return ret2
            if p3 + cur + 1 != n and stones[p3 + cur + 1] == nextStone + 1:
                ret3 = dfs(p3 + cur + 1, k + 1)
            return ret3
        return dfs(1, 1)


if __name__ == '__main__':
    s = Solution()
    print(s.canCross([0,1,3,5,6,8,12,17]))
    print(s.canCross([0,1,2,3,4,8,9,11]))
    print(s.canCross([0,1,2,5,6,9,10,12,13,14,17,19,20,21,26,27,28,29,30]))

