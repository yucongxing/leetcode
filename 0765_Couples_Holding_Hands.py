class Solution:
    def minSwapsCouples(self,row):
        ans = 0
        for i in range(0, len(row), 2):
            if row[i+1] != row[i]^1:
                j = row.index(row[i]^1);
                row[i+1], row[j] = row[j], row[i+1]
                ans += 1
        return ans

s = Solution()
print(s.minSwapsCouples([0,2,1,3]))

