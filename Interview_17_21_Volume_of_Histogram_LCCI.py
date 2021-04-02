from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        maxheight = max(height)
        maxleft, maxright = 0, n-1
        for i in range(n):
            if height[i] == maxheight:
                maxleft = i
                break
        for i in range(n-1, -1, -1):
            if height[i] == maxheight:
                maxright = i
                break
        ans = 0
        cur = 0
        for i in range(maxleft):
            if height[i] < height[cur]:
                ans += height[cur] - height[i]
            else:
                cur = i
        cur = n-1
        for i in range(n-1, maxright, -1):
            if height[i] < height[cur]:
                ans += height[cur] - height[i]
            else:
                cur = i
        for i in range(maxleft, maxright):
            ans += maxheight - height[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
