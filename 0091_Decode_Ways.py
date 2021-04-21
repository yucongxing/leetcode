class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        if n == 1:
            return 1
        pp, p = 1, 1
        ans = p
        for i in range(1, n):
            if s[i] == '0' and (s[i-1] != '1' and s[i-1] != '2'):
                return 0
            if s[i] == '0':
                ans = pp
                p = pp
                continue
            if s[i - 1] == '1':
                ans = pp + p
            elif s[i - 1] =='2':
                if ord(s[i]) - ord('0') <= 6:
                    ans = pp + p
            pp = p
            p = ans
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('12'))
    print(s.numDecodings('226'))
    print(s.numDecodings('2101'))
    print(s.numDecodings('1123'))
    print(s.numDecodings('1201234'))
    print(s.numDecodings('123123'))

