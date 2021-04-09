from typing import List, Optional


class Solution:
    def findMin(self, nums: List[int]) -> Optional[int]:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]

        for i in range(1,n):
            if nums[i] > nums[i+1]:
                return nums[i+1]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([3,4,5,1,2]))
