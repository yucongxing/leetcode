class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxlen = 0
        ulen = 0
        for i, n in enumerate(nums):
            if n == 0 or i == len(nums)-1:
                if n == 1:
                    ulen += 1
                if ulen > maxlen:
                    maxlen = ulen
                ulen = 0
            else:
                ulen+=1
        return maxlen

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))
