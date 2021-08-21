from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return n
        cur = chars[0]
        cnt = 1
        new = 0
        for i in range(1, n):
            if chars[i] != cur:
                chars[new] = cur
                new += 1
                if cnt > 1:
                    for t in str(cnt):
                        chars[new] = t
                        new += 1
                cur = chars[i]
                cnt = 1
            else:
                cnt += 1
            if i == n - 1:
                chars[new] = cur
                new += 1
                if cnt > 1:
                    for t in str(cnt):
                        chars[new] = t
                        new += 1

        return new


if __name__ == '__main__':
    s = Solution()
    print(s.compress(['a', 'a', 'b', 'b', 'c', 'c', 'c']))
        
