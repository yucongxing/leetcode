from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        vis = [[False for _ in range(1 << n)] for _ in range(n)]
        q = list()
        for i in range(n):
            q.append((i, 1 << i, 0))
            vis[i][1 << i] = True

        ans = 0
        while q:
            u, mask, dist = q.pop(0)
            if mask == (1 << n) - 1:
                ans = dist
                break
            for v in graph[u]:
                mask_v = mask | (1 << v)
                if not vis[v][mask_v]:
                    q.append((v, mask_v, dist + 1))
                    vis[v][mask_v] = True
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))
