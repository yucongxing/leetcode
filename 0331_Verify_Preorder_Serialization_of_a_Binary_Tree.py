class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1
        for ch in preorder.split(','):
            if slot == 0:
                return False
            if ch.isdigit():
                slot += 1
            else:
                slot -= 1
        return slot == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSerialization('#,#,3,5,#'))
