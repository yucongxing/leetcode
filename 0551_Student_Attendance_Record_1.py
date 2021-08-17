class Solution:
    def checkRecord(self, s: str) -> bool:
        anum = 0
        for i in range(len(s)):
            if s[i] == 'A':
                anum += 1
            if anum >= 2:
                return False
            if i >= 3 and s[i] == s[i - 1] == s[i - 2] == 'L':
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkRecord('PPALLP'))
    print(s.checkRecord('PPALLL'))
