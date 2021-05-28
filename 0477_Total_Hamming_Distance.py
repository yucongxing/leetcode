from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        re = [0 for _ in range(32)]
        for i in range(n):
            for j in range(32):
                re[j] += ((nums[i] >> j) & 1)
        ans = 0
        for c in re:
            ans += c * (n - c)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.totalHammingDistance([4, 14, 4]))

