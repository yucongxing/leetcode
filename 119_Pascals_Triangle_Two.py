class Solution:
    def f(self, x: int):
        if x == 0 or x == 1:
            return 1
        else:
            return x * self.f(x - 1)

    def getRow(self, rowIndex: int):
        ans = list(range(0, rowIndex + 1))
        return [self.f(rowIndex) // self.f(rowIndex - a) // self.f(a) for a in ans]


s = Solution()
a = s.getRow(4)
print(a)
