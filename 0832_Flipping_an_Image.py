from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[j ^ 1 for j in i[::-1]] for i in A]


if __name__ == "__main__":
    s = Solution()
    print(s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
