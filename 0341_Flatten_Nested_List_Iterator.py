class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = []
        def dfs(nestedList: [NestedInteger]) -> None:
            for l in nestedList:
                if l.isInteger():
                    self.list.append(l.getInteger())
                else:
                    dfs(l.getList())
        dfs(nestedList)
        self.start = -1

    def next(self) -> int:
        self.start += 1
        return self.list[self.start]

    def hasNext(self) -> bool:
        if self.start < len(self.list) - 1:
            return True
        return False

