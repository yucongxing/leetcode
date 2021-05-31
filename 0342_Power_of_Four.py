class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(1))
    print(s.isPowerOfFour(4))
    print(s.isPowerOfFour(16))
    # 100 10000

