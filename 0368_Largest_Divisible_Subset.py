from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1 for _ in range(n)]
        maxSize = 1
        maxVal = dp[0]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > maxSize:
                maxSize = dp[i]
                maxVal = nums[i]
        res = list()
        if maxSize == 1:
            res.append(nums[0])
            return res
        for i in range(n-1, -1, -1):
            if dp[i] == maxSize and maxVal % nums[i] == 0:
                res.append(nums[i])
                maxVal = nums[i]
                maxSize -= 1
                if maxSize <= 0:
                    break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.largestDivisibleSubset([1,2,3]))
    print(s.largestDivisibleSubset([1,2,4,8]))

