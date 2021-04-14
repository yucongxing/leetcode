from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        premin = [float('inf') for _ in range(n)]
        for i in range(1, n):
            premin[i] = min(premin[i - 1], nums[i - 1])
        stk = list()
        for i in range(n - 1, -1, -1):
            nmusk = float('-inf')
            while stk and stk[-1] < nums[i]:
                nmusk = stk.pop()
            if premin[i] < nmusk:
                return True
            stk.append(nums[i])
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.find132pattern([1,2,3,4]))
    print(s.find132pattern([3,1,4,2]))
    print(s.find132pattern([-1, 3,2,0]))
    
