# 1 2 2 5 6 6
class Solution:
    def arrayPairSum(self,nums):
        nums.sort()
        ans = 0
        for i in range(0,len(nums),2):
            ans += nums[i]
        return ans

s = Solution()
print(s.arrayPairSum([6,2,6,5,1,2]))
