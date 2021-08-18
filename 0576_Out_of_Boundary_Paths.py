class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove + 1)]
        neignbor = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        dp[0][startRow][startColumn] = 1
        mod = int(1e9 + 7)
        ans = 0
        for i in range(1, maxMove + 1):
            for j in range(m):
                for k in range(n):
                    for ne in neignbor:
                        nextj, nextk = j + ne[0], k + ne[1]
                        if 0 <= nextj < m and 0 <= nextk < n:
                            dp[i][nextj][nextk] = (dp[i - 1][j][k] + dp[i][nextj][nextk]) % mod
                        else:
                            ans = (ans + dp[i - 1][j][k]) % mod
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findPaths(2, 2, 2, 0, 0))
    print(s.findPaths(1, 3, 3, 0, 1))

