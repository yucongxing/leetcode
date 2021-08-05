from typing import List
from functools import lru_cache


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        used = [False for _ in range(n)]
        visited = [False for _ in range(n)]
        safe = [False for _ in range(n)]
        ans = list()
        @lru_cache()
        def dfs(u):
            used[u] = True
            visited[u] = True
            if len(graph[u]) == 0:
                visited[u] = False
                if not safe[u]:
                    ans.append(u)
                    safe[u] = True
                return
            for v in graph[u]:
                if visited[v]:
                    visited[u] = False
                    return
                if not used[v]:
                    dfs(v)
                if not safe[v]:
                    visited[v] = False
                    return
            if not safe[u]:
                safe[u] = True
                ans.append(u)
            visited[u] = False
        for i in range(n):
            if not used[i]:
                dfs(i)
        ans.sort()
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
    print(s.eventualSafeNodes([[],[0,2,3,4],[3],[4],[]]))

