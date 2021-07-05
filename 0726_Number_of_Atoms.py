class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = list()
        i, n = 0, len(formula)
        stack.append(dict())
        while i != n:
            if formula[i] == '(':
                i += 1
                stack.append(dict())
            elif formula[i] == ')':
                i += 1
                num = 0
                if i == n or not (ord('0') <= ord(formula[i]) <= ord('9')):
                    num = 1
                while i < n and ord('0') <= ord(formula[i]) <= ord('9'):
                        num = num * 10 + ord(formula[i]) - ord('0')
                        i += 1
                top = stack.pop(-1)
                for k, v in top.items():
                    if k in stack[-1]:
                        stack[-1][k] += v * num
                    else:
                        stack[-1][k] = v * num
            else:
                atom = list()
                atom.append(formula[i])
                i += 1
                while i < n and ord('a') <= ord(formula[i]) <= ord('z'):
                    atom.append(formula[i])
                    i += 1
                atom = ''.join(atom)
                
                num = 0
                if i == n or not (ord('0') <= ord(formula[i]) <= ord('9')):
                    num = 1
                while i < n and ord('0') <= ord(formula[i]) <= ord('9'):
                        num = num * 10 + ord(formula[i]) - ord('0')
                        i += 1
                if atom in stack[-1]:
                    stack[-1][atom] += num
                else:
                    stack[-1][atom] = num
        top = stack[-1]
        ans = sorted(top.items(), key=lambda x: x[0])
        return ''.join([w[0] + (str(w[1]) if w[1] > 1 else '') for w in ans])


if __name__ == '__main__':
    s = Solution()
    print(s.countOfAtoms('H2O'))
    print(s.countOfAtoms('K4(ON(SO3)2)2'))
