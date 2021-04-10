class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n >>= 1
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(6))
    print(s.isUgly(8))
    print(s.isUgly(14))
