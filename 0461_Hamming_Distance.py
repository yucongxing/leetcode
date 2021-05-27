class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        cnt = 0
        while ans != 0:
            cnt += ans & 1
            ans >>= 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1,4))

