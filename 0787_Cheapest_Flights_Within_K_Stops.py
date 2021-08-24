from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = 0xFFFFFFF
        dp = [[inf for _ in range(n)] for _ in range(k + 2)]
        dp[0][src] = 0
        for i in range(1, k + 2):
            for u, v, p in flights:
                dp[i][v] = min(dp[i - 1][u] + p, dp[i][v])
        ans = min(dp[x][dst] for x in range(1, k + 2))
        return ans if ans != inf else -1


if __name__ == "__main__":
    s = Solution()
    print(
        s.findCheapestPrice(
            n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1
        )
    )
    print(
        s.findCheapestPrice(
            n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0
        )
    )
    print(s.findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1))
