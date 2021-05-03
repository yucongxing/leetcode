class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = 1
        if x < 0:
            x *= -1
            sign = -1
        while x > 0:
            if ans > (2 ** 31 - 1) // 10:
                return 0
            t = x % 10
            ans = ans * 10 + t
            x //= 10
        ans = sign * ans
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
    print(s.reverse(123456789))
    print(s.reverse(1534236469))

