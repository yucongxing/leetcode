from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = 0
        right = n - 1
        for i in range(n):
            if nums[i] == target:
                return True
            if i < n - 1 and nums[i] > nums[i + 1]:
                left = i + 1
                break
        while left <= right:
            middle = left + (right - left) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.search([2,5,6,0,0,1,2], 0))
    print(s.search([2,5,6,0,0,1,2], 3))
    print(s.search([1,0,1,1,1], 0))
