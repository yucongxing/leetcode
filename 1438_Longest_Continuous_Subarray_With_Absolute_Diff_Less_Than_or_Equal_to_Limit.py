from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        maxque, minque = deque(), deque()
        left = right = ret =0

        while right < n:
            while maxque and maxque[-1] < nums[right]:
                maxque.pop()
            while minque and minque[-1] > nums[right]:
                minque.pop()

            maxque.append(nums[right])
            minque.append(nums[right])

            while maxque and minque and maxque[0] - minque[0] > limit:
                if nums[left] == minque[0]:
                    minque.popleft()
                if nums[left] == maxque[0]:
                    maxque.popleft()
                left += 1

            ret = max(ret, right - left + 1)
            right += 1
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubarray([8, 2, 4, 7], 4))
    print("hello world!")
