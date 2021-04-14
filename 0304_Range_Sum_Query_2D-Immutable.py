from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or matrix is None:
            return
        self.presum = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                self.presum[i][j] = matrix[i - 1][j - 1] + self.presum[i - 1][j] + self.presum[i][j - 1] - self.presum[i - 1][j - 1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int,) -> int:
        
        return self.presum[row2 + 1][col2 + 1] - self.presum[row2 + 1][col1] - self.presum[row1][col2 + 1] + self.presum[row1][col1]


if __name__ == '__main__':
    n = NumMatrix([[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],[1, 2, 0, 1, 5],[4, 1, 0, 1, 7],[1, 0, 3, 0, 5]])
    n1 = NumMatrix([[]])
    print(n.sumRegion(2, 1, 4, 3))
    print(n.sumRegion(1, 1, 2, 2))
    print(n.sumRegion(1, 2, 2, 4))
