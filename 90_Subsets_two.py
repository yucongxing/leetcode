from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        for mask in range(1<<(n)):
            subset = list()
            flag = True
            for i in range(n):
                if mask & (1 << i):
                    if i > 0 and mask >> (i - 1) & 1 == 0 and nums[i] == nums[i-1]:
                        flag = False
                        break
                    subset.append(nums[i])
            if flag:
                ans.append(subset)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))

