class Solution:
    def reverseVowels(self, s: str) -> str:
        can = 'aeiouAEIOU'
        s1 = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s1[l] in can and s1[r] in can:
                s1[l], s1[r] = s1[r], s1[l]
                l += 1
                r -= 1
            if s1[l] not in can:
                l += 1
            if s1[r] not in can:
                r -= 1
        return ''.join(s1)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels('leetcode'))
    print(s.reverseVowels('hello'))

