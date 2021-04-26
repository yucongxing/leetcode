from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)
        low = max(weights)
        high = sum(weights)
        while low < high:
            middle = low + (high - low) // 2
            temp = 0
            day = 1
            for i in range(n):
                temp += weights[i]
                if temp > middle:
                    temp = weights[i]
                    day += 1
            if day <= D:
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == '__main__':
    s = Solution()
    print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
    print(s.shipWithinDays([3,2,2,4,1,4],3))
