class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            middle = l + (r - l) // 2
            if isBadVersion(middle):
                r = middle
            else:
                l = middle + 1
        return l

