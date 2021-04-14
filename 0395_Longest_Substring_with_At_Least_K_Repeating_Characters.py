from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        return self.divideConquer(s, 0, n - 1, k)

    def divideConquer(self, s: str, left: int, right: int, k: int) -> int:
        longest = 0
        re = Counter(s[left: right + 1])
        
        split = None
        for ch, cnt in re.items():
            if cnt < k:
                split = ch

        if split is None:
            return right - left + 1

        i = left
        while i <= right:
            while i <= right and s[i] == split:
                i += 1
            if i > right:
                break
            start = i
            while i <= right and s[i] != split:
                i += 1

            longest = max(longest,self.divideConquer(s, start, i - 1, k))

        return longest


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring('ababbc',2))
    print(s.longestSubstring('ababacb',3))

