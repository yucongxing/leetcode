class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return False if n < 0 else str(bin(n)).count('1') == 1
        return False if n <= 0 else (n & -n) == n


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(16))
    print(s.isPowerOfTwo(3))
