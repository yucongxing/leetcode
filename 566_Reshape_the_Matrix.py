class Solution:
    def matrixReshape(self,nums,r,c):
        row,col = len(nums),len(nums[0])
        if row*col != r*c:
            return nums
        ans = [[None]*c for _ in range(r)]
        cnt = 0
        for i in range(r):
            for j in range(c):
                ans[i][j] = nums[cnt//col][cnt-cnt//col*col]
                cnt += 1
        return ans

s = Solution()
print(s.matrixReshape([[1,2],[3,4]],4,1))

