from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        allsum = sum(stones)
        neg = allsum // 2
        dp = [[False for _ in range(neg + 1)] for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= stones[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - stones[i - 1]]
        for i in range(neg, -1, -1):
            if dp[n][i]:
                return allsum - 2 * i
        return allsum


if __name__ == '__main__':
    s = Solution()
    print(s.lastStoneWeightII([2, 7, 4, 1, 8, 1]))

