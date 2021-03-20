from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = list()
        for ch in tokens:
            if ch in '+-*/':
                n1 = stk.pop()
                n2 = stk.pop()
                if ch == '+':
                    stk.append(n1 + n2)
                elif ch == '-':
                    stk.append(n2 - n1)
                elif ch == '*':
                    stk.append(n1 * n2)
                else:
                    stk.append(int(n2 / n1))
            else:
                num = 0
                sign = 1
                if ch[0] == '-':
                    sign = -1
                    ch = ch[1:]
                for c in ch:
                    num = num * 10 + ord(c) - ord('0')
                stk.append(sign * num)

        return stk[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["2","1","+","3","*"]))
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
