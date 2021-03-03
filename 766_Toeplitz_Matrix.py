from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))

