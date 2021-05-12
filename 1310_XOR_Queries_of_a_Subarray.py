from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        re = [0 for _ in range(n)]
        re[0] = arr[0]
        for i in range(1, n):
            re[i] = re[i - 1] ^ arr[i]
        ans = list()
        for query in queries:
            if query[0] == 0:
                ans.append(re[query[1]])
            else:
                ans.append(re[query[1]] ^ re[query[0] - 1])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.xorQueries([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]]))
