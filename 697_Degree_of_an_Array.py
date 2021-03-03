from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = dict()
        for i, n in enumerate(nums):
            if n in mp:
                mp[n][0] += 1
                mp[n][2] = i
            else:
                mp[n] = [1, i, i]

        maxnum = 0
        minlen = 0
        for cnt, left, right in mp.values():
            if cnt > maxnum:
                maxnum = cnt
                minlen = right - left + 1
            elif cnt == maxnum:
                if right - left + 1 < minlen:
                    minlen = right - left + 1

        return minlen
