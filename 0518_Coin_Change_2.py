from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # @lru_cache(None)
        # def dfs(amount: int, i: int) -> int:
            # if i >= n or amount < 0:
                # return 0
            # if amount == 0:
                # return 1
            # # select current coin
            # ans = dfs(amount - coins[i], i)
            # # don't select current coin
            # ans += dfs(amount, i + 1)
            # return ans
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[amount]


if __name__ == '__main__':
    s = Solution()
    print(s.change(5, [1, 2, 5]))
    print(s.change(3, [2]))

