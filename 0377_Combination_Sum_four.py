from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4([1], 4))
    print(s.combinationSum4([1,2,3], 4))
    print(s.combinationSum4([4,2,1], 32))
