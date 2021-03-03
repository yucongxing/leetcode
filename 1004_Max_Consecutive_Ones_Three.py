from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        left = lsum = rsum = 0
        ans = 0

        for right in range(n):
            rsum += 1 - A[right]
            while lsum < rsum - K:
                lsum += 1 - A[left]
                left += 1
            ans = max(ans, right - left + 1)

        return ans


s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
