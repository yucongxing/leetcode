from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        path = list()
        ans = list()

        def dfs(u):
            nonlocal path
            path.append(u)
            if u == n - 1:
                nonlocal ans
                ans.append(path[:])
                path.pop(-1)
                return
            for v in graph[u]:
                dfs(v)
            path.pop(-1)

        dfs(0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.allPathsSourceTarget([[1, 2], [3], [3], []]))
    print(s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
