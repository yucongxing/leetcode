class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    minx = 0x3fffffff
                    for k in range(i, j):
                        minx = min(minx, dp[i][k] + dp[k+1][j])
                    dp[i][j] = minx
        return dp[0][n-1]


if __name__ == '__main__':
    s = Solution()
    print(s.strangePrinter('aba'))
