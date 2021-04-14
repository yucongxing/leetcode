class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stk = list()
        presign = '+'
        num = 0

        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if s[i] in '+-*/' or i == n - 1:
                if presign == '+':
                    stk.append(num)
                elif presign == '-':
                    stk.append(-num)
                elif presign == '*':
                    stk[-1] *= num
                else:
                    stk[-1] = int(stk[-1] / num)
                presign = s[i]
                num = 0
        return sum(stk)


if __name__ == '__main__':
    s = Solution()
    print(s.calculate('2 + 4 /1'))

