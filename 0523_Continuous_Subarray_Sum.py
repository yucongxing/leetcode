from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        map = {0: -1}
        presum = 0

        for i in range(n):
            presum += nums[i]
            if not (presum % k) in map:
                map[presum % k] = i
            else:
                if i - map[presum % k] >= 2:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkSubarraySum([0, 0], 1))
    print(s.checkSubarraySum([1, 2, 3], 5))
