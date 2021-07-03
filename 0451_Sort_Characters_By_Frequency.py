from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        ans = sorted(c.items(), key=lambda x: x[1], reverse=True)
        print(ans)
        ans = ''.join([w[0] * w[1] for w in ans])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.frequencySort('tree'))
