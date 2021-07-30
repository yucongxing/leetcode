from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = list()
        l = 1
        while 2 ** l - 1 < label:
            level.append(2 ** l - 1)
            l += 1
        level.append(2**l - 1)
        ans = list()
        for i in range(len(level), 0, -1):
            # print(i, '->', label)
            ans.append(label)
            if label == 1:
                break
            if i % 2 == 0:
                label = level[i - 2] + level[i - 1] - label + 1
                label = label // 2
            else:
                label = label // 2
                if label != 1:
                    label = level[i-3] + level[i-2] - label + 1
        ans.reverse()
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.pathInZigZagTree(14))
    print(s.pathInZigZagTree(26))
