from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        allsum = sum(nums)
        if allsum - target < 0 or (allsum - target) % 2 != 0:
            return 0
        neg = (allsum - target) // 2
        dp = [[0 for _ in range(neg + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(0, neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[n][neg]


if __name__ == '__main__':
    s = Solution()
    print(s.findTargetSumWays([1,1,1,1,1], 3))

