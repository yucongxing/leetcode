class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n + 1))
        for i in range(1, n + 1):
            minn = 0xfffffff
            j = 1
            while j * j <= i:
                minn = min(minn, dp[i - j * j])
                j += 1
            dp [i] = minn + 1
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(12))

