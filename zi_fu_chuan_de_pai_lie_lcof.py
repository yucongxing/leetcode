from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        ls, ans = list(s), list()
        def dfs(i: int) -> None:
            if i == n - 1:
                ans.append(''.join(ls))
                return
            re = set()
            for j in range(i, n):
                if ls[j] in re:
                    continue
                re.add(ls[j])
                ls[j], ls[i] = ls[i], ls[j]
                dfs(i + 1)
                ls[j], ls[i] = ls[i], ls[j]
        dfs(0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.permutation('abc'))
