from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda a:(a[0], -a[1]))

        n = len(envelopes)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) 


if __name__ == '__main__':
    s = Solution()
    print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
