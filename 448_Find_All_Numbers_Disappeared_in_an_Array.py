class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)
        return res


s = Solution()
res = s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
print(res)
