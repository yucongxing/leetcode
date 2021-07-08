from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        presum = 0
        cnt = dict()
        ret = 0
        for n in nums:
            if presum in cnt:
                cnt[presum] += 1
            else:
                cnt[presum] = 1
            presum += n
            if presum - goal in cnt:
                ret += cnt[presum - goal]
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
    print(s.numSubarraysWithSum([0, 0, 0, 0, 0], 0))
