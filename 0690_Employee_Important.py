from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        re = {employee.id: employee for employee in employees}
        def dfs(root: int) -> int:
            ans = re[root].importance
            if len(re[root].subordinates) == 0:
                return ans
            for em in re[root].subordinates:
                ans += dfs(em)
            return ans
        return dfs(id)


if __name__ == '__main__':
    s = Solution()

