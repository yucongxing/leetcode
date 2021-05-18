from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n - 1):
            sum = 0
            for k in range(i, n):
                sum ^= arr[k]
                if sum == 0 and k > i:
                    ans += (k - i)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countTriplets([2, 3, 1, 6, 7]))
