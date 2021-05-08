from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        l, r = jobs[0], sum(jobs)
        while l < r:
            middle = (l + r) // 2
            if self.check(jobs, k, middle):
                r = middle
            else:
                l = middle + 1
        return l

    def dfs(self, jobs: List[int], workloads: List[int], idx: int, limit: int) -> bool:
        if idx >= len(jobs):
            return True
        cur = jobs[idx]
        for i in range(len(workloads)):
            if workloads[i] + cur <= limit:
                workloads[i] += cur
                if self.dfs(jobs, workloads, idx + 1, limit):
                    return True
                workloads[i] -= cur
            if workloads[i] == 0 or workloads[i] + cur == limit:
                break
        return False

    def check(self, jobs: List[int], k: int, limit: int) -> bool:
        workloads = [0 for _ in range(k)]
        return self.dfs(jobs, workloads, 0, limit)


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTimeRequired([3,2,3], 3))
    print(s.minimumTimeRequired([1,2,4,7,8], 2))
