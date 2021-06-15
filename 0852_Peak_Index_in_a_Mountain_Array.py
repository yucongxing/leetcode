from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) >> 1
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.peakIndexInMountainArray([0, 1, 0]))
