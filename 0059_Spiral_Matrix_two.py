from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        layers = (n + 1) // 2
        num = n ** 2
        ans = [[0 for _ in range(n)] for _ in range(n)]
        cnt = 1
        for l in range(layers):
            for i in range(l, n-l):
                if cnt > num:
                    return ans
                ans[l][i] = cnt
                cnt += 1
            for i in range(l+1, n-l-1):
                if cnt > num:
                    return ans
                ans[i][n-l-1] = cnt
                cnt += 1
            for i in range(n-l-1, l-1, -1):
                if cnt > num:
                    return ans
                ans[n-l-1][i] = cnt
                cnt += 1
            for i in range(n-l-2, l, -1):
                if cnt > num:
                    return ans
                ans[i][l] = cnt
                cnt += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
    ma = s.generateMatrix(5)
    for l in ma:
        print(l)

