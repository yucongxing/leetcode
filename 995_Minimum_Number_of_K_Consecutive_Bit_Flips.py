from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        diff = [0 for _ in range(n + 1)]
        res = 0
        revcnt = 0
        for i in range(n):
            revcnt += diff[i]
            if (A[i] + revcnt) % 2 == 0:
                if i + K > n:
                    return -1
                res += 1
                revcnt += 1
                diff[i + K] -= 1
        return res


s = Solution()
print(s.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))
