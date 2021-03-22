class Solution:
    def hammingWeight(self, n: int) -> int:
        # return str(bin(n)).count('1')
        ans = 0
        while n:
            n = n & (n-1)
            ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(6))
