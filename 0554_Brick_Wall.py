from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        re = dict()
        for row in wall:
            curlen = row[0]
            for i in range(1, len(row)):
                if curlen not in re:
                    re[curlen] = 1
                else:
                    re[curlen] += 1
                curlen += row[i]
        if not re:
            return len(wall)
        maxx = max(re.values())
        return len(wall) - maxx


if __name__ == '__main__':
    s = Solution()
    print(s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
    print(s.leastBricks([[1],[1],[1]]))
