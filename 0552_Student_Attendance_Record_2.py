class Solution:
    def checkRecord(self, n: int) -> int:
        mod = int(1e9 + 7)
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1
        for i in range(1, n + 1):
            dp[i][0][0] = ((dp[i - 1][0][0] + dp[i - 1][0][1]) % mod + dp[i - 1][0][2]) % mod
            dp[i][0][1] = dp[i - 1][0][0]
            dp[i][0][2] = dp[i - 1][0][1]
            dp[i][1][0] = (((dp[i - 1][0][0] + dp[i - 1][0][1]) % mod + dp[i - 1][0][2]) % mod + ((dp[i - 1][1][0] + dp[i - 1][1][1]) % mod + dp[i - 1][1][2]) % mod) % mod
            dp[i][1][1] = dp[i - 1][1][0]
            dp[i][1][2] = dp[i - 1][1][1]
        return (((((dp[n][0][0] + dp[n][0][1]) % mod + dp[n][0][2]) % mod + dp[n][1][0]) % mod + dp[n][1][1]) % mod + dp[n][1][2]) %mod


if __name__ == '__main__':
    s = Solution()
    print(s.checkRecord(2))
    print(s.checkRecord(3))
    print(s.checkRecord(1))
    print(s.checkRecord(10101))
