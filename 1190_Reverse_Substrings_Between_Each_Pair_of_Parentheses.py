class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = list()
        for i in range(n):
            if s[i] != ')':
                stack.append(s[i])
            if stack and s[i] == ')':
                temp = list()
                while stack[-1] != '(':
                    temp.append(stack.pop(-1))
                stack.pop(-1)
                stack.extend(temp)
        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseParentheses('(ed(et(oc))el)'))
    print(s.reverseParentheses('a(bcdefghijkl(mno)p)q'))
