from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [0xfffffff for _ in range(n)]
        visit = [False for _ in range(n)]
        edges = dict()
        for t in times:
            edges[(t[0] - 1, t[1] - 1)] = t[2]
        dist[k - 1] = 0
        while True:
            # print(dist)
            u = -1
            maxtime = 0xfffffff
            for i in range(n):
                if dist[i] < maxtime and not visit[i]:
                    u = i
                    maxtime = dist[i]
            if u == -1:
                break
            visit[u] = True
            for v in range(n):
                if not visit[v] and (u, v) in edges:
                    if dist[u] + edges[(u, v)] < dist[v]:
                        dist[v] = dist[u] + edges[(u, v)]
        ans = max(dist)
        return ans if ans != 0xfffffff else -1


if __name__ == '__main__':
    s = Solution()
    print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
