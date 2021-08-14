from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        order = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                order[i][preferences[i][j]] = j
        
        match = [0] * n
        for xy in pairs:
            match[xy[0]] = xy[1]
            match[xy[1]] = xy[0]

        unhappyCount = 0
        for x in range(n):
            y = match[x]
            index = order[x][y]
            for i in range(index):
                u = preferences[x][i]
                v = match[u]
                if order[u][x] < order[u][v]:
                    unhappyCount += 1
                    break
        
        return unhappyCount

