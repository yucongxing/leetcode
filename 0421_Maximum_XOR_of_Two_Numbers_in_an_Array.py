from typing import List


class Trie:
    def __init__(self):
        self.left = None
        self.right = None


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        MAX_BIT = 30

        def add(num: int):
            p = root
            for i in range(MAX_BIT, -1, -1):
                bit = (num >> i) & 1
                if bit == 0:
                    if not p.left:
                        p.left = Trie()
                    p = p.left
                else:
                    if not p.right:
                        p.right = Trie()
                    p = p.right
        def check(num: int) -> int:
            ans = 0
            p = root
            for i in range(MAX_BIT, -1, -1):
                bit = (num >> i) & 1
                if bit == 0:
                    if p.right:
                        p = p.right
                        ans = ans* 2 + 1
                    else:
                        p = p.left
                        ans *= 2
                else:
                    if p.left: 
                        p = p.left
                        ans =  ans * 2 + 1
                    else:
                        p = p.right
                        ans *= 2
            return ans

        n = len(nums)
        ans = 0
        for i in range(1, n):
            add(nums[i-1])
            ans = max(ans, check(nums[i]))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMaximumXOR([3, 10, 5, 25, 2, 8]))
    print(s.findMaximumXOR([8, 10, 2]))

