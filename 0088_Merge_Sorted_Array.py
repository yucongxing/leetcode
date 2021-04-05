from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1
        while p1 >=0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1
        if p1 >= 0: return
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1



if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    print(s.merge(nums1,3,[2,5,6],3))
    print(nums1)

