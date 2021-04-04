from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if not answers:
            return 0
        re = dict()
        ret = 0
        for a in answers:
            if a in re:
                re[a] += 1
            else:
                re[a] = 1
        for k, v in re.items():
            ret += (v + k) // ( k + 1) * (k + 1)
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.numRabbits([1,1,2]))
    print(s.numRabbits([0,0,1,1,1]))
