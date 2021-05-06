from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in range(len(encoded)):
            ans.append(encoded[i] ^ ans[i])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.decode([1,2,3], 1))
    print(s.decode([6,2,7,3], 4))

