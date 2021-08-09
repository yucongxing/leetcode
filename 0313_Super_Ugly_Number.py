from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ans = [1 for _ in range(n)]
        p = [0 for _ in range(len(primes))]

        last = 0
        while last < n - 1:
            next = 0xffffffff
            for i in range(len(primes)):
                minnum = primes[i] * ans[p[i]]
                if minnum < next and minnum > ans[last]:
                    next = minnum
            last += 1
            ans[last] = next
            
            for i in range(len(primes)):
                if primes[i] * ans[p[i]] == next:
                    p[i] += 1
        return ans[n - 1]

if __name__ == '__main__':
    s = Solution()
    print(s.nthSuperUglyNumber(12, [2,7,13,19]))
    print(s.nthSuperUglyNumber(1, [2,3,5]))

