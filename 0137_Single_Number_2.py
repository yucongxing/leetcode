from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = 0
            for n in nums:
                total += (n >> i) & 1
            if total % 3 != 0:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 <<i)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1,2,1,1]))
