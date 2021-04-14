from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        col0 = False
        row0 = False
        for i in range(col):
            if matrix[0][i] == 0:
                row0 = True
                break
        for i in range(row):
            if matrix[i][0] == 0:
                col0 = True
                break
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] =0
        if row0:
            for i in range(col):
                matrix[0][i] = 0
        if col0:
            for i in range(row):
                matrix[i][0] = 0


if __name__ == '__main__':
    s = Solution()
    m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(m)
    print(m)
