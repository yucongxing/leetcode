class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0, 1, 1]
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        for _ in range(3, n + 1):
            ans.append(ans[-1] + ans[-2] + ans[-3])
        return ans[n]


if __name__ == '__main__':
    s = Solution()
    print(s.tribonacci(4))
    print(s.tribonacci(25))
