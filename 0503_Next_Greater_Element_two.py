from typing import List


# dan diao zhan
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1 for _ in range(n)]
        stk = list()
        for i in range(2 * n - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ans[stk.pop()] = nums[i % n]
            stk.append(i % n)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElements([1, 2, 1]))
