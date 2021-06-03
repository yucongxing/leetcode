from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        re = {0: -1}
        counter = 0

        for i in range(n):
            if nums[i] == 0:
                counter -= 1
            else:
                counter += 1
            if counter in re:
                ans = max(ans, i - re[counter])
            else:
                re[counter] = i

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxLength([0, 1, 0]))
