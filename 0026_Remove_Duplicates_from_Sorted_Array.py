from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        quick, slow = 1, 0
        while quick < len(nums):
            if nums[quick] != nums[slow]:
                nums[slow + 1] = nums[quick]
                slow += 1
            quick += 1
        return slow + 1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

