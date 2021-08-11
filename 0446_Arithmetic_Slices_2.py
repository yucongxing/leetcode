from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        dp = [defaultdict(int) for _ in range(len(nums))]
        for i, x in enumerate(nums):
            for j in range(i):
                d = x - nums[j]
                cnt = dp[j][d]
                ans += cnt
                dp[i][d] += (cnt + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices([1,2,3,4,5,6]))
    print(s.numberOfArithmeticSlices([7,7,7,7,7]))
