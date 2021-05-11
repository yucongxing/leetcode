from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total ^= i
        odd = 0
        for i in range(1, n - 1, 2):
            odd ^= encoded[i]
        perm = [0 for _ in range(n)]
        perm[0] = total ^ odd
        for i in range(0, n - 1):
            perm[i+1] = perm[i] ^ encoded[i]
        return perm


if __name__ == '__main__':
    s = Solution()
    print(s.decode([3,1]))
