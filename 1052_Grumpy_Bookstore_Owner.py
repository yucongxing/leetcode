from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        sumtotal = [0 for _ in range(n + 1)]
        sumg = [0 for _ in range(n + 1)]
        for i in range(1,n + 1):
            sumtotal[i] = customers[i - 1] +  sumtotal[i-1]
            sumg[i] = sumg[i-1] + (customers[i - 1] if grumpy[i - 1] == 0 else 0)
        maxdelta = 0
        for i in range(n - X + 1):
            if sumtotal[i + X] - sumtotal[i] - (sumg[i + X] - sumg[i]) > maxdelta:
                maxdelta = sumtotal[i + X] - sumtotal[i] - (sumg[i + X] - sumg[i]) 
        return sumg[-1] + maxdelta


if __name__ == "__main__":
    s = Solution()
    print(s.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0,1,0,1,0,1,0,1], 3))
    print(s.maxSatisfied([3], [1], 1))
