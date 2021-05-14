class Solution:
    def intToRoman(self, num: int) -> str:
        s = str(num)
        n = len(s)
        ans = ''
        for i in range(n, 0, -1):
            if i == 4:
                ans += (self.print4(ord(s[n - i]) - ord('0')))
            elif i == 3:
                ans += (self.print3(ord(s[n - i]) - ord('0')))
            elif i == 2:
                ans += (self.print2(ord(s[n - i]) - ord('0')))
            else:
                ans += (self.print1(ord(s[n - i]) - ord('0')))
        return ans

    def print1(self, i: int):
        ans = ''
        if i <= 3:
            ans += ('I' * i)
        elif i==4:
            ans += ('IV')
        elif i == 5:
            ans += ('V')
        elif i <= 8:
            ans += ('V' + 'I' * (i - 5))
        else:
            ans += ('IX')
        return ans

    def print2(self, i: int):
        ans = ''
        if i <= 3:
            ans += ('X' * i)
        elif i==4:
            ans += ('XL')
        elif i == 5:
            ans += ('L')
        elif i <= 8:
            ans += ('L' + 'X' * (i - 5))
        else:
            ans += ('XC')
        return ans

    def print3(self, i: int):
        ans = ''
        if i <= 3:
            ans += ('C' * i)
        elif i==4:
            ans += ('CD')
        elif i == 5:
            ans += ('D')
        elif i <= 8:
            ans += ('D' + 'C' * (i - 5))
        else:
            ans += ('CM')
        return ans

    def print4(self, i: int):
        ans = ''
        ans += ('M' * i)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(1994))
    print(s.intToRoman(58))

