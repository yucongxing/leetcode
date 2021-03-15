from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = list()
        layers = (min(m, n) + 1) // 2
        cnt = 0
        for l in range(layers):
            for i in range(l, n - l):
                if cnt == n*m:
                    break
                ans.append(matrix[l][i])
                cnt += 1
            for i in range(l + 1, m - l - 1):
                if cnt == n*m:
                    break
                ans.append(matrix[i][n - l - 1])
                cnt += 1
            for i in range(n - l - 1, l - 1, -1):
                if cnt == n*m:
                    break
                ans.append(matrix[m - l - 1][i])
                cnt += 1
            for i in range(m - l - 2, l, -1):
                if cnt == n*m:
                    break
                ans.append(matrix[i][l])
                cnt += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(s.spiralOrder([[1,2,3,4]]))
    print(s.spiralOrder([[1]]))
