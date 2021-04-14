from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.presum = [0 for _ in range(len(self.nums) + 1)]
        for i in range(0, len(self.nums)):
            self.presum[i + 1] = self.presum[i] + self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.presum[j + 1] - self.presum[i]

