from typing import List  
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a: str, b: str): return int(a + b) - int(b + a)
        strnums = sorted(map(str, nums), key=cmp_to_key(cmp), reverse=True)
        return '0' if strnums[0]=='0' else ''.join(strnums)

if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([10,2]))
