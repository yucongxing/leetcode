class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        m, n = steps + 1, min(steps, arrLen)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = dp[i-1][j]
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % mod
                if j < n - 1:
                    dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % mod
        return dp[steps][0]


if __name__ == '__main__':
    s = Solution()
    print(s.numWays(3, 2))
    print(s.numWays(2, 4))
