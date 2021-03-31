from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        re = dict()
        for i in range(len(nums)):
            if target - nums[i] in re:
                return [i, re[target - nums[i]]]
            re[nums[i]] = i
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15],9))
