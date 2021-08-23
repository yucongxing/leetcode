class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        ans = [0 for _ in range(n + 1)]
        ans[0] = 0
        ans[1] = 1
        for i in range(2, n + 1):
            if i & 1 == 1:
                ans[i] = ans[i // 2] + ans[i // 2 + 1]
            else:
                ans[i] = ans[i // 2]
        return max(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.getMaximumGenerated(7))
