from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        ret = 0
        for n in nums:
            ret ^= n
        return ret == 0


if __name__ == '__main__':
    s = Solution()
    print(s.xorGame([1,1,2]))
