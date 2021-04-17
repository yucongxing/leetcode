from typing import List
from sortedcontainers import SortedSet
import bisect


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        st = SortedSet()
        left, right = 0, 0
        while right < len(nums): 
            if right - left > k:
                st.remove(nums[left])
                left += 1
            idx = bisect.bisect_left(st, nums[right] - t)
            if st and idx >= 0 and idx < len(st) and abs(nums[right] - st[idx]) <= t:
                return True
            st.add(nums[right])
            right += 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyAlmostDuplicate([1,2,3,1], k = 3, t = 0))
