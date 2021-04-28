import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c % 4 == 3:
            return False
        if c == 0:
            return True
        for i in range(int(math.sqrt(c)) + 1):
           remain = c - i * i
           if remain == int(math.sqrt(remain)) * int(math.sqrt(remain)):
               return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.judgeSquareSum(5))
    print(s.judgeSquareSum(4))
    print(s.judgeSquareSum(3))
