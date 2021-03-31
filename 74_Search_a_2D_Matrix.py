from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        middle = (left + right) // 2
        while left <= right:
            if matrix[middle // n][middle - middle // n * n] == target:
                return True
            elif matrix[middle // n][middle - middle // n * n] > target:
                right  = middle - 1
                middle = (left + right) // 2
            else:
                left = middle + 1
                middle = (left + right) // 2
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
