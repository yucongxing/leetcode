class Solution:
    def romanToInt(self, s: str) -> int:
        re = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        ans = 0
        for i in range(n):
            if i < n - 1:
                if re[s[i]] < re[s[i + 1]]:
                    ans -= re[s[i]]
                else:
                    ans += re[s[i]]
            else:
                ans += re[s[i]]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MCMXCIV'))
    print(s.romanToInt('LVIII'))

