from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(start, end):
            m1, m2 = nums[start], max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                t = m2
                m2 = max(m1 + nums[i], m2)
                m1 = t
            return m2
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums)
        return max(robRange(0, n - 2), robRange(1, n - 1))

if __name__ == '__main__':
    s = Solution()
    print(s.rob([2,3,2]))
    print(s.rob([1,2,3,1]))
    print(s.rob([1,2]))

