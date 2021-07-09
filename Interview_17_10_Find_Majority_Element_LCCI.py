from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        cnt = 0
        for n in nums:
            if cnt == 0:
                candidate = n
            if n == candidate:
                cnt += 1
            else:
                cnt -= 1

        cnt = 0
        for n in nums:
            if n == candidate:
                cnt += 1
        return candidate if cnt * 2 > len(nums) else -1


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3, 2]))
