from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cur = 0
        ans = 0
        for i in range(len(costs)):
            if cur + costs[i] > coins:
                break
            cur += costs[i]
            ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxIceCream([1, 3, 2, 4, 1], 7))
