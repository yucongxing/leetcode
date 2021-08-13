class Solution:
    def countDigitOne(self, n: int) -> int:
        k = 1
        ans = 0
        while k <= n:
            ans += (n // (k * 10) * k + min(max(n % (k * 10) - k + 1, 0), k))
            k *= 10
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countDigitOne(13))

