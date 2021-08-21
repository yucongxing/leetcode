class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s1 = list(s)
        for i in range(0, n, 2 * k):
            s1[i: i + k] = reversed(s1[i: i + k])
        return ''.join(s1)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr('leetcode', 2))

