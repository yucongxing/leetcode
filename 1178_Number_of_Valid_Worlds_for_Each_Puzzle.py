from typing import List
import collections


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        re = collections.Counter()

        for w in words: # 遍历每一个word
            mask = 0   # 计算每一个word对应的hash值，每个字母出现用对应位数的二进制为1来表示
            for s in w:
                # 1右移每个字母的顺序的位数，然后加到hash值上面，如果该位已经出现，则不改变（这就是为什么用 | 或操作
                mask |= (1 << (ord(s) - ord('a')))               
            if str(bin(mask)).count('1') <= 7:   # 因为题目给定了puzzles只有7位，所以大于7位的肯定是没有对应的puzzles的，直接舍弃
                re[mask] += 1

        ans = list()
        for p in puzzles:
            total = 0

            mask = 0
            for i in range(1, 7):
                mask |= (1 << (ord(p[i]) - ord('a')))

            subset = mask   # 计算二进制子集的通用模板
            while subset:
                s = subset | (1 << (ord(p[0]) - ord('a')))
                if s in re:
                    total += re[s]
                subset = (subset-1) & mask
            
            if (1 << (ord(p[0]) - ord('a'))) in re:  # subset = 0的时候，while循环九退出了，这时候s = sunset | (1 << (ord(p[0]) - ord('a')))就是只含首字母的子集，没有被计算到，所以要特判
                total += re[(1 << (ord(p[0]) - ord('a')))]

            ans.append(total)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findNumOfValidWords(["aabo"],["abvoeyz"]))
