from typing import List
from collections import Counter


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        MAX = 2 ** 10
        n = len(nums)

        dp = [0x3fffffff for _ in range(MAX)]
        dp[0] = 0

        for i in range(k):
            c = Counter()
            size = 0
            for j in range(i, n, k):
                c[nums[j]] += 1
                size += 1

            t2min = min(dp)

            g = [t2min for _ in range(MAX)]
            for mask in range(MAX):
                for x , cx in c.items():
                    g[mask] = min(g[mask], dp[mask ^ x] - cx)
            dp = [val + size for val in g]
        return dp[0]


if __name__ == '__main__':
    s = Solution()
    print(s.minChanges([1, 2, 0, 3, 0], 1))

