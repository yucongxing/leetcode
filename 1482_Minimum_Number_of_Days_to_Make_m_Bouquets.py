from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m > len(bloomDay) // k:
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            cnt = 0
            curm = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] > mid:
                    cnt = 0
                if bloomDay[i] <= mid:
                    cnt += 1
                if cnt == k:
                    curm += 1
                    cnt = 0
                if curm >= m:
                    break
            if curm >= m:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.minDays([1,10,3,10,2],3,1))
    print(s.minDays([1,10,3,10,2],3,2))
    print(s.minDays([7,7,7,7,12,7,7],2,3))
    print(s.minDays([1000000000, 1000000000],1,1))

