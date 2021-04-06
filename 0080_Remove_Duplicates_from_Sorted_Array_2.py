from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #cur = nums[0]
        #i = 1
        #d = 1
        #while i < len(nums):
            #if nums[i] == cur:
                #d += 1
            #else:
                #d = 1
                #cur = nums[i]
            #if d > 2:
                #nums.pop(i)
                #d = 2
            #else:
                #i += 1
        #return len(nums)

        # official solution:
        n = len(nums)
        if n <= 2:
            return n
        
        fast = slow = 2
        while fast < n:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,1,2,2,3]
    l = s.removeDuplicates(nums)
    print(l, nums)

