class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        lst = list(range(start, start + (n-1) * 2 + 1, 2))
        print(lst)
        ans = 0
        for i in lst:
            ans ^= i
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.xorOperation(5, 0))
    print(s.xorOperation(4, 3))
    print(s.xorOperation(1, 7))
    print(s.xorOperation(10, 5))

