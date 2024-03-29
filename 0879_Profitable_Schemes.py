from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        length = len(group)
        dp = [[[0 for _ in range(minProfit + 1)] for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            members, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < members:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        if earn > k:
                            dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - members][0]
                        else:
                            dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - members][k - earn]
                        # dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - earn)]) % MOD
        total = sum(dp[length][j][minProfit] for j in range(n + 1))
        return total % MOD


if __name__ == '__main__':
    s = Solution()
    print(s.profitableSchemes(5, 3, [2, 2], [2, 3]))
    print(s.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))

