
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
# method 1
#        ans = list()
#        for i in range(num + 1):
#            ans.append(str(bin(i)).count('1'))
#        return ans
        ans = [0 for _ in range(num + 1)]
        highbit = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highbit = i
            ans[i] = ans[i - highbit] + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(2))
    print(s.countBits(5))
