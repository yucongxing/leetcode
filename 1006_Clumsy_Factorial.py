class Solution:
    def clumsy(self, N: int) -> int:
        ans = 0
        cnt = 0
        stk = list()
        stk.append(N)
        for i in range(N - 1, 0, -1):
            if cnt % 4 == 0:
                t = stk.pop()
                stk.append(t*i)
            elif cnt % 4 == 1:
                t = stk.pop()
                stk.append(int(t/i))
            elif cnt % 4 == 2:
                stk.append(i)
            else:
                stk.append(-i)
            cnt += 1

        ans = sum(stk)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.clumsy(10))
    print(s.clumsy(4))
