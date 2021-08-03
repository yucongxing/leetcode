from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        minn, left = 100001, -1
        maxn, right = -100001, -1
        for i in range(n):
            if nums[i] >= maxn:
                maxn = nums[i]
            else:
                right = i
            if nums[n - i - 1] <= minn:
                minn = nums[n - i - 1]
            else:
                left = n - i - 1
        return 0 if right == -1 else right - left + 1


if __name__ == '__main__':
    s = Solution()
    print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))
