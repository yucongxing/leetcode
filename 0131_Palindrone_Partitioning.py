from typing import List


class Solution:
    def partition(self, s: str) -> List[List[int]]:
        n = len(s)
        dp = [[True for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
        ret = list()
        ans = list()
        def dfs(i: int) -> None:
            if i == n:
                ret.append(ans[:])
                return
            for j in range(i, n):
                if dp[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()
        dfs(0)
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
